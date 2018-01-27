#Ramnell

def sumVectors(vectorList):
    vec = Vector([0,0,0])
    for i in vectorList:
        vec += i
    return vec

class Sys():
    def __init__(self, name):
        self.name = name
        self.parts = []
        self.fields = []
        self.obstacles = []
        self.typ = 's'

    def __add__(self, target):
        if target.typ == 'p':
            if target not in self.parts: self.parts.append(target)
        elif target.typ == 'f':
            if target not in self.fields: self.fields.append(target)
        elif target.typ == 'o': 
            if target not in self.obstacles: self.obstacles.append(target)
        elif target.typ == 's': print("Can't add systems to systems")
        else: print("invalid type")

    def __sub__(self, target):
        if target.typ == 'p' and target in self.parts:
            self.parts.remove(target)
        elif target.typ == 'f' and target in self.fields:
            self.fields.remove(target)
        elif target.typ == 'o' and target in self.obstacles:
            self.obstacles.remove(target)
        elif target.typ == 's': print("Can't remove systems from systems")

    def tickAll(self, step):
        for i in self.parts:
            i.tick(step)

    def announce(self):
        for i in self.parts: print("Particle: ", i.name)
        for i in self.fields: print("Field: ", i.name)
        for i in self.obstacles: print("Obstacle: ",i.name)

    def anyContact(self):
        for i in self.parts:
            for j in self.parts:
                if i != j and i.contact(j):
                    return True
        return False

class Vector():
    def __init__(self,body):
        self.body = body
        self.typ = 'v'

    def __add__(self,target):
        '''vector addition'''
        if not len(self) == len(target):
            print("Vector Sum not defined for vectors of unequal length")
        else: return Vector([self.body[i] + target.body[i] for i in range(0,len(self))])

    def __sub__(self, target):
        '''vector subtraction'''
        if not len(self) == len(target):
            print("Vector Subtraction not defined for vectors of unequal length")
        else: return Vector([self.body[i] - target.body[i] for i in range(0,len(self))])

    def cross(self, target):
        '''cross products'''
        if len(self) == 3 and len(target) == 3:
            i = self.body[1] * target.body[2] - self.body[2] * target.body[1]
            j = - self.body[0] * target.body[2] + self.body[2] * target.body[0]
            k = self.body[0] * target.body[1] - target.body[0] * self.body[1]
            return Vector([i,j,k])
        if not len(self) == len(target):
            print("Cross Product not defined for vectors of unequal length")
        else:
            print("Cross Product not defined in %d dimensions" % (len(self)))

    def dot(self,target):
        '''dot products'''
        if not len(self) == len(target):
            print("Dot Product not defined for vectors of unequal length")
        else: return sum([self.body[i] * target.body[i] for i in range(0,len(self))])

    def __mul__(self,scalar):
        return Vector([self.body[i] * scalar for i in range(0,len(self))])

    def mag(self):
        return sum([v ** 2 for v in self.body]) ** .5

    def show(self, prnt = 1):
        if prnt == 1: print(self.body)
        return self.body

    def __len__(self):
        return len(self.body)

    def __repr__(self):
        return str(repr(self.body))

    def unit(self):
        return self * (1/self.mag())


class Particle(object):
    #used for spherical objects

    def __init__(self,name, pos, vel, mass,radius):
        self.name = name
        self.pos = Vector(pos)
        self.vel = Vector(vel)
        self.mass = mass
        self.size = radius
        self.forces = []
        self.typ = 'p'

    def show(self):
        print("Particle: ", self.name)
        print("Radius: ", self.size)
        print("Mass: ", self.mass)
        print("Position:", self.pos.show(prnt = 0))
        print("Velocity: ", self.vel.show(prnt = 0), self.vel.mag())
        print("Momentum: ", (self.vel * self.mass).show(prnt = 0))
        print("Forces: ", [i.name for i in self.forces])
        
    def displacement(self, target):
       self.disp = (self.pos - target.pos)
       return self.disp
       
    def addForce(self, force):
        self.forces.append(force)

    def remForce(self, force):
        self.forces.remove(force)
    
    def contact(self, target):
        if self.displacement(target).mag() <= (self.size + target.size): return True
        else: return False

    def tick(self, step):
        a = sumVectors([n.evaluate(self) for n in self.forces]) * (1 / self.mass)
        self.vel += a * step
        self.pos += self.vel * step

    def freeze(self):
        self.vel = Vector([0,0,0])


class Obstacle(object):
    '''rigid, immobile objects'''
    def __init__(self,name,pos,func):
        self.pos = pos
        self.func = func
        self.name = name
        self.typ = 'o'

    def contact(self, target):
        if abs(self.func(target.pos)) <= target.size:
            return True
        else:
            return False

class Force(Vector):
    '''forces on or between particles'''
    def __init__(self,name, func, target = None, pos = 'self'):
        self.target = target
        self.name = name
        if type(pos) == type(Vector([])):
            self.pos = pos
        elif type(pos) == 'self':
            self.pos = None
        self.func = func

    def evaluate(self,particle):
        b = self.func(self,particle,self.target)
        return b


    '''apply forces to every particle in a system. Makes them behave like fields'''
    def addField(self,sys):
        for i in sys.parts:
            if self not in i.forces:
                i.addForce(self)
                
    def remField(self,sys):
        for i in sys.parts:
            if self in i.forces:
                i.forces.remove(self)


