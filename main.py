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


def canSliceExtend(
        slice: SliceDefinition,
        taskDefinition: TaskDefinition,
        rowIncr: int,
        colIncr: int,
        pizza: np.array = None)-> bool:
    sliceRowsLength = slice.endRowIndex-slice.startRowIndex + rowIncr + 1
    sliceColsLength = slice.endColIndex-slice.startColIndex + colIncr + 1
    if(slice.endRowIndex + 1 + rowIncr > taskDefinition.rows):
        return False
    if(slice.endColIndex + 1 + colIncr > taskDefinition.columns):
        return False
    if(sliceRowsLength * sliceColsLength > taskDefinition.maxCells):
        return False
    if(pizza is not None):
        startRowIndexForExtendCheck =slice.startRowIndex
        startColIndexForExtendCheck =slice.startColIndex
        if(rowIncr> 0):
            startRowIndexForExtendCheck = slice.endRowIndex+rowIncr
        if(colIncr> 0):
            startColIndexForExtendCheck = slice.endColIndex+colIncr
        for rowIndex in range(startRowIndexForExtendCheck,  slice.endRowIndex+rowIncr+1):
            for columnIndex in range(startColIndexForExtendCheck,slice.endColIndex+colIncr+1):
                if (npPizza[rowIndex, columnIndex] == 'X'):
                     return False
    return True


def cutSlice(pizza: np.array, rowIndex, columnIndex, slices, taskDefinition):
    sliceToCut = SliceDefinition(rowIndex, columnIndex)
    i = 0
    tempPizza = np.copy(pizza)
    mushroomsCount = 0
    tomatosCount = 0
    while (1):
        i = i + 1
        tempSlice = tempPizza[sliceToCut.startRowIndex:(
            sliceToCut.endRowIndex+1), sliceToCut.startColIndex:(sliceToCut.endColIndex+1)]
        for rowIndex, rowValue in enumerate(tempSlice):
            for columnIndex, ing in enumerate(rowValue):
                if (ing == 'T'):
                    tomatosCount += 1
                if (ing == 'M'):
                    mushroomsCount += 1
                tempPizza[rowIndex + sliceToCut.startRowIndex][columnIndex +
                                                               sliceToCut.startColIndex] = "X"
        if (mushroomsCount >= taskDefinition.minimumIngr and tomatosCount >= taskDefinition.minimumIngr):
            sliceToCut.ready = True
            break
        if (sliceToCut.ready == False):
            if (canSliceExtend(sliceToCut, taskDefinition, 1, 0,tempPizza)):
                sliceToCut.endRowIndex += 1
            elif(canSliceExtend(sliceToCut, taskDefinition, 0, 1, tempPizza)):
                sliceToCut.endColIndex += 1
            else:
                break
    if(sliceToCut.ready == True):
        slices.append(sliceToCut)
        return tempPizza
    return pizza


def tryExtendSlices(slices, npPizza: np.array):
    for slice in slices:
        while(1):
            if (canSliceExtend(slice, taskDefinition, 1, 0, npPizza)):
                slice.endRowIndex += 1
            elif(canSliceExtend(slice, taskDefinition, 0, 1, npPizza)):
                slice.endColIndex += 1
            else:
                for rowIndex in range(slice.startRowIndex, slice.endRowIndex + 1):
                    for columnIndex in range(slice.startColIndex, slice.endColIndex + 1):
                        npPizza[rowIndex, columnIndex] = 'X'
                break


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
    for rowIndex in range(0, taskDefinition.rows):
        for columnIndex in range(0, taskDefinition.columns):
            if(npPizza[rowIndex, columnIndex] != 'X'):
                npPizza = cutSlice(npPizza, rowIndex, columnIndex,
                                   slices, taskDefinition)
    print(f'{npPizza}')
    tryExtendSlices(slices, npPizza)
    print(f'{npPizza}')
    prepareResults(slices, fileIndex)
