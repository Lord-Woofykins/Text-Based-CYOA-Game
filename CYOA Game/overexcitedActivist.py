import os
import time
import random
from storyText import scenes

# Clear the terminal 
os.system("clear")

# ANSI Colour Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
END = "\033[0m"

# Item types
# These are the types of items that can be used in the game
itemTypes = {
    "weapon": ["screwdriver"],
    "money": ["wallet", "briefcase"],
    "food": ["apple", "sandwich"],
}

# Scene-specific stats
stealth = 3
nuclearVolatility = 0
foodBonus = 25
attack = 12
countrysideEnding = False

# General player stats
inventory = ["apple"]
playerHealth = 100

# Keybinds
inventoryBind = "z"
playerHealthBind = "x"
saveGameBind = "s"

# Backend variables
writeDelay = 0.01
spaceDelayMultiplier = 1.1
writePreset = "medium-fast"

#Customisability of the game to the user
writeSpeedPresets = {
    "slow": 0.05,
    "medium": 0.025,
    "medium-fast": 0.01,
    "fast": 0.005
}


#Starting scene
scene = "scene5B-2"


# Print statements below this point
print(os.getcwd())

# Functions below this point

# Handle the Speech Contest Challenge
def challengeSpeechContest():
    global scene

    # This block of print statements introduces your actions
    messagePrinter("Threadit            r/Politics")
    username = inputHandler("Choose your username: ")
    print()
    messagePrinter("Threadit            r/Politics")
    messagePrinter(f"u/{username}: I hate cheese! #CheeseIsBad")
    messagePrinter("| 1. Upvote (21) | 2. Downvote (7) | 3. Comments (4) |")
    print()

    # This block of print statements introduces opposition actions
    messagePrinter("Comments:")
    messagePrinter("1. I agree, cheese is the worst!")
    messagePrinter("2. I'm chonky and like cheese, but I respect your opinion.")
    messagePrinter("3. u/CheeseVigilante42: Oh. Oh, you hate cheese? You just wake up in the morning and decide to be objectively wrong? CHEESE IS THE BACKBONE OF SOCIETY. You think you’re better than the entirety of France? THAN THE GRANDMA IN ITALY HANDMAKING MOZZARELLA RIGHT NOW? I bet your fridge is just air and despair. #CheeseIsLife")

    # This is an optional tangent of print statements, unrelated to storyline
    messagePrinter("1 reply:")
    response = inputHandler("Open? (y/n) ")
    if response == "y":
        messagePrinter("u/Chonky: I hope you choke on a cracker. I hope you get a paper cut on your tongue. I hope you step on a lego. I hope you get a splinter under your fingernail. I hope you get a popcorn kernel stuck in the back of your throat. I hope you get a blister. I hope you get a pimple in your ear. I hope you get a mosquito bite on your eyelid. I hope you get a sunburn on your scalp. I hope you get a cramp in your foot. I hope you get a headache. I hope you get a stomach ache. I hope you get a toothache. I hope you get a brain freeze.")
    print()
    
    # Requesting response from user
    messagePrinter("Speech Contest!" + "\n" + "Write the best (angriest) speech possible!")
    print()
    speech = input("Speech: ")

    # Calculating the score derived from the response
    speechScore = 0
    # Scoring added for length
    if len(speech) > 150:
        speechScore += 2
    elif len(speech) > 60:
        speechScore += 2
    elif len(speech) >= 20:
        speechScore += 1
    # Scoring added for keywords
    keywords = ["cheese", "hate", "anger", "rage", "disgust", "pooky", "france", "italy", "mozzarella", "grandma", "backbone", "society", "wrong", "despair", "life", "vigilante", ]
    for keyword in keywords:
        if keyword in speech.lower():
            speechScore += 1
    # Scoring added for punctuation
    speechScore += speech.count("!") + speech.count("?") + speech.count(".") + speech.count(",") #Scoring added for punctuation
    
    # Checking if the user fails, and gives hints
    if speechScore < 4: # Speech score of 5 to pass means at least a decent length of speech and medium difficulty based on playtesting
        messagePrinter("u/CheeseVigilante42: And THERE IT IS, folks! He crumbles.")
        if len(speech) < 10:
            messagePrinter("u/CheeseVigilante42: Imagine not even bothering to write a proper length comeback.")
        elif "cheese" not in speech.lower():
            messagePrinter("u/CheeseVigilante42: Didn't even mention cheese.")
        elif speech.count("!") == 0:
            messagePrinter("u/CheeseVigilante42: No exclamation points? No ALL CAPS? No insults? You call that a speech?")
        elif speech.count("?") == 0:
            messagePrinter("u/CheeseVigilante42: No rhetorical questions? No insults? You call that a speech?")
        elif len(speech.split()) < 30:
            messagePrinter("u/CheeseVigilante42: Could've spent more time on that one instead of rage quitting.")
        print()
        messagePrinter("You have lost the speech contest. Words hurt.")
        # Requesting whether to try again
        response = inputHandler("Try again? (y/n) ")
        while response != "y" and response != "n":
            response = inputHandler("Try again? (y/n) ")
        if response == "n":
            scene = "end"
        else:
            challengeSpeechContest()
    # Win message
    else:
        messagePrinter("u/CheeseVigilante42: FINE, I'LL ADDRESS THE ELEPHANT IN THE ROOM" + "\n" + "I'm the VICTIM here. Do you know how many alt accounts I've been banned from? SEVENTEEN. All because I dared to speak the TRUTH about cheese. MY LAWYER WILL BE IN TOUCH. *Proceeds to dramatically delete reddit account*")
        if speechScore > 8:
            messagePrinter("The mods of the thread have given you money to help you out of the debt that you must be because of the job that you must've lost in sacrifice of the time taken to write that speech.")
        inputHandler("")
        scene = "scene3A"
        displayScene(scenes[scene])

