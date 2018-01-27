#a number of useful functions for defining forces in the Ramnell physics engine
    
from Ramnell import *

#define some constants
from math import pi as PI
G = 6.6726 * 10 **-11 
g = 9.81

#define a weight force acting in the negative j direction. For kinematics
weight = Force('weight',lambda sel,par,targ: Vector([0,par.mass * g,0]))

def gravity(tar):
    return Force('gravity %s' %(tar.name),lambda sel,par,tar:  par.displacement(tar).unit() * -G * par.mass * tar.mass * (1/par.displacement(tar).mag()) ** 2, target = tar)

def addGravity(system):
    '''adds gravity to all particles'''
    for i in system.parts:
        for j in system.parts:
            if i != j:
                i.addForce(gravity(j))

def drag(CD = .5, dens = 1.3):
    '''define a drag force with variable CD and air density. Assumed spherical objects'''
    return Force('drag', lambda sel,par,tar: par.vel * -.5 * CD * dens * par.size ** 2* PI * par.vel.mag())

def spring(const):
    '''define an omnidirectional spring'''
    return Force('spring', lambda sel,par,tar: par.displacement(sel) * par.displacement(sel).mag() * (const /2))

def plane(normal, point, name= 'plane'):
    '''define a plane to contact objects'''
    return Obstacle(name, point, lambda pos: normal.dot(point - pos))
    
def runProjectile(system,step):
    '''update the particles as long as they are above the ground obstacle'''
    #requires a ground obstacle defined
    t = 0
    while True:
        numVal = len(system.parts)
        for i in system.parts:
            if not ground.contact(i):
                i.tick(step)
            else:
                print(i.name,i.pos.show(prnt = 0), t * step)
                system - i
        if numVal == 0:
            break
        t += 1

