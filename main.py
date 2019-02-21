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


statementsFolderPath = "C:\HashCodeStatements\\"
fileNames = [
    "a_example.in",
    "b_small.in",
    "c_medium.in",
    "d_big.in"
]
with open(statementsFolderPath + fileNames[0], 'r') as myfile:
    #data = myfile.read()
    fileLines = myfile.readlines()
taskDefinition = getTaskDefinitions(fileLines)
print(f'{taskDefinition.columns}')
print(f'{len(fileLines)}')

pizza = []
for line in fileLines:
    pizzaLine = [x.strip() for x in line.replace('\n', '')]
    pizza.append(pizzaLine)
# print(f'{pizza}')

# dzialamy
npPizza = np.array(pizza)
numberOfSlices = 0
sliceToCut = SliceDefinition()
sliceToCut.startRowIndex = 0
sliceToCut.endRowIndex = 0
sliceToCut.startColIndex = 0
sliceToCut.endColIndex = 0
slices = []

while (1):
    mushroomsCount = 0
    tomatosCount =0
       tempSlice = npPizza[sliceToCut.startRowIndex:(
        sliceToCut.endRowIndex+1), sliceToCut.startColIndex:(sliceToCut.endColIndex+1)]
    for rowIndex, rowValue in enumerate(tempSlice):
        for columnIndex, ing in enumerate(rowValue):
            if (ing == 'T')
                tomatosCount += 1
            if (ing == 'M')
                mushroomsCount += 1
            
    break

