import math


class TaskDefinition:
    rows: int
    columns: int
    minimumIngr: int
    maxCells: int
class SliceDefinition:
    startRowIndex: int
    lastRowIndex: int
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
#print(f'{pizza}')

#dzialamy

numberOfSlices = 0
sliceToCut = SliceDefinition()
sliceToCut.startRowIndex = 0
sliceToCut.lastRowIndex = 0
sliceToCut.startColIndex = 0
sliceToCut.endColIndex = 0
slices = []

while (1):

#for rowIndex, rowValue in enumerate(pizza):
 #   print(f'{rowValue}')
    for columnIndex, columnValue in enumerate(rowValue):
  #      if (rowValue[columnIndex] < sliceToCut.IsComplete)
  ##          taskDefinition.minimumIngr