# This is the function where the fight scene plays out
# In the fight, there are two main stats to keep track of: the status of the opposition and their health, these deeply effect the outcomes and available options
def challengeFight(attack):
    global scene, playerHealth
    oppHealth = 80
    oppAttack = 12
    ignored = False # Keeps track of whether the user has used the ignore trick
    messagePrinter("In the background, a chant can be heard: 'Hit him', 'Hit him', 'Hit him'!")
    messagePrinter("The challenger snarles at you, and spits on the ground.")
    print()
    fightStatus = 'alert'
    while fightStatus != 'dead' and oppHealth > 0 and playerHealth > 0: #Checking if the player or opponent has died
        messagePrinter(f"challenger Stats: Health: {oppHealth} | Attack: {oppAttack} | Status: {fightStatus}")
        messagePrinter("Options: (1) Attack | (2) Bribe | (3) Use Item | (4) Flee | (5) Ignore")
        print()
        messagePrinter(f"Remember: Press [{inventoryBind}] to see your inventory and [{playerHealthBind}] to see your health!")

        response = integerResponseGenerator() # Asking for user input
        
        # The player's turn

        # Determining outcome for attack option
        if response == 1:
            # Roll a 50/50 and deduct health from opponent if successful
            if fightStatus == 'stunned':
                if random.randint(0, 1) == 0:
                    messagePrinter("Your hit strikes them, but the challenger manages to stagger to his feet.", GREEN)
                    oppHealth -= attack
                    fightStatus = 'angry'
                # 50/50 chance fail
                else:
                    messagePrinter("You miss.")
                    fightStatus = 'alert'
            # Checks for angry state, and causes loss of health
            elif fightStatus == 'angry':
                messagePrinter("You attempt to strike the challenger, but they block your punch and counter.", RED)
                playerHealth -= attack
                fightStatus = 'alert'
            # Default state causes a 1/4 roll
            else:
                roll = random.randint(0, 3)
                if roll == 0: # Stun + hit
                    messagePrinter("You hit the challenger, and they fall to the ground.", GREEN)
                    oppHealth -= attack
                    fightStatus = 'stunned'
                elif roll in [1, 2]: # Hit + angry
                    messagePrinter('You land a successful strike on them!', GREEN)
                    oppHealth -= attack
                    fightStatus = 'angry'
                else: # Fail + angry status
                    messagePrinter("You attempt to hit the challenger, but they manage to dodge just in time.", RED)
                    fightStatus = 'angry'
        
        # Determining outcome for bribe option
        elif response == 2:
            if len(inventory) > 0:
                messagePrinter("What do you bribe with?")

                # Displaying inventory with options
                i = 1
                for item in inventory:
                    messagePrinter(f"({i}) {item.upper()}")
                    i += 1
                
                # Requesting a valid integer response
                response = integerResponseGenerator()
                while response not in range(1, len(inventory) + 1):
                    messagePrinter("Please enter a valid option.")
                    response = integerResponseGenerator()

                item = inventory[response - 1] # Getting the item from the inventory
                # Checking the bribe type, and determining the response from the opponent
                if item in itemTypes["money"]: # Money initiates the greed response from the opponent, causing them to run away and for the fight to end
                    messagePrinter("You bribe the challenger with money, and they run away.", GREEN)
                    inventory.remove(item)
                    fightStatus = 'dead'
                elif item in itemTypes["weapon"]: # Weaponry angers the opponent
                    messagePrinter(f"You take out the {item.lower()}, but for some reason the sight of it only makes them angrier. They knock it out of your hand before you can formally offer it.", RED)
                    inventory.remove(item)
                    fightStatus = 'angry'
                elif item in itemTypes["food"]: # The opponent is likely homeless and starving, so offering food stuns them since they didn't expect such kindness
                    messagePrinter(f"You offer the {item.lower()} to the challenger. They seem confused but take it anyway.", GREEN)
                    inventory.remove(item)
                    fightStatus = 'stunned'
            else: # The player is encouraged to keep track of their stats, because choosing something that they are unable to do negatively impacts them
                messagePrinter("You don't have anything!")
                fightStatus = 'alert'
                continue
        
        # Item use function is largely the same, other than different effects and text
        elif response == 3:
            if len(inventory) > 0:
                messagePrinter("What do you use?")

                # Displaying inventory with options
                i = 1
                for item in inventory:
                    messagePrinter(f"({i}) {item.upper()}")
                    i += 1
                
                # Requesting a valid integer response
                response = integerResponseGenerator()
                while response not in range(1, len(inventory) + 1):
                    messagePrinter("Please enter a valid option.")
                    response = integerResponseGenerator()

                item = inventory[response - 1] # Getting the item from the inventory
                # Checking the item type, and determining the buff/response
                if item in itemTypes["money"]: # Increase of player health and angry status for money
                    messagePrinter("Showing the challenger how rich you are only angers them, but it does improve your ego.", YELLOW)
                    inventory.remove(item)
                    fightStatus = 'angry'
                    playerHealth += 10
                elif item in itemTypes["weapon"]: # Attack increase for weapon use
                    messagePrinter(f"Your {item.lower()} instills fear into the challenger, and your attack is buffed.", GREEN)
                    inventory.remove(item)
                    fightStatus = 'stunned'
                    attack += 8
                elif item in itemTypes["food"]: # Increase in health and reset of fightstatus for food
                    messagePrinter(f"You eat the {item.lower()} and gain {foodBonus} health.", GREEN)
                    inventory.remove(item)
                    playerHealth += foodBonus
                    fightStatus = 'alert'
            
            else: # Resetting the status of opposition in response to invalid option
                messagePrinter("You don't have anything!", YELLOW)
                fightStatus = 'alert'
                continue
        
        elif response == 4: # Fleeing causes the player to lose extra health
            messagePrinter("You fail and fall to a critical strike from the challenger.", RED)
            playerHealth -= int(oppAttack * 2)
            fightStatus = 'alert'
        
        elif response == 5: # Choosing to ignore the opponent
            if not ignored:
                messagePrinter("The audience gasps as you turn away from the challenger, raising your megaphone to continue your speech.",)
                inputHandler('') # Requesting input to act as a break to read between text
                messagePrinter("Turns out you were playing 5D chess all along, and as the challenger goes to strike you the horribly mistime it and somehow fall off of the stage.", GREEN)
                oppHealth = int(oppHealth/2)
                ignored = True
            else:
                messagePrinter("You go too far. The challenger lands a critical strike.", RED)
                playerHealth -= int(oppAttack * 2)

        else:
            messagePrinter("Entering an invalid integer caused the opponent to gain a free attack.", RED)
        
        # The opponent's turn
        print() # Print statement to decrease visual congestion of the terminal
        if fightStatus == 'stunned':
            fightStatus = 'alert'
            continue
        elif fightStatus == 'alert':
            if random.randint(0, 1) == 0:
                messagePrinter("The challenger strikes you.")
                playerHealth -= oppAttack
            else:
                oppHeal = random.randint(0, 15)
                oppHealth += oppHeal
                messagePrinter(f"They regain {oppHeal} health.")
        elif fightStatus == 'angry':
            messagePrinter("The challenger strikes with all their might, venting their anger.")
            playerHealth -= int(oppAttack * 1.2)
            fightStatus = 'alert'

    #Ending the fight
    if playerHealth <= 0: #Checking if the player has died
        inputHandler("")
        scene = f"{scene}-1"
    elif oppHealth <= 0: #Checking if the opponent has died
        inputHandler("")
        scene = f"{scene}-2"
        displayScene(scenes[scene])
    elif fightStatus == 'dead': #Checking if the opponent has fled
        inputHandler("")
        scene = f"{scene}-3"
        displayScene(scenes[scene])
    
