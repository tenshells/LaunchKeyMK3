# name=Novation Launchkey 49 MK3
#Script_Madeby_SheltonChiramal
#Instagram_@tenshells

import transport
import midi
import mixer
import general

#shells imports
import ui
import channels
import playlist
import launchMapPages
import plugins
# import pykeys

#Below are the variables which can be changed
play_button = 115
stop_button = 116
record_button = 117
undo_button = 77
loop_button = 118

#shells changes
prev =102
next =103

# TODO:
# PITCH WHEEL AUTO TO EVERY DIRTY CHANNEL,


capmidi = 74
quant = 75
metro = 76
DeviceSelect =51
DeviceLock = 52
DS = -1


RightArrow = 104
SSM = 105

UpArrow = 106
DownArrow = 107

fadbut1 = 11
#exit shells

fader = (71,72,73,74,75,76,77,78,79)

knobs = [21,22,23,24,25,26,27,28]

#Function starts from below
def OnMidiMsg(transport_controller):
    transport_controller.handled= False
    print(transport_controller.midiId,transport_controller.status, transport_controller.port, transport_controller.data1, transport_controller.data2)
    if transport_controller.midiId == midi.MIDI_CONTROLCHANGE:
        #buttons
        tc = transport_controller
        global Mr,Ml,Mu,Md
        if transport_controller.data2 > 0 and transport_controller.midiId ==176:
            
            #Basic Transport Controls
            if transport_controller.data1 == play_button:
                print('Start')
                # print(f"Here port is {transport_controller.port} and it is of type {type(transport_controller.port)}")
                transport.start()
                transport_controller.handled = True
            if transport_controller.data1 == stop_button:
                print('Stop')
                transport.stop()
                transport_controller.handled = True
            if transport_controller.data1 == record_button:
                print('Record')
                transport.record()
                transport_controller.handled = True
            if transport_controller.data1 == loop_button:
                print('Pattern/Song Mode')
                transport.setLoopMode()
            if transport_controller.data1 == prev:
                print('General Previous and livePlaylist +1s')
                ui.previous()
                transport_controller.handled = True		
            if transport_controller.data1 == next:
                print('General Next and livePlaylist -1s')
                ui.next()
                transport_controller.handled = True	
            
            #up and down arrows for prev,next presets... #redundant with current jog wheels doing same thing :)
            if transport_controller.data1 == UpArrow:
                print('prevPreset')
                plugins.prevPreset(channels.selectedChannel())
                transport_controller.handled = True	    
            if transport_controller.data1 == DownArrow:
                print('nextPreset')
                plugins.nextPreset(channels.selectedChannel())
                transport_controller.handled = True
            
            #switch Channel Rack -> Playlist -> Mixer
            if transport_controller.data1 == DeviceSelect:
                if transport_controller.data2 == 127:
                    global DS
                    if DS == -1 or DS == 0:
                        ui.setFocused(1)
                        DS = 1
                        print("focus on racks yo")
                    elif DS == 1:
                        ui.setFocused(2)
                        DS = 2
                        print("focus on soul yo")
                    elif DS == 2:
                        ui.setFocused(0) 
                        DS = 0   
                        print("focus on picture yo")
                    transport_controller.handled = True
            
            #learn plugins 
            if transport_controller.data1 == DeviceLock:
                # print(f"the plugin in selected channel is {plugins.getPluginName(channels.selectedChannel())}")
                if plugins.getPluginName(channels.selectedChannel()) == "3x Osc":
                    print("Hey old triple :)")
                else:
                    print(f"Hey {plugins.getPluginName(channels.selectedChannel())} `)")
                print(f"I see you got {plugins.getParamCount(channels.selectedChannel())} parameters")
                for i in range(plugins.getParamCount(channels.selectedChannel())):
                    print(f"{i+1:2}  {plugins.getParamName(i,channels.selectedChannel()):25} is {plugins.getParamValue(i,channels.selectedChannel())}")
                transport_controller.handled = True
            
            #show editor at selected channel
            if transport_controller.data1 == RightArrow:
                print('RA: Show Editor at SC ')
                channels.showEditor(channels.selectedChannel())
                transport_controller.handled = True	
            
            #solo channel
            if transport_controller.data1 == SSM:
                print('Solo Channel')
                channels.soloChannel(channels.selectedChannel())
                transport_controller.handled = True	   
            
            #for transport controls who overlap with faders...
            if transport_controller.status == 191:
                if transport_controller.data1 == undo_button:    
                    print('Undo')
                    general.undo()
                    transport_controller.handled = True		
                if transport_controller.data1 == metro:
                    print('Metronome')
                    transport.globalTransport(midi.FPT_Metronome,110)
                    transport_controller.handled = True	
                if transport_controller.data1 == quant:
                    print('Quick Quantise, tbd')
                    channels.quickQuantize(channels.selectedChannel)
                    transport_controller.handled = True	
                if transport_controller.data1 == capmidi:
                    print('Capture Midi,  tbd')
                    # transport.globalTransport(midi.FPT_Metronome,110)
                    transport_controller.handled = True	
        
        #for faders
        if transport_controller.status == 176:
            if transport_controller.data1 == fader[8]:
                print('Master Volume')
                mixer.setTrackVolume(0,0.63 * (transport_controller.data2 / 100))
                # if transport_controller.data2 == 127:
                #     print("Master capped at 100 :)")
                transport_controller.handled = True
            if transport_controller.data1 == fader[0]:
                print('Mixer Channel 1 Volume')
                mixer.setTrackVolume(1,0.63 * transport_controller.data2 / 100)
                transport_controller.handled = True
            if transport_controller.data1 == fader[1]:
                print('Mixer Channel 2 Volume')
                mixer.setTrackVolume(2,0.63 * transport_controller.data2 / 100)
                transport_controller.handled = True

        #for knobs
        if transport_controller.data1 == knobs[0]:
            print('Control Volume of Selected Channel')
            channels.setChannelVolume(channels.selectedChannel(),tc.data2/127)
            transport_controller.handled = True	        

        if transport_controller.data1 == knobs[1]:
            print('Control Pan of Selected Channel')
            channels.setChannelPan(channels.selectedChannel(),tc.data2/63.5 - 1)
            transport_controller.handled = True	           
    
    #Pitch Wheel controls pitch with semitone range +-12
    if transport_controller.midiId == 224:
        print('Pitch Bend Range')
        channels.setChannelPitch(channels.selectedChannel(),12,2)
        pro = transport_controller.data2 * 128 + transport_controller.data1        
        channels.setChannelPitch(channels.selectedChannel(),pro/8192 -1)
        transport_controller.handled = True	
