bag = {'red': 12, 'green': 13, 'blue': 14}
validCombinations = []
for colour in bag.keys():
  numberOfColour = bag[colour]
  for i in range(1, numberOfColour+1):
    combination = str(i) + " " +  colour
    validCombinations.append(combination)

sumOfId = 0
sumOfPower = 0

f = open("input.txt", "r")
for game in f:
  [gameID, picks] = game.split(":")
  id = gameID.split(" ")[1]
  picks = picks.replace(";", ",").replace("\n", "").split(",")

  # Part 1
  pickSet = set([item.strip() for item in picks])
  if pickSet.issubset(validCombinations):
    sumOfId += int(id)

  # Part 2
  powerOfGame = 1
  for colour in bag.keys():
    maxNumberOfColour = max([int(item.strip().split(" ")[0]) for item in picks if colour in item])
    powerOfGame *= maxNumberOfColour
  sumOfPower += powerOfGame

print(sumOfId)
print(sumOfPower)