def challengeSneak(stealth):
    global scene

    time.sleep(1)
    messagePrinter("Get ready...")
    time.sleep(2)

    # Adjust difficulty based on the stealth variable
    baseWindowStart = 2  # Base time before the window starts
    baseWindowDuration = 1  # Base duration of the window

    # Modify the time window based on stealth
    sneakWindowStart = baseWindowStart - (stealth * 0.1)  # Higher stealth reduces the wait time
    sneakWindowDuration = baseWindowDuration + (stealth * 0.1)  # Higher stealth increases the window duration
    sneakWindowStart = max(0.5, sneakWindowStart)  # Ensure the start time is not too short
    sneakWindowDuration = min(3, sneakWindowDuration)  # Cap the maximum duration

    sneakWindowEnd = sneakWindowStart + sneakWindowDuration

    # Inform the player when to start typing
    messagePrinter("Type 'sneak' now!")
    startTime = time.time()
    inputText = input()  # Capture the player's input
    endTime = time.time()

    # Check if the input was within the correct time window
    if sneakWindowStart <= (endTime - startTime) <= sneakWindowEnd and inputText.lower() == "sneak":
        messagePrinter("You successfully sneak past the guard!", GREEN)
        inputHandler("")
        scene = f"{scene}-Success"
    else:
        messagePrinter("You failed to sneak past the guard. The guard notices you!", RED)
        inputHandler("")
        scene = f"{scene}-Fail"

    displayScene(scenes[scene])

