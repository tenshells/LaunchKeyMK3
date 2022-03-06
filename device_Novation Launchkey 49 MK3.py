# name=Novation Launchkey 49 MK3
#Script_Madeby_RemoViky
#Instagram_@sbrmnyn.a

import transport
import midi
import mixer
import general

#shells imports
import ui
import channels

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

SSM = 105

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
        if transport_controller.data2 > 0:
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
                print('General Previous')
                ui.previous()
                transport_controller.handled = True		
            if transport_controller.data1 == next:
                print('General Next')
                ui.next()
                transport_controller.handled = True	
            
            #for overlaps with faders...
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

            if transport_controller.data1 == SSM:
                print('Solo Channel')
                channels.soloChannel(channels.selectedChannel())
                transport_controller.handled = True	    
        
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
        
        
        
            	
            
            