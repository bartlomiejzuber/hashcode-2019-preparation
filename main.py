import math
import numpy as np


class TaskDefinition:
    rows: int = 0
    columns: int = 0
    minimumIngr: int = 0
    maxCells: int = 0


class SliceDefinition:
    startRowIndex: int = 0
    endRowIndex: int = 0
    startColIndex: int = 0
    endColIndex: int = 0
    ready: bool = False
    rowExtended: bool = False

    def __init__(self, rowIndex, columnIndex):
        self.startRowIndex = rowIndex
        self.endRowIndex = rowIndex
        self.startColIndex = columnIndex
        self.endColIndex = columnIndex


def getFilesLines(filesNumber)-> []:
    filesDataLines = []
    statementsFolderPath = "C:\\HashCodeStatements\\"
    fileNames = [
        "a_example.in",
        "b_small.in",
        "c_medium.in",
        "d_big.in"
    ]
    for fileNumber in range(0, filesNumber):
        fileName = fileNames[fileNumber]
        with open(statementsFolderPath + fileName, 'r') as myfile:
            fileLines = myfile.readlines()
        filesDataLines.append(fileLines)
    return filesDataLines


def getTaskDefinitions(fileLines)-> TaskDefinition:
    taskDefinition = TaskDefinition()
    definitions = fileLines[0]
    fileLines.remove(fileLines[0])
    taskDefinitionData = definitions.split(" ")
    taskDefinition.rows = int(taskDefinitionData[0])
    taskDefinition.columns = int(taskDefinitionData[1])
    taskDefinition.minimumIngr = int(taskDefinitionData[2])
    taskDefinition.maxCells = int(taskDefinitionData[3])
    return taskDefinition


def prepareResults(slices, fileIndex):
    file = open(f'{fileIndex}_result.txt', "w")
    file.writelines(f'{slices.__len__()} \n')
    for sliceItem in slices:
        file.writelines("{} {} {} {}\n".format(sliceItem.startRowIndex,
                                               sliceItem.startColIndex, sliceItem.endRowIndex, sliceItem.endColIndex))
    file.close()


def canSliceExtend(slice: SliceDefinition, taskDefinition: TaskDefinition, rowIncr: int, colIncr: int)-> bool:
    result = True
    sliceRowsLength = slice.endRowIndex-slice.startRowIndex + rowIncr + 1
    sliceColsLength = slice.endColIndex-slice.startColIndex + colIncr + 1
    if(sliceRowsLength > taskDefinition.rows):
        result = False
    if(sliceColsLength > taskDefinition.columns):
        result = False
    if(sliceRowsLength * sliceColsLength > taskDefinition.maxCells):
        result = False
    return result

def cutSlice(pizza: np.array, rowIndex, columnIndex, slices, taskDefinition):
    sliceToCut = SliceDefinition(rowIndex, columnIndex)
    i = 0
    mushroomsCount = 0
    tomatosCount = 0
    while (1):
        i = i + 1
        tempSlice = npPizza[sliceToCut.startRowIndex:(
            sliceToCut.endRowIndex+1), sliceToCut.startColIndex:(sliceToCut.endColIndex+1)]
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
            if (canSliceExtend(sliceToCut,taskDefinition, 1,0)):
                sliceToCut.endRowIndex += 1
       #         sliceToCut.rowExtended = True
            elif(canSliceExtend(sliceToCut,taskDefinition, 0,1)):
                    sliceToCut.endColIndex += 1
            else:
                break
          #      sliceToCut.rowExtended = False
    if(sliceToCut.ready==True):
        slices.append(sliceToCut)


fileDataLines = getFilesLines(4)
for fileIndex, fileLines in enumerate(fileDataLines):
    print(f'File Index: {fileIndex}')
    taskDefinition = getTaskDefinitions(fileLines)
    pizza = []
    for line in fileLines:
        pizzaLine = [x.strip() for x in line.replace('\n', '')]
        pizza.append(pizzaLine)
    npPizza = np.array(pizza)
    slices = []
    for rowIndex, rowValue in enumerate(npPizza):
        for columnIndex, ing in enumerate(rowValue):
            if(ing != 'X'):
                cutSlice(npPizza, rowIndex, columnIndex, slices, taskDefinition)
    print(f'{npPizza}')
    prepareResults(slices, fileIndex)
