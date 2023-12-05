import re

f = open("input.txt", "r")
res = 0

for line in f:
  allNumbers = line.split(":")[1].replace("|", "").split()
  winningNumbers = len(allNumbers)-len(set(allNumbers))
  if winningNumbers > 0:
    res += 2**(max(0, winningNumbers-1))      
print(res)