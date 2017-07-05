# Scene: parent class for all scenes
from sys import exit

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
