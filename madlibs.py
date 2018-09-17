from coolprinter import tprint
import colors as c
import os

def displayOptions():
    tprint(c.blue + "Choose what you'd like to do:" + c.yellow + "\n\tP: Play Level\n\tC: Create Level\n\tQ: Quit\n" + c.end)
    selection = getValidInput('Choose P/C/Q: ', ['P', 'p', 'C', 'c', 'Q', 'q'])
    if selection in 'Pp':
        levelSelect()
    elif selection in "Cc":
        createLevel()
    elif selection in 'Qq':
        return False
    return True

def createLevel():
    tprint(c.magenta + 'Creating new level...\n')
    variables, story = getMadLib()
    if story: 
        name = getViableName()
        levelFile = open('Levels/' + name + '.txt', 'w')
        levelFile.write(variables + '\n' + story)
        levelFile.close()

def getViableName():
    name = input(c.blue + 'What do you want to call this MadLib? ' + c.yellow)
    if name not in [level[:-4] for level in os.listdir('Levels')]:
        tprint(c.magenta + 'Saving '+ name + '...\n')
        return name
    else:
        tprint(c.red + 'The name you have chosen for your level is already in use by a different level.')
    return getViableName()

def playLevel(levelName):
    levelFile = open('./Levels/' + levelName + '.txt', 'r')
    variables = levelFile.readline()[:-1].split(' ')
    story = levelFile.readline()
    if getValidInput('Do you want to see the story before filling it in? (y/n) ', ['Y', 'y', 'N', 'n']) in 'Yy':
        tprint('\n' + c.blue + levelName + ':\n   ' + c.gray + colorify(story, variables) + '\n')
    tprint(c.blue + '\nCompleted MadLib:   \n' + fillOutMadLib(story, variables) + '\n')

def levelSelect():
    tprint(c.magenta + 'Loading Saved Levels...\n')
    options = [level[:-4] for level in os.listdir('Levels')]
    if len(options) > 0:
        tprint(c.blue + 'Levels:\n' + c.yellow + ''.join(['\t' + str(index + 1) + '. ' + level + '\n' for index, level in enumerate(options)]))
        chosenLevel = getValidInput("Enter the level name you'd like to play: ", options)
        playLevel(chosenLevel)
    else:
        tprint(c.red + 'There are no levels to play yet.\n')
        if getValidInput('Want to create one? (y/n): ', ['Y', 'y', 'N', 'n']) in 'Yy':
            createLevel()

def getMadLib():
    variables = input(c.blue + 'Enter the variable names required for this level separated by spaces (noun adjective verb): ' + c.yellow)
    story = input(c.blue + "Enter your story separated by spaces, enter " + c.cyan + variables + c.blue + " for places that require user input: " + c.gray)
    tprint(c.blue + 'Your MadLib: ' + colorify(story, variables.split(' ')) + '\n')
    if getValidInput('Save? (y/n): ', ['Y', 'y', 'N', 'n']) in 'Nn':
        return False, False
    return variables, story
    
def fillOutMadLib(story, variables):
    newWords = []
    variables += [v + '.' for v in variables]
    for word in story.split(" "):
        newWord = word
        if word in variables:
            if word[-1] == ".":
                newWord = input(c.blue + "Enter a " + c.cyan + word[:-1] + c.blue + ": " + c.yellow) + '.'
            else:
                newWord = input(c.blue + 'Enter a ' + c.cyan + word + c.blue + ": " + c.yellow)
        newWords.append(newWord)
    return c.gray + " ".join(newWords)

def getValidInput(prompt, validResponses):
    response = input(c.blue + prompt + c.yellow)
    if response not in validResponses:
        tprint(c.red + 'That is an invalid response.' + c.end + '\n')
        return getValidInput(prompt, validResponses)
    return response

def colorify(wordString, specials):
    newWords = [c.gray]
    for word in wordString.split(' '):
        newWord = word
        withPeriod = word[-1] == '.'
        if withPeriod: word = word[:-1]
        if word in specials:
            newWord = c.cyan + word + c.gray
        if withPeriod: newWord += '.'
        newWords.append(newWord)
    return " ".join(newWords)

def main():
    tprint(c.blue + '--- Mad Libs ---\n')
    if not os.path.isdir('Levels'):
        os.mkdir('Levels')
    keepGoing = displayOptions()
    while keepGoing:
        keepGoing = displayOptions()
    tprint(c.magenta + '\nThanks for playing!!!!\n' + c.end)
    
main()

list = [[1,2,3], 3, 4, 5]
