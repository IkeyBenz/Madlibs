from random import randint
nums = ["this is pos 1","this is pos 2","this is pos 3","this is pos 4","this is pos 5","this is pos 6","this is pos 7","this is pos 8","this is pos 9","this is pos 10"]
helperList = []
scrambled = []
backToNormal = []

while len(nums) > 0:
    rand = randint(0, len(nums)-1)
    helperList.append(rand)
    scrambled.append(nums.pop(rand))


print(scrambled)
print(helperList)