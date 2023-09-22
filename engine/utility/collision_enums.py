from enum import Enum

class CollisionModes(Enum):
    quick = 0
    exact = 1
     
class CollisionTypes(Enum):
    world   = 0
    static  = 1
    dynamic = 2
    
class CollisionDirection(Enum):
    right = 0
    up    = 1
    left  = 2
    down  = 3
