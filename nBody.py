# Run a n-body simulation on the solar system
# adds five planets, the Sun, and Halley's comet

from Ramnell import *
from Rforces import *
AU = 150*10**9 #m

#define the objects as particles
sun = Particle('sun',[0,0,0],[0,0,0], 1.989*10**30, 86*10**7)
mercury = Particle('Mercury',[0,AU*.387,0],[47000,0,0], 3.285*10**23, 2439*10**3)
venus = Particle('Venus',[.723*AU, 0, 0],[0,35000,0],4.8*10**24 ,6051000)
earth = Particle('Earth',[0,AU,0],[30000,0,0], 5.9*10**24, 6371000)
mars = Particle('Mars',[1.524*AU, 0, 0],[0,24000,0],6.7*10**23 ,6974000)
comet = Particle('Comet',[0,AU*.586,0],[55000,0,0], 3.285*10**23, 11000)
jupiter = Particle('Jupiter',[5.2*AU, 0, 0],[0,13000,0],1.9*10**27 ,67000000)

output = open("nBody.txt", "w+")

#add each element to a system
system = Sys('solar system')
system + sun
system + earth
system + mars
system + mercury
system + venus
system + comet
system + jupiter


system.announce() #display which particles are in the system
addGravity(system) #add gravity between each particle in the system

output.write("Time | %s\n" % repr(["pos %s" % n.name + ',' for n in system.parts]) + "\n") #header
step = 1000 #s  
for i in range(0,100000): #simulate over the course of three years
    if i % 5000 == 0:
        print("%.2f%% done" % (i/1000)) #show progress
    output.write(str(step * i))
    for n in system.parts:
        output.write(repr(n.pos)) #write to the file
    output.write("\n")
    system.tickAll(step) #update the entire system at once

output.close() #close the file
    




