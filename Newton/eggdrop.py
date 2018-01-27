#egg dropper
#uses a riemann sum approxamation to calculate kinematics
#under forces of weight, springs, friction, and drag

#the system being modeled is an egg drop using a parachute to slow down initially
#with some legs absorbing the impact
#coefficient of drag was determined experimentally

from math import sin, cos, radians, pi

'''initial condition'''
massOne = .168
timeStep = .001
step = 0
sprPos = .1
sprConst = 30
angle = 90 #angle off horizontal
fricCoeff = 0
area = .4 * .4 * 2
dragCoeff = .6 
airDens = 1.3

constants = (massOne,timeStep,fricCoeff,angle,sprConst, area, dragCoeff, airDens)

#initial values
posOne = 11.4
velOne = -.01 #slight negative to prevent early termination of loop
maxA = 0

variables = [velOne,posOne,0,posOne - sprPos,maxA]

def getAccel(constants,variables,t):
    #forces, in the direction of motion
    forceG = -massOne * 9.81 * sin(radians(angle))#force of gravity
    
    if variables[3] <= 0: forceS = - sprConst * variables[3]    #force of the spring
    else: forceS = 0
    
    forceF = - fricCoeff * massOne * 9.81 * cos(radians(angle)) #force of friction
    if variables[0] <= 0:
        forceF *= -1
        
    d = dragCoeff
    if t*timeStep < .25:
        d *= .5 #parachute deploys gradually
        
    forceD = -.5 * d * airDens * area * variables[0] * abs(variables[0])

    variables[2] = (forceG + forceF + forceS + forceD) / massOne #sum of forces= ma
    if variables[4] < variables[2]: variables[4] = variables[2] 
    return variables

def getVelocity(constants,variables):
    variables[0] += variables[2]*timeStep               #v = vi + at
    return variables

def getPosition(constants,variables):
    variables[1] += variables[0]*timeStep              #x = xi + vt
    variables[3] = variables[1] - sprPos               #recaclulate the distance to the spring
    return variables


while variables[0] < 0 and variables[1] > 0:
    #continue so long as it is moving downwards and is above the ground
    variables = getAccel(constants,variables,step)
    variables = getVelocity(constants,variables)        
    variables = getPosition(constants,variables)
    step += 1

#print the end condition
print(step*timeStep, ' Seconds')
print(variables[0:2],variables[4])
