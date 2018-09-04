import os

def displayOptions():
    print("Choose what you'd like to do:\n\tP: Play Level\n\tC: Create Level\n\tQ: Quit\n")
    selection = getValidInput('Choose P/C/Q: ', ['P', 'p', 'C', 'c', 'Q', 'q'])
    if selection in 'Pp':
        levelSelect()
    elif selection in "Cc":
        createLevel()
    elif selection in 'Qq':
        return False
    return True

def createLevel():
    print('Creating new level...\n')
    variables, story = getMadLib()
    name = getViableName()
    levelFile = open('Levels/' + name + '.txt', 'w')
    levelFile.write(variables + '\n' + story)
    levelFile.close()

def getViableName():
    name = input('What do you want to call this MadLib? ')
    if name not in [level[:-4] for level in os.listdir('Levels')]:
        return name
    else:
        print('The name you have chosen for your level is already in use by a different level.')
    return getViableName()

def playLevel(levelName):
    levelFile = open('./Levels/' + levelName + '.txt', 'r')
    variables = levelFile.readline()[:-1].split(' ')
    story = levelFile.readline()
    if getValidInput('Do you want to see the story before filling it in? (y/n) ', ['Y', 'y', 'N', 'n']) in 'Yy':
        print(colorify(story, variables))
    print('\nCompleted MadLib:\n' + fillOutMadLib(story, variables) + '\n')

def levelSelect():
    if not os.path.isdir('Levels'):
        os.mkdir('Levels')
    options = [level[:-4] for level in os.listdir('Levels')]
    if len(options) > 0:
        optionsString = "Levels:\n"
        for index, level in enumerate(options):
            optionsString += '\t' + str(index + 1) + '. ' + level + '\n'
        print(optionsString)
        chosenLevel = getValidInput("Enter the level name you'd like to play: ", options)
        playLevel(chosenLevel)
    else:
        print('There are no levels to play yet.')
        if getValidInput('Want to create one? (y/n): ', ['Y', 'y', 'N', 'n']) in 'Yy':
            createLevel()

def getMadLib():
    keepAsking = True
    while keepAsking:
        variables = input('Enter the variable names required for this level separated by spaces: ')
        story = input("Enter your story separated by spaces, enter " + variables + " for places that require user input: ")
        print('Your MadLib:', colorify(story, variables.split(' ')))
        if getValidInput('Save? (y/n): ', ['Y', 'y', 'N', 'n']) in 'Yy':
            keepAsking = False
    return variables, story
    
def fillOutMadLib(story, variables):
    newWords = []
    variables += [v + '.' for v in variables]
    for word in story.split(" "):
        newWord = word
        if word in variables:
            if word[-1] == ".":
                newWord = input("Enter a " + word[:-1] + ": ") + '.'
            else:
                newWord = input('Enter a ' + word + ': ')
        newWords.append(newWord)
    return " ".join(newWords)

def getValidInput(prompt, validResponses):
    response = input(prompt)
    if response not in validResponses:
        print('That is an invalid response.\n')
        return getValidInput(prompt, validResponses)
    return response

def colorify(wordString, specials):
    newWords = []
    for word in wordString.split(' '):
        newWord = word
        withPeriod = word[-1] == '.'
        if withPeriod: word = word[:-1]
        if word in specials:
            newWord = '\033[0;36;40m' + word + '\033[0m'
        if withPeriod: newWord += '.'
        newWords.append(newWord)
    return " ".join(newWords)

def main():
    print('--- Mad Libs ---\n')
    keepGoing = displayOptions()
    while keepGoing:
        keepGoing = displayOptions()
    print('\nThanks for playing!!!!')
    
main()