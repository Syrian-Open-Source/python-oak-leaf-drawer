import math
import matplotlib.pyplot as plt


# declare the functions a,b,c,d,e,f,g
def resolveA(teta):
    return 0.01 * (math.cos(teta) ** 9) * (math.cos(5.0 * teta) ** 10)


def resolveB(teta):
    return 0.25 * math.sin(2 * teta)


def resolveC(teta):
    return 1 - 0.5 * math.sin(10 * teta) ** 2


def resolveD(teta):
    return 1 - (math.cos(teta) * math.cos(3 * teta)) ** 8


def resolveE(teta):
    return math.sin(teta)


def resolveF(teta):
    return 0.2 * math.sin(10 * teta) ** 2


def resolveG(teta):
    return 0.5 + math.sin(2 * teta) ** 2



xRotatedList = []
yRotatedList = []
xList = []
yList = []

def OakLeafX(teta):
    return resolveA(teta) + (resolveB(teta) * resolveC(teta) * resolveD(teta))


def OakLeafY(teta):
    return resolveE(teta) * (1 - (resolveF(teta) * resolveG(teta)))


def generateOakLeaf():
    for i in range(1, 180):
        xList.append(OakLeafX(math.radians(i)))
    for i in range(1, 180):
        yList.append(OakLeafY(math.radians(i)))

    return xList, yList


def plot(xList, yList, title):
    plt.plot(xList, yList)
    plt.title(title)
    plt.show()


xList, yList = generateOakLeaf()
# plot(xList, yList, "One Oak Leaf")

xRotatedList = []
yRotatedList = []


def generateRotatedList(xList, yList, angle):
    for i in range(1, 180):
        xRotatedList.append((yList[i] * math.sin(math.radians(angle))) + (xList[i] * math.cos(math.radians(angle))))
        yRotatedList.append((yList[i] * math.cos(math.radians(angle))) - (xList[i] * math.sin(math.radians(angle))))

    return xRotatedList, yRotatedList

xRotatedList = []
yRotatedList = []


def generateOakLeafPattern(rotationAngle):
    xPatternList = []
    yPatternList = []

    xList, yList = generateOakLeaf()
    if rotationAngle <= 0:
        count = 1
    else:
        count = 360 / rotationAngle

    for j in range(0, math.ceil(count)):
        xPatternList += generateRotatedList(xList, yList, (rotationAngle * j))[0]
        yPatternList += generateRotatedList(xList, yList, (rotationAngle * j))[1]

    return xRotatedList, yRotatedList


def drawPattern(rotationAngle, text):
    plot(generateOakLeafPattern(rotationAngle)[0], generateOakLeafPattern(rotationAngle)[1], text)
