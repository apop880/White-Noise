# White Noise
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
<a href="https://www.buymeacoffee.com/uMhxJCzPS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

_A white noise machine for a `media_player` entity._

## Installation

This app is best installed using
[HACS](https://github.com/custom-components/hacs), so that you can easily track
and download updates.

Alternatively, you can download the `whitenoise` directory from inside the `apps` directory here to your
local `apps` directory, then add the configuration to enable the `whitenoise`
module.

## How it works

You can define an instance of the app in your apps.yaml file for every
white noise machine you'd like to configure. As a pre-requisite, you will need
an audio file that is an hour or more long. My recommendation is to download one
of the 60 minute files from [here](https://mc2method.org/white-noise/) to your
`www` directory.

The app is configured to play the audio file on the configured speaker. Every 55
minutes, it will automatically fade the volume out on the speaker, so that it
can restart the audio file without it sounding abrupt. Then the volume will fade
in to what it was previously. This way, you're able to use a file of a
reasonable length, rather than creating a file that is 8+ hours long and takes
up an unnecessary amount of space on your server.

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

## Issues/Feature Requests

Please log any issues or feature requests in this GitHub repository for me to review.