# Function handling the nuclear meltdown challenge
# The challenge is made purposefully easy to put emphasis on the useer making their own decision to pursue this nuclear narrative
def challengeMeltdown(nuclearVolatility):
    global scene
    response = inputHandler("Prevent the meltdown. Hint: Type 'calm' the required number of times. ")
    calmCount = 0
    for word in response.lower().split():
        if word == "calm":
            calmCount += 1
    if calmCount < nuclearVolatility ** 2:  # Use ** for exponentiation in Python
        scene = "scene8B"
        displayScene(scenes[scene])
    else:
        scene = f"{scene}-1"
        displayScene(scenes[scene])

# Generates an integer response
def integerResponseGenerator():
    response = 0
    while response == 0:
        try:
            response = int(inputHandler(''))
        except ValueError:
            messagePrinter("Please enter a number.")
            response = 0
    return response

# Print messages with a delay between letters
def messagePrinter(message, currentColour=END):
    for letter in message:
        if letter == " ":
            time.sleep(writeDelay + writeDelay * spaceDelayMultiplier)    
        print(currentColour + letter, end="", flush=True)
        time.sleep(writeDelay)
    print()

#Setting keybinds and interacting with the player's responses
def keyBindHandler():
    global inventoryBind, playerHealthBind, playerHealth, saveGameBind #Accessing the global variables to change them
    response = input("Change key bindings? (y/n) ").lower()
    while response != "y" and response != "n": #Checking if the response is either y or n
        messagePrinter("Please enter a valid response.")
        response = input("Change key bindings? (y/n) ").lower()

    if response == "y": #Checking if the user wants to change the keybinds

        #InventoryBind Setting
        inventoryBind = input("Inventory: ")
        #Making sure the keybinds are unique of each other and important options
        while inventoryBind in ["1", "2", "3", "4", "", "True", "False"]:
            messagePrinter(f"[{inventoryBind}] is already bound to an option, please choose another key.")
            inventoryBind = input("Inventory: ")
        
        #playerHealthBind Setting
        playerHealthBind = input("Health: ")
        while playerHealthBind in ["1", "2", "3", "4", "", "True", "False", inventoryBind]:
            if playerHealthBind == inventoryBind:
                messagePrinter(f"[{inventoryBind}] is already bound to inventory, please choose another key.")
            elif playerHealthBind in ["1", "2", "3", "4", "", "True", "False"]:
                messagePrinter(f"[{playerHealthBind}] is already bound to an option, please choose another key.")
            playerHealthBind = input("Health: ")
        

        #saveGameBind Setting
        saveGameBind = input("Save game: ")
        while saveGameBind in ["1", "2", "3", "4", "", "True", "False", inventoryBind, playerHealthBind]:
            #Specifically ensuring that the binding is unique of other bindings
            if saveGameBind == inventoryBind:
                messagePrinter(f"[{inventoryBind}] is already bound to inventory, please choose another key.")
            elif saveGameBind == playerHealthBind:
                messagePrinter(f"[{playerHealthBind}] is already bound to health, please choose another key.")

            #Ensuring that the binding won't overlap with future options, overprotective just in case
            elif saveGameBind in ["1", "2", "3", "4", "", "True", "False"]:
                messagePrinter(f"[{saveGameBind}] is already bound to an option, please choose another key.")
            saveGameBind = input("Save game: ")
        messagePrinter("Key bindings have been changed, your new key bindings are:")
        messagePrinter(f"Inventory: [{inventoryBind}]" + "\n" + f"Health: [{playerHealthBind}]" + "\n" + f"Save: [{saveGameBind}]" + "\n")
    return response

