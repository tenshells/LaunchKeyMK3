# LaunchKeyMK3

Python Script to run in FL Studio versions 20.8 and above.

Supports Launchkey 25,37,49,61.

Note 49,61 keys provide extra functionality for 9 faders and 9 fader buttons.
No support for Launchkey Mini mk3 yet, willing to work with someone who has a LK mini mk3 to add script.

Availible in 25,37,49,61 :
  - Transport: Play/Pause, Stop, Record, switch from Song Mode/Pattern Mode, Undo, Metronome(Click).
  - Device Select can be used to add new plugin to channel rack/mixer 
  - Device Lock button next to knobs can be used to switch from Channel Rack -> Playlist -> Mixer
  - Jog buttons for previous/next for use in browser/Mixer/Channel Rack/switching presets in FL Stock plug-ins like Flex etc.
  - Stop Solo Mute button for Soloing Channel
  - Pitch Wheel for selected channel with semitone range +-12
  - First knob, Second Knob (in pot mode 1) Controls selected channel volume, pan

Avalible for 49,61 key versions:
Faders:
  The faders have a max ceiling at 100% volume (0dB) to avoid clipping/ruining speakers :)
  - Master fader controls Master Volume
  - First 2 faders linked to first two Mixer Channels

Upcoming Support:
  - Plugin Support for FLEX, 3xOsc, FL keys..
  - Switching to Mixer using Device Lock Mode enables first 8 faders to control 8 mixer channel volumes 
  - Control, Alt, Shift support in Launchpad probably with Up, Down 
  - Quantize quick Quantizes selected channel

SETUP:
  - just download this .py script and put it in a folder (name not important, could be LaunchkeyMK3 or PurpleHaze), this folder should be in your User Data Folder of FL Studio which could either be in Documents\Image-Line\FL Studio\Settings\Hardware\ or C:\Program Files\Image-Line\FL Studio 20\System\Hardware specific, try both :)
  - for any doubts check the Developer's Guide or feel free to message me on Discord, my username is : 10shelcaramel#4945
 
Helpful Tips:
  *Coming Soon!*

Developer's Guide:
  https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm
  
Special Thanks to:
  * https://github.com/rjuang for the pykeys module which will use Control, Shift, Alt so you can work independently of the keyboard in the future!
  * https://github.com/MiguelGuthridge  for inspiring me in how much you can extend support for a midi controller! Check out his Universal Controller Script!
  * Remo Viky for creating the first Launchkey MK3 script that i found, which taught me the basics of scripting
  
