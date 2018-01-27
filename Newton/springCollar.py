#model systems acting under gravity, friction and springs
#used to check physics homework problems

from math import sin, cos, radians

massOne = 10 #kg
timeStep = .1 #s
step = 0
sprPos = .75 #m
sprConst = 1000 #N/m
angle = 50 #angle off horizontal
fricCoeff = .28 

constants = (massOne,timeStep,fricCoeff,angle,sprConst)

posOne = 15 #m
velOne = -6 #/ms
accOne = 0 #m/s/s
disp = posOne + sprPos

variables = [velOne,posOne,accOne,disp]

def getAccel(constants,variables):
    #forces, in the direction of motion
    forceG = -massOne * 9.81 * sin(radians(angle))#force of gravity
    
    if variables[3] <= 0: forceS = - sprConst * variables[3]    #force of the spring
    else: forceS = 0
    
    forceF = - fricCoeff * massOne * 9.81 * cos(radians(angle)) #force of friction
    if variables[0] <= 0:
        forceF *= -1

#    print(forceF,forceG,forceS)
    variables[2] = (forceG + forceF + forceS) / massOne #sum of forces = ma
    return variables

def getVelocity(constants,variables):
    variables[0] += variables[2]*timeStep               #v = vi + at
    return variables


def getPosition(constants,variables):
    variables[1] += variables[0]*timeStep              #x = xi + vt
    variables[3] = variables[1] + sprPos                #recaclulate the distance to the spring
    return variables

#posData = [] #used to graph position
while step < 100: 
#while variables[1] > 0: #stop when it reaches the ground
#while variables[0] <= -0.1: #stop when it comes to rest
    print(int((variables[3] + 10)) * ' ' , '*') #plots position vs time in the command line
    variables = getAccel(constants,variables)
    variables = getVelocity(constants,variables)
    variables = getPosition(constants,variables)
    step += 1
    #posData.append(variables[1]) #used to graph position
    
'''print the final condition'''
print(step*timeStep, ' Seconds')
print(variables)
print(posData)