# This checks what the next scene is, and progresses the storyline in that direction
def moveScene(sceneKey):
    global scene
    scene = sceneKey["move"]
    displayScene(scenes[scene])

#Handle inputting from the user and find next scene for booleans
def boolHandler(sceneKey):
    global scene
    try:
        print()
        choice = inputHandler(f"{sceneKey["bool"]} ").lower()
        if choice == 'y':
            scene = f"{scene}-True"
            displayScene(scenes[scene])
        elif choice == 'n':
            scene = f"{scene}-False"
            displayScene(scenes[scene])
        else:
            print("Please input either y/n.")
            boolHandler(sceneKey)
    except ValueError:
        os.system("clear")
        print("There was an error with inputting, please input either y/n.", "\n")
        boolHandler(sceneKey)


# Handle user input and navigate to the next scene
def optionHandler(sceneKey):
    global scene #Accessing the scene variable globally so that changes are kept
    choice = 0 #Setting the choice to 0 to trigger the while loop
    try:
        while choice not in range(1, len(sceneKey["options"])):
            choice = int(inputHandler(sceneKey["options"]["optionText"]))
            if choice not in range(1, len(sceneKey["options"])):
                print("Please enter a valid option.")
        scene = f"{scene}-{choice}"
        displayScene(scenes[scene])
    except ValueError:
        os.system("clear")
        print("There was an error with inputting, please input a number.", "\n")
        optionHandler(sceneKey)

