#spring model
from math import sin, cos, radians, pi
#apple: .136 tennis ball: .0585
massOne = 130 / 1.6
timeStep = .001
step = 0
sprPos = 0
sprConst = 000
angle = 90 #angle off horizontal
fricCoeff = 0
area = .6
dragCoeff = .8
airDens = 1.2
resConst = .1

constants = (massOne,timeStep,fricCoeff,angle,sprConst, area, dragCoeff, airDens)

term = 0
#posOne = (6*10.66 + 14 + 3.5)/ 3.1
posOne = 11.4
velOne = -.1
accOne = 0
disp = posOne + sprPos

variables = [velOne,posOne,accOne,disp,term]

def getAccel(constants,variables):
    #forces, in the direction of motion
    forceG = -massOne * 9.81 * sin(radians(angle))#force of gravity
    
    if variables[3] <= 0: forceS = - sprConst * variables[3]    #force of the spring
    else: forceS = 0
    
    forceF = - fricCoeff * massOne * 9.81 * cos(radians(angle)) #force of friction
    if variables[0] <= 0:
        forceF *= -1
    #forceD = 0
    forceD = -.5 * dragCoeff * airDens * area * variables[0] * abs(variables[0])
    #print(forceF,forceG,forceS,forceD)
    variables[2] = (forceG + forceF + forceS + forceD) / massOne #sum of forces= ma
    return variables

def getVelocity(constants,variables):
    variables[0] += variables[2]*timeStep               #v = vi + at
    return variables


def getPosition(constants,variables):
    variables[1] += variables[0]*timeStep              #x = xi + vt
    variables[3] = variables[1] + sprPos                #recaclulate the distance to the spring
    return variables


count = 0
flag = 0
#while step < 100:
while variables[1] > -45:
#while not (.1 > abs(variables[0]) and count >= 20):
#while not variables[4]:
    #print(int((variables[3] + 1)*30) * ' ' , '*')
    variables = getAccel(constants,variables)
    variables = getVelocity(constants,variables)
    if variables[1] < 0 and variables[0] < 0:
        print(variables, step * timeStep)
        variables[0] = - (resConst * variables[0])
        print('boing!', variables[0])
        
    variables = getPosition(constants,variables)
    if abs(variables[0]) < .01:
        flag = (1 - flag)
        count += .5
        print(str(count) * flag ,str(variables[1]) * flag)
        if variables[1] < .05:
            break
    step += 1
if resConst != 0:
    variables = getAccel(constants,variables)
    variables = getVelocity(constants,variables)
    if variables[1] < 0:
        variables[0] = - (resConst * variables[0])
    variables = getPosition(constants,variables)
    step += 1
print(step*timeStep, ' Seconds')
print(variables)
