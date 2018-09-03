print("Starting new MadLibs game...\n")
variables = input("Enter the variable names you're going to use in this madlib separated by spaces. ('noun adjective verb' ... etc): ").split(' ')
varString = " ".join(["'" + v + "'" for v in variables])
print("Enter your story separated by spaces, enter", varString, "for places that require user input.")
story = input("Your story: ")
newWords = []
variables += [v + '.' for v in variables]

for word in story.split(" "):
    if word in variables:
        if word[-1] == ".": word = word[:-1]
        newWords.append(input("Enter a " + word + ": "))
    else:
        newWords.append(word)
        
print(" ".join(newWords))