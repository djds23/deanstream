import collections
import random
import models

class Randomizer():
    def __init__(self):
        self.videos = [i for i in range(models.Video.query.count()+1) if models.Video.query.get(i) != None]

    def gen_random_video(self, denom=2):
        '''return a video that hasn't recently been watched'''
        recently_watched = collections.deque(maxlen=len(self.videos)//denom)
        while True:
            selection = random.choice(self.videos)
            if selection not in recently_watched:
                yield selection
                recently_watched.append(selection)
