bag = {'red': 12, 'green': 13, 'blue': 14}
validCombinations = []
for colour in bag.keys():
  numberOfColour = bag[colour]
  for i in range(1, numberOfColour+1):
    combination = str(i) + " " +  colour
    validCombinations.append(combination)
result = 0
f = open("input.txt", "r")
for game in f:
  [gameID, picks ]= game.split(":")
  id = gameID.split(" ")[1]
  picks = picks.replace(";", ",").replace("\n", "").split(",")
  pickSet = set([item.strip() for item in picks])
  if pickSet.issubset(validCombinations):
    result += int(id)
print(result)