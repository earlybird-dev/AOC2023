import re

f = open("input.txt", "r")

# Combine all lines together, add "." around each line to avoid out of range errors
all = ""
for line in f:
  cleanLine = line.replace("\n", "")
  lineLen = len(cleanLine)+2
  all += "." + cleanLine + (".")
all = "."*lineLen + all + "."*lineLen

digitPositionDict = {i: c for i, c in enumerate(all) if c.isdigit()}
digitPositions = list(digitPositionDict.keys())
digitPositions.append(len(all)) # To avoid missing the last number

posGroups = []
posGroup = []
for (i, pos) in enumerate(digitPositions):
  if len(posGroup) == 0:
    posGroup.append(pos)
  try:
    nextPos = digitPositions[i+1]
    if (pos + 1) == nextPos:
      posGroup.append(pos)  
      posGroup.append(nextPos)  
      continue
    else:
      posGroups.append(sorted(list(set(posGroup))))
      posGroup = []
  except:
    break

validPosGroups = []

for posGroup in posGroups:
  valid = False
  for pos in posGroup:
    [topChar, bottomChar, leftChar, rightChar] = [pos - lineLen, pos + lineLen, pos - 1, pos + 1]
    adjacentChars = all[topChar] + all[topChar+1] + all[topChar-1] + all[bottomChar] +  all[bottomChar+1] +  all[bottomChar-1] + all[leftChar] + all[rightChar]
    if re.findall("[^0-9.]", adjacentChars):
      valid = True
  if valid == True:
    validPosGroups.append(posGroup)

validPositions = [num for posGroup in validPosGroups for num in posGroup]
validPositions = sorted(validPositions)

newCombinedLine = [digitPositionDict[i] if i in validPositions else " " for i in range(0, len(all))]
numberList = ''.join(newCombinedLine).split(" ")
result = sum([int(num) for num in numberList if num != ''])
print(result)