# Display the current scene and its options
def displayScene(sceneKey):
    global scene, countrysideEnding, nuclearVolatility, stealth, playerHealth
    os.system("clear")

    if len(sceneKey["text"]) > 1: #Checking if there are parameters (colour) added to the text
        colour = globals().get(sceneKey["text"][1], END)  # Get the color code from the global variables
        messagePrinter(sceneKey["text"][0], colour)
    else:
        messagePrinter(sceneKey["text"][0]) #Displaying the text of the scene

    #Items
    if "item" in sceneKey: #Adding any items to the inventory
        inventory.append(sceneKey["item"])
        print()
        messagePrinter(f"A {sceneKey["item"]} has been added to you inventory!")
    
    if "removeItem" in sceneKey:
        inventory.remove(sceneKey["removeItem"])
        messagePrinter(f"A {sceneKey["removeItem"].lower()} has been removed from your inventory.")

    if "health" in sceneKey: #Checking if there is a health change
        playerHealth += sceneKey["health"]
        if playerHealth <= 0: #Checking if the health is less than or equal to 0
            messagePrinter("You have died.")
            scene = "end"
    
    if "stealth" in sceneKey: #Checking if there is a stealth change
        stealth += sceneKey["stealth"]

    if "nuclearVolatility" in sceneKey: #Checking if there is a nuclear volatility change
        nuclearVolatility += sceneKey["nuclearVolatility"]
    
    if "countrysideEnding" in sceneKey:
        countrysideEnding = True

    if "options" in sceneKey: # Checking if there are options to choose from
        #Displaying the options
        for key, option in sceneKey["options"].items():
            if key != "optionText":
                messagePrinter(f"{key.title()}: {option}")
        print()
        
        optionHandler(sceneKey) #Requesting input to trigger game progression

    elif "bool" in sceneKey: #Checking if there is a boolean to choose from
        boolHandler(sceneKey)

    elif "boolMoney" in sceneKey: #Checking if there is an item unlockable event to choose from
        if "wallet" in inventory or "briefcase" in inventory:
            inputHandler(sceneKey["boolMoney"])
            if "wallet" in inventory:
                inventory.remove("wallet")
            elif "briefcase" in inventory:
                inventory.remove("briefcase")
            scene = f"{scene}-True"
            displayScene(scenes[scene])
        else:
            messagePrinter(sceneKey["boolMoneyFail"], RED)
            scene = "end"

    elif "move" in sceneKey: # Move to the next scene
        inputHandler("")
        moveScene(sceneKey)

    elif "opportunity" in sceneKey: # Handling opportunities based on items held
        if sceneKey["opportunity"][0] in inventory:
            response = 0
            # Deriving a valid response from the user
            while response != "y" or response != "n":
                print()
                response = inputHandler(sceneKey["opportunity"][1]) 
                if response == "y":
                    # Determine outcome based on a random 50/50
                    if random.randint(0, 1) == 0: # Successful outcome
                        scene = f"{scene}-1"
                        displayScene(scenes[scene])
                    else: # Failed outcome
                        scene = f"{scene}-2"
                        displayScene(scenes[scene])
                # Declined response
                elif response == "n":
                    scene = f"{scene}-3"
                    displayScene(scenes[scene])
                else:
                    print("Please input either y/n.")
        else:
            # Triggered when opportunity unavailable due to current inventory status
            response = inputHandler('')
            scene = f"{scene}-3"
            displayScene(scenes[scene])
    
    # If statements checking if their respective challenges are present
    elif "challengeSpeech" in sceneKey:
        messagePrinter(sceneKey["challengeSpeech"])
        challengeSpeechContest()
    
    elif "challengeFight" in sceneKey:
        messagePrinter(sceneKey["challengeFight"])
        challengeFight(attack)
    
    elif "challengeSneak" in sceneKey:
        messagePrinter(sceneKey["challengeSneak"])
        challengeSneak(stealth)
    
    elif "challengeMeltdown" in sceneKey:
        messagePrinter(sceneKey["challengeMeltdown"])
        challengeMeltdown(nuclearVolatility)
    
    # If statements determining which ending to take depending on the countrySideEnding variable's boolean status
    elif "peacefullEnding" in sceneKey:
        if countrysideEnding == True:
            messagePrinter(sceneKey["peacefullEnding"])
        else:
            messagePrinter(sceneKey["mainEnding"])
        scene = "end"
    


