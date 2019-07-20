<a href="https://www.buymeacoffee.com/uMhxJCzPS" target="_blank"><img
src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"
alt="Buy Me A Coffee" style="height: 41px !important;width: 174px
!important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5)
!important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5)
!important;" ></a>

## App configuration

Define the app once for each white noise machine you want to create, giving it a unique name each time.

```yaml
white_noise:
  module: whitenoise
  class: WhiteNoise
  media_player: master_bedroom_speaker
  input_boolean: white_noise
  filename: https://xyz.duckdns.org/local/audio/42-Rain-60min.mp3
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `whitenoise`
`class` | False | string | | `WhiteNoise`
`media_player` | True | string || The `media_player` entity you want to use as a white noise machine. You only need to list the portion to the right of the period, so in the example above `media_player.master_bedroom_speaker` is the full `entity_id` being used.
`input_boolean` | True | string || An `input_boolean` you have defined to control the white noise machine. As with `media_player`, you only need the portion after the period, so for the example above, `input_boolean.white_noise` is the full `entity_id` controlling this white noise machine.
`filename` | True | string || The location of the white noise file. You may have to play with this depending on what type of `media_player` you are using. I am using a Google Home, and that device requires a URL it can hit over the internet, so I had to use my external URL rather than the IP address on my local network.