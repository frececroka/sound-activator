# sound-activator

Automatically turn your speakers on if sound is playing.

## Usage

The `asound` node in the `procfs` is used to determine whether audio is currently playing. You therefore must use ALSA to play sound. You need external switching hardware (e.g. a relay) to turn your speaker on and off. The code sets GPIO 2 high (VCC) if sound is playing and low (GND) if sound is not playing. The switching hardware should turn the speaker on/off depending on this digital signal.