# Handle general inputting from the user
def inputHandler(inputText):
    # Asking for input to trigger requested functions
    response = input(inputText)

    if response == inventoryBind: # Showing inventory contents
        if inventory:
            messagePrinter("Inventory:")
            print()
            for item in inventory:
                messagePrinter(item.strip().title())
            print()
        else:
            messagePrinter("Inventory is empty.")
        response = inputHandler(inputText)

    elif response == playerHealthBind: # Showing health
        messagePrinter(f"Health: {playerHealth}")
        response = inputHandler(inputText)

    elif response == saveGameBind: # 
        messagePrinter("Saving the game...", BLUE)
        saveFileWriter()
        messagePrinter("Save Successull!", GREEN)
        response = inputHandler(inputText)


    return response #Returning a response to be used by functions such as optionHandler or boolHandler

# This is a utility function that finds the path to the requested fie, compatible with the operating system
def getFilePath(file):
    currentFolder = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(currentFolder, file)
    return filePath

# Save File Functions
def saveFileWriter():
    global inventory, playerHealth, inventoryBind, playerHealthBind, saveGameBind, scene, writePreset
    filePath = getFilePath("saveFile.txt")

    with open(filePath, "w") as saveFile:
        # Write game stats
        saveFile.write("# Scene-specific stats\n")
        saveFile.write(f"stealth {stealth}\n")
        saveFile.write(f"nuclearVolatility {nuclearVolatility}\n")
        saveFile.write(f"foodBonus {foodBonus}\n")
        saveFile.write(f"attack {attack}\n")
        saveFile.write(f"countrysideEnding {countrysideEnding}\n")

        # Write inventory
        saveFile.write("# General player stats\n")
        saveFile.write(f"inventoryItems {' '.join(inventory)}\n")
        saveFile.write(f"playerHealthStat {playerHealth}\n\n")

        # Write keybinds
        saveFile.write("# Keybinds\n")
        saveFile.write(f"inventoryBind {inventoryBind}\n")
        saveFile.write(f"playerHealthBind {playerHealthBind}\n")
        saveFile.write(f"saveGameBind {saveGameBind}\n\n")

        # Write current scene
        saveFile.write("# Starting scene\n")
        saveFile.write(f"scene {scene}\n\n")

        saveFile.write("# Backend variables\n")
        saveFile.write(f"writePreset {writePreset}\n")

# Reads the requested file and adds the 
def fileLoader(fileName):
    global inventory, playerHealth, inventoryBind, playerHealthBind, saveGameBind, scene, writePreset, stealth, nuclearVolatility, foodBonus, attack, countrysideEnding
    filePath = getFilePath(fileName)

    messagePrinter("Loading Save File...", BLUE)
    time.sleep(0.5) #This is only to give the feeling that something is happenning
    
    try:
        with open(filePath, "r") as file:
            lines = file.readlines()
            for line in lines:
                # In each elif block, the words are split between their value and keys, and the keys are assigned to their respective variables
                if line.startswith("inventoryItems"):
                    inventory = line.strip().split()[1:]
                    inventory = [item.strip() for item in inventory]  # Ensure items are properly stripped and added as a list
                elif line.startswith("playerHealthStat"):
                    playerHealth = int(line.strip().split()[1])
                elif line.startswith("inventoryBind"):
                    inventoryBind = line.strip().split()[1]
                elif line.startswith("playerHealthBind"):
                    playerHealthBind = line.strip().split()[1]
                elif line.startswith("saveGameBind"):
                    saveGameBind = line.strip().split()[1]
                elif line.startswith("scene"):
                    scene = line.strip().split()[1]
                elif line.startswith("writePreset"):
                    writePreset = line.strip().split()[1]
                elif line.startswith("stealth"):
                    stealth = line.strip().split()[1]
                elif line.startswith("nuclearVolatility"):
                    nuclearVolatility = line.strip().split()[1]
                elif line.startswith("foodBonus"):
                    foodBonus = line.strip().split()[1]
                elif line.startswith("attack"):
                    attack = line.strip().split()[1]
                elif line.startswith("countrysideEnding"):
                    countrysideEnding = line.strip().split()[1]
    # In the case that an error occurs with the saveFile not being present or inaccessible
    except FileNotFoundError:
        messagePrinter("No save file found. Using backup default values.", YELLOW)
    
    messagePrinter("File loaded successfully!", GREEN)

