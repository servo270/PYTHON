#spring model
from math import sin, cos, radians

massOne = 10
timeStep = .1
step = 0
sprPos = .75
sprConst = 1000
angle = 50 #angle off horizontal
fricCoeff = .28

constants = (massOne,timeStep,fricCoeff,angle,sprConst)

posOne = 15
velOne = -6
accOne = 0
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

#posData = []
while step < 100:
#while variables[1] > 0:
#while variables[0] <= -0.1:
    print(int((variables[3] + 10)) * ' ' , '*')
    variables = getAccel(constants,variables)
    variables = getVelocity(constants,variables)
    variables = getPosition(constants,variables)
    step += 1
    #posData.append(variables[1])
print(step*timeStep, ' Seconds')
print(variables)
print(posData)
