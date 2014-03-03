import collections
import random

def gen_random_video(video, denom=2):
    '''return a video that hasn't recently been watched'''
    recently_watched = collections.deque(maxlen=len(video)//denom)
    while True:
        selection = random.choice(video)
        if selection not in recently_watched:
            yield selection
            recently_watched.append(selection)
