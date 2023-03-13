#! /usr/bin/env python3

# Control the robot using telnet commands
import telnetlib
import time

host = "192.168.1.3"
port = 6666


class Rover:
    def __init__(self):
        self.connect_telnet()
        self.music_track = 0

    def connect_telnet(self):
        self.tn = telnetlib.Telnet(host, port)

    def play_music(self):
        msg = 'controlCommand("Soundboard v4", "Track_' + str(self.music_track) + '")\r\n'
        self.tn.write(
            (msg.encode('ascii')))
        self.music_track = (self.music_track + 1) % 7

    def stop_music(self):
        self.tn.write(b'controlCommand("Soundboard v4", "Stop")\r\n')

    def clap(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Clap")\r\n')
        
    def dance(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Dance")\r\n')
        
    def hands_dance(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Hands Dance")\r\n')
        
    def head_bang(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Head Bang")\r\n')
        
    def head_scratch(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Head Scratch")\r\n')
        
    def wave_left(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Wave Left")\r\n')
        
    def wave_right(self):
        self.tn.write(
            b'controlCommand("Auto Position", "AutoPositionAction", "Wave Right")\r\n')
        
    def rock_n_roll(self):
        self.play_music()
        time.sleep(2)

        i = 0
        while i < 7:
            self.clap()
            time.sleep(3)
            self.dance()
            time.sleep(3)
            self.hands_dance()
            time.sleep(3)
            self.play_music()
            i += 1

        self.stop_music()
        time.sleep(1)
        self.tn.close()

if __name__ == '__main__':
    Roli = Rover()
    Roli.rock_n_roll()