# Request either a previous save file to be loaded or to start a new game
def askForSaveFileLoad():
    response = inputHandler("[a] Load save file and configurations" + "\n" + "[b] New Game (a/b) ").lower()
    while response not in ["a", "b"]:
        messagePrinter("Please enter either a or b.")
        response = inputHandler("[a] Load save file and configurations" + "\n" + "[b] New Game (a/b) ").lower()
    if response == "a":
        fileLoader("saveFile.txt")
    elif response == "b":
        fileLoader("newGame.txt")

# Print sample text at various speeds
def writeDelayDemo():
    global writeDelay
    # Cycles through the speeds and displays a samble text at that speed
    for speed in writeSpeedPresets:
        writeDelay = writeSpeedPresets[speed]
        messagePrinter(f"Example of {speed} speed.")
        time.sleep(0.5)

# Changing the write speed variable based on responses, and determining whether to show the write demo
def writeSpeedHandler():
    messagePrinter("Choose your writing speed:\n")

    # Requesting to show demo speeds
    response = inputHandler("See Demo Speeds? (y/n) ")
    while response != "y" and response != "n":
        messagePrinter("Please input either y or n.")
        response = inputHandler("See Demo Speeds? (y/n) ")
    if response == "y":
        writeDelayDemo() # Call to write demo function
    
    # Requesting write speed
    response = input("Choose your preferred write speed: [1] slow | [2] medium | [3] medium-fast | [4] fast ")
    while response not in ["1", "2", "3", "4"]:
        response = input("Choose your preferred write speed: [1] slow | [2] medium | [3] medium-fast | [4] fast ")
    setWriteSpeed(response)

# Set the write speed to the chosen speed
def setWriteSpeed(response):
    global writeDelay
     # Converting the values of the writeSpeedPresets dictionary into a list
    presets = []
    for key in writeSpeedPresets:
        presets.append(writeSpeedPresets[key])
    
    # Matching the value to the response, and setting the value
    counter = 1
    for value in presets:
        if counter == int(response):
            writeDelay = value
        counter += 1
    

#Display opening text and handle calling of various functions, for game setup of save files, keybinds and text speed
def intro():
    #Displaying opening text & info
    messagePrinter("Welcome To Overexcited Activist!" + "\n")
    time.sleep(0.2)

    askForSaveFileLoad() # Starting a new game or continuing a pre-existing game
    writeSpeedHandler() # Setting the game print speed
    

    # Displaying game controls
    messagePrinter("Controls:")
    messagePrinter(f"Inventory: [{inventoryBind}]" + "\n" + f"Health: [{playerHealthBind}]" + "\n" + f"Save: [{saveGameBind}]" + "\n")
    time.sleep(0.2)

    #Requesting changes to keybinds of inventory and health
    response = keyBindHandler()
    if response != "n": #Checking if confirmation is necessary
        response = input("Confirm bindings? (y) ").lower()
        while response != "y": #Looping until the user confirms the keybinds
            keyBindHandler()
            response = input("Confirm bindings? Note: [n] will retain new bindings. (y/n) ").lower()
    
    inputHandler("Begin? ") #Requesting input to begin the game or demo controls
    os.system("clear")

# Game Loop
intro() #Call into to the game
while scene != "end":
    displayScene(scenes[scene])