import appdaemon.plugins.hass.hassapi as hass

class WhiteNoise(hass.Hass):
#White Noise Machine	
	def initialize(self):
		#assemble the input_boolean
		self.switch = "input_boolean." + self.args['input_boolean']
		#assemble the speaker
		self.speaker = "media_player." + self.args['media_player']
		#get the filename
		self.filename = self.args['filename']
		#listener for the input boolean
		self.listen_state(self.state_switch, self.switch)
		#timer to restart the track hourly
		self.loop_timer = None
		#listener for if the music turns off
		self.media_listener = None
		#get the current_volume so we can fade out/in
		self.original_volume = 0
		#run a fade out/in to keep in sync if switch is already on
		if self.get_state(self.switch) == "on":
			self.run_in(self.repeat_track, 0, action = "out")
			self.media_listener = self.listen_state(self.media_stopped,
				self.speaker,
				old = "playing", duration = 30)

	def state_switch(self, entity, attribute, old, new, kwargs):
		if new == "off":
			self.turn_off(self.speaker)
			self.cancel_timer(self.loop_timer)
			self.cancel_listen_state(self.media_listener)
			if self.original_volume != 0:
				self.call_service("media_player/volume_set",
					entity_id = self.speaker,
					volume_level = self.original_volume)
				self.original_volume = 0
		else:
			#start the white noise
			self.call_service("media_player/play_media",
				entity_id = self.speaker,
				media_content_type = "music",
				media_content_id = self.filename)
			#restart the track in 55 minutes
			#will only run if the input boolean is still on
			self.loop_timer = self.run_in(self.repeat_track, 60*55, action = "out")
			#start the listener for if the music turns off, so that the switch
			#doesn't get out of sync
			self.media_listener = self.listen_state(self.media_stopped,
				self.speaker,
				old = "playing", duration = 30)

	def repeat_track(self, kwargs):
		if kwargs["action"] == "out":
			if self.original_volume == 0:
				#starting fade out
				self.original_volume = self.get_state(self.speaker, attribute = "volume_level")
				self.call_service("media_player/volume_down", entity_id = self.speaker)
				self.loop_timer = self.run_in(self.repeat_track, 7, action = "out")
			elif self.get_state(self.speaker, attribute = "volume_level") > 0.1:
				#fade out in progress
				self.call_service("media_player/volume_down", entity_id = self.speaker)
				self.loop_timer = self.run_in(self.repeat_track, 7, action = "out")
			else:
				#volume is low enough, start track again
				self.call_service("media_player/play_media",
					entity_id = self.speaker,
					media_content_type = "music",
					media_content_id = self.filename)
				#call fade in
				self.loop_timer = self.run_in(self.repeat_track, 7, action = "in")
		else:
			if self.get_state(self.speaker, attribute = "volume_level") < self.original_volume:
				#still fading in
				self.call_service("media_player/volume_up", entity_id = self.speaker)
				self.loop_timer = self.run_in(self.repeat_track, 7, action = "in")
			else:
				#back to original volume
				self.original_volume = 0
				#schedule another restart in 55 minutes
				self.loop_timer = self.run_in(self.repeat_track, 60*55, action = "out")

	def media_stopped(self, entity, attribute, old, new, kwargs):
		if self.get_state(self.speaker) != "playing":
			self.turn_off(self.switch)