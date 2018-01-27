
massOne = 165
massTwo = 125
gravParam = 6.67408*(10**(-11))
timeStep = 100003
step = 0

constants = (massOne,massTwo,gravParam,timeStep)

velOne = 0
velTwo = 0
posOne = 0
posTwo = 15
accOne = 0
accTwo = 0
dist = posTwo-posOne

variables = [velOne,velTwo,posOne,posTwo,accOne,accTwo,dist]

def getAccel(constants,variables):
    variables[4] = massTwo*gravParam/((posOne-posTwo)*(posOne-posTwo))
    variables[5] = -massOne*gravParam/((posOne-posTwo)*(posOne-posTwo))
    print(timeStep)
#    print(variables[4])
#    print(variables[5])
    return variables

def getVelocity(constants,variables):
    variables[0] += variables[4]*timeStep
    variables[1] += variables[5]*timeStep
#    print(variables[0])
#    print(variables[1])
    return variables


def getPosition(constants,variables):
    variables[2] += variables[0]*timeStep
    variables[3] += variables[1]*timeStep
    variables[6] = variables[3]-variables[2]
    #print(variables[6])
    return variables


print(variables)
while variables[6] > 0:
    variables = getAccel(constants,variables)
    variables = getVelocity(constants,variables)
    variables = getPosition(constants,variables)
    step += 1
print(step*timeStep)
print(step*timeStep/3600, " hours")
print(step*timeStep/3600/24, " days")
print(variables)
