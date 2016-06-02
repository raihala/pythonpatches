import random
import time

class Object(object):
    """
    An improvement over the default object class.
    """
    __doc__ = "None"
    
    def __getattr__(self, name):
        time.sleep(random.random() * 10)
        raise OSError("Python encountered a problem. "
                      "You must reboot your computer!")
    
    def __setattr__(self, name, value):
        pass
    
    def __repr__(self):
        return "None"

    def __dir__(self):
        return []
    
    def __cmp__(self, other):
        return random.random() > 0.5
    
    def __nonzero__(self):
        return random.random() > 0.5
    
    def __del__(self):
        time.sleep(random.random() * 5)
