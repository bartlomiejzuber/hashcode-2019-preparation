import math
import numpy as np


class TaskDefinition:
    rows: int
    columns: int
    minimumIngr: int
    maxCells: int


class SliceDefinition:
    startRowIndex: int
    endRowIndex: int
    startColIndex: int
    endColIndex: int
    ready: bool
    rowExtended: bool


def getTaskDefinitions(fileLines):
    taskDefinition = TaskDefinition()
    definitions = fileLines[0]
    fileLines.remove(fileLines[0])
    taskDefinitionData = definitions.split(" ")
    taskDefinition.rows = int(taskDefinitionData[0])
    taskDefinition.columns = int(taskDefinitionData[1])
    taskDefinition.minimumIngr = int(taskDefinitionData[2])
    taskDefinition.maxCells = int(taskDefinitionData[3])
    return taskDefinition


statementsFolderPath = "C:\\HashCodeStatements\\"
fileNames = [
    "a_example.in",
    "b_small.in",
    "c_medium.in",
    "d_big.in"
]
for fileNumber in range(0, 4):
    fileName = fileNames[fileNumber]
    print(f'{fileName}')
    with open(statementsFolderPath + fileName, 'r') as myfile:
        fileLines = myfile.readlines()
    taskDefinition = getTaskDefinitions(fileLines)
    pizza = []
    for line in fileLines:
        pizzaLine = [x.strip() for x in line.replace('\n', '')]
        pizza.append(pizzaLine)

    npPizza = np.array(pizza)
    numberOfSlices = 0
    slices = []
    while (1):
        sliceToCut = SliceDefinition()
        sliceToCut.startRowIndex = 0
        sliceToCut.endRowIndex = 0
        sliceToCut.startColIndex = 0
        sliceToCut.endColIndex = 0
        sliceToCut.ready = False
        sliceToCut.rowExtended = False
        i = 0
        mushroomsCount = 0
        tomatosCount = 0
        while (1):
            i = i + 1
            tempSlice = npPizza[sliceToCut.startRowIndex:(
                sliceToCut.endRowIndex+1), sliceToCut.startColIndex:(sliceToCut.endColIndex+1)]
            print(f'{tempSlice}')
            for rowIndex, rowValue in enumerate(tempSlice):
                for columnIndex, ing in enumerate(rowValue):
                    if (ing == 'T'):
                        tomatosCount += 1
                    if (ing == 'M'):
                        mushroomsCount += 1
                    npPizza[rowIndex + sliceToCut.startRowIndex][columnIndex +
                                                                 sliceToCut.startColIndex] = "X"
            if (mushroomsCount >= taskDefinition.minimumIngr and tomatosCount >= taskDefinition.minimumIngr):
                sliceToCut.ready = True
                break
            if (sliceToCut.ready == False):
                if (sliceToCut.rowExtended == False):
                    sliceToCut.endRowIndex += 1
                    sliceToCut.rowExtended = True
                else:
                    sliceToCut.endColIndex += 1
                    sliceToCut.rowExtended = False
            print(f'{sliceToCut.endRowIndex}')
            print(f'{sliceToCut.endColIndex}')
        slices.append(sliceToCut)
        numberOfSlices += 1
        break
    file = open("{}_result.txt".format(fileName.split(".")[0]), "w")
    file.writelines("{} \n".format(numberOfSlices))
    for sliceItem in slices:
        file.writelines("{} {} {} {}\n".format(sliceItem.startRowIndex,
                                               sliceItem.startColIndex, sliceItem.endRowIndex, sliceItem.endColIndex))
    file.close()
