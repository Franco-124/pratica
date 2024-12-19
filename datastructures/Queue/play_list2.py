from time import sleep
from random import randint
from node_queue import Queue

class Tracks:
    def __init__(self, title = None):
        self.title = title
        self.length= randint(5,10)
    

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()
    
    def add_track(self, track):
        self.enqueue(track)
    
    def play(self):
        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.title))
            sleep(current_track_node.length)


def main():
    track1 = Tracks("white whistle")
    track2 = Tracks("butter butter")
    track3 = Tracks("Oh black star")
    track4 = Tracks("Watch that chicken")
    
    track_player = MediaPlayerQueue()
    track_player.add_track(track1)
    track_player.add_track(track2)
    track_player.add_track(track3)
    track_player.add_track(track4)
    
    track_player.play()
main()