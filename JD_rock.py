#! /usr/bin/env python3

# Control the robot using telnet commands
import telnetlib
import time

host = "192.168.1.1"
port = 23

class JD_Robot:
    def __init__(self):
        self.connect_telnet()
        self.music_track = 0

    def connect_telnet(self):
        self.tn = telnetlib.Telnet(self.host, self.port)

    def play_music(self):
        self.tn.write(
            'controlCommand("Soundboard v4", "Track_' + str(self.music_track) + '")')
        self.music_track = (self.music_track + 1) % 10

    def stop_music(self):
        self.tn.write('controlCommand("Soundboard v4", "Stop")')

    def wink(self):
        self.tn.write(
            'controlCommand("RGB Animator", "AutoPositionAction", "Wink")')

    def disco_dance(self):
        self.tn.write(
            'controlCommand("Auto Position", "AutoPositionAction", "Disco Dance")')

    def pre_dance(self):
        self.tn.write(
            'controlCommand("Auto Position", "AutoPositionAction", "Predance")')

    def happy_hands(self):
        self.tn.write(
            'controlCommand("Auto Position", "AutoPositionAction", "Happy Hands")')
        
    def rock_n_roll(self):
        self.wink()
        time.sleep(1)
        self.play_music()
        time.sleep(1)

        i = 0
        while i < 10:
            self.pre_dance()
            time.sleep(3)
            self.disco_dance()
            time.sleep(3)
            self.happy_hands()
            time.sleep(3)
            i += 1

        self.stop_music()
        self.tn.close()

if __name__ == '__main__':
    JD = JD_Robot()
    JD.rock_n_roll()
