from random import randint




def LB():
    p("------------------------------------------------------")

def p(toPrint):
    print(toPrint)

def showStats():
    global playerStats
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    p("H:" + str(playerStats[0]) + "|S:" + str(playerStats[1]) + "|D:" + str(playerStats[2]) + "|M:" + str(playerStats[3]) + "|G:" + str(playerStats[4]))
    p("J:" + playerJob + "|" + str(playerJobSalary))
    

def numericalQuestion(maxNumber):
    while True:
        while True:
            try:
                numericalInput = input("-")
                numericalInput = int(numericalInput)
                break
            except:
                if numericalInput == "S" or numericalInput == "s":
                    showStats()
                else:
                    p("Please enter a numerical value")
        if numericalInput >= maxNumber + 1:
            p("Value too high")
        elif numericalInput <= 0 or numericalInput == 0:
            p("Value too low")
        else:
            return numericalInput

def gameStart():
    p("Setting up...")
    LB()
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    playerJobSalary = 0
    playerEquipment = [["", 0, 0], ["", 0, 0], ["", 0, 0]]
    newReincarnation(0)

def newReincarnation(reincarnationValue):
    global magicType
    magicType = "Undefined"
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if reincarnationValue == 0:
        playerSpecies = speciesGeneration()
        playerStats = [1, 1, 1, 0, 0] #Health, Strength, Dexterity, Magic, and Gold
        p("You have been placed into the body of " + playerName + ".")
        p("YOu are a " + playerSpecies + " Newborn")
    staticLife()


def staticLife():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    isAlive = True
    while isAlive == True:
        chooseMagicType()
        if playerAge <= 11 and playerAge >= 4:
            p("Wait out your childhood at home(1) or go Adventuring(2)")
            p("WARNING: Going adventuring at this age adds difficulty to the game.")
            childDecicion = numericalQuestion(2)
            if childDecicion == 1:
                timeSkip()
            elif childDecision == 2:
                goQuesting()
        elif playerAge <= 4:
            p("You are an infant child, and therefore cannot act at this time")
            timeSkip()
        else:
            p("Spend some time at home(1) or go Adventuring(2)")
            playerDecision = numericalQuestion(2)
            if playerDecision == 1:
                timeSkip()
            elif playerDecision == 2:
                goQuesting()
    

def timeSkip():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    p("How long would you like to skip? This will be interrupted if you experiance any life-changing events. Maximum time 99 years")
    timeToSkip = numericalQuestion(1000)
    while timeToSkip != 0 and isAlive == True:
        ageOneYear()
        timeToSkip = timeToSkip - 1
    showStats()

def ageOneYear():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    p("You are now " + str(playerAge + 1) + " years old.")
    playerStats[4] = playerStats[4] + playerJobSalary
    event = randint(1, 6)
    if event == 1:
        eventNumber = randint(1, 2)
        while eventNumber >= 0 and isAlive == True:
            agingEvent()
            eventNumber = eventNumber - 1
    elif event == 2:
        eventNumber = randint(0, 3)
        while eventNumber >= 1 and isAlive == True:
            agingEvent()
            eventNumber = eventNumber - 1
    else:
        agingEvent()
    playerAge = playerAge + 1

def agingMagicSpawn(magicChance):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    hasMagic = randint(1, magicChance)
    if hasMagic == 1 and playerStats[3] == 0:
        playerStats[3] = playerStats[3] + 1
        p("Growing up, " + playerName + " shows unusual abilities - they seem to have natural magical talent")

def jobGeneration(grouping):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    playerJobGroup = "misc"
    jobGroupList = ["MAGIC", "ARMY", "NOBLE", "CRIME", "POOR", "HOLY", "OUTER", "PRODUCTION", "CITY"]
    magicJobs = ["Necomancer", "Artificer", "Mage", "Enchanter", "Warlock"]
    crimeJobs = ["Thief", "Assassin", "Thug"]
    armyJobs = ["Soldier", "Veteran Soldier", "Army Officer", "General"]
    cityJobs = ["Factory Worker", "Paper Pusher", "Begger"]
    productionJobs = ["Potter", "Blacksmith", "Tailor", "Leatherworker"]
    outerJobs = ["Hermit", "Highwayman"]
    holyJobs = ["Priest", "High Priest"]
    nobleJobs = ["Count", "Baron", "Knight", "Lord"]
    poorJobs = ["Farmer", "Herder", "Trader"]
    if grouping == 1:
        #job specification
        specifyJob = jobGroupList[randint(3, 8)]
        if specifyJob == "CRIME":
            job = crimeJobs[randint(0, 2)]
        elif specifyJob == "ARMY":
            job = armyJobs[0]
        elif specifyJob == "CITY":
            job = cityJobs[randint(0, 2)]
        elif specifyJob == "PRODUCTION":
            job = productionJobs[randint(0, 3)]
        elif specifyJob == "OUTER":
            job = outerJobs[randint(0, 1)]
        elif specifyJob == "HOLY":
            job = holyJobs[0]
        elif specifyJob == "POOR":
            job = poorJobs[randint(0, 2)]
        else:
            p("Index out of range")

    elif grouping == 0:
        specifyJob = randint(1, 100)
        if specifyJob <= 5:
            job = "Blessed Child"
        elif specifyJob <= 30:
            job = "Thief"
        else:
            job = "Farmer"
            
    else:
        p("Error")
    p(job)
    return job

def findNewJob(testValue):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    jobFound = jobGeneration(testValue)
    p("You have gained the chance to become a " + jobFound)
    p("Accept(1), or continue your current life(2)")
    hasAccepted = numericalQuestion(2)
    if hasAccepted == 1:
        playerJob = jobFound
        jobStats = checkJobStats(jobFound)
        p("Your new job has a salary of " + str(playerJobSalary))
        return salaryIllnessCheck()
    else:
        p("You continue on as before")
        return [5, 2, 10, 1, 0]
    
def checkJobStats(jobSelected):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    largeJobsList = [["Blessed Child", 0], ["Necomancer", randint(5, 15)], ["Artificer", randint(40, 100)], ["Mage", randint(10, 20)], ["Enchanter", randint(20, 50)], ["Warlock", (randint(1, 30))], ["Thief", randint(1, 3)], ["Assassin", randint(5, 15)], ["Thug", randint(1, 3)], ["Soldier", 6], ["Veteran Soldier", 8], ["Army Officer", 20], ["General", randint(30, 50)], ["Factory Worker", randint(1, 3)], ["Paper Pusher", randint(1, 5)], ["Begger", 1], ["Potter", randint(3, 20)], ["Blacksmith", randint(3, 20)], ["Tailor", randint(1, 20)], ["Leatherworker", randint(1, 20)], ["Hermit", 0], ["Highwayman", randint(1, 12)], ["Priest", randint(0, 1)], ["High Priest", randint(0, 100)], ["Count", randint(50, 100)], ["Baron", randint(20, 80)], ["Knight", randint(10, 30)], ["Lord", randint(80, 200)], ["King", randint(100, 1000)], ["Farmer", randint(1, 4)], ["Herder", randint(1, 2)], ["Trader", randint(1, 8)]]
    xValue = 0
    hasFound = False
    try:
        while hasFound == False:
            if jobSelected == largeJobsList[xValue][0]:
                playerJobSalary = largeJobsList[xValue][1]
                hasFound == True
            xValue = xValue + 1
    except:
        null = 0
        

def salaryIllnessCheck():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if playerJobSalary <= 0:
        return [2, 3, 14, 1]
    elif playerJobSalary <= 5:
        return [4, 2, 8, 1]
    elif playerJobSalary <= 15:
        return [8, 2, 6, 1]
    elif playerJobSalary <= 30:
        return [12, 1, 6, 2]
    elif playerJobSalary <= 60:
        return [14, 1, 4, 2]
    elif playerJobSalary >= 120:
        return [20, 0, 3, 4]



def playerEmployment(ageType):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if ageType == 0:
        employmentChance = randint(1, 20)
        if employmentChance == 1:
            valueToReturn = findNewJob(0)
        else:
            valueToReturn = [5, 2, 10, 1]
    elif ageType == 1:
        if playerJob == "Child":
            playerJob = "Unemployed"
            valueToReturn = [5, 2, 10, 1]
        if playerJob == "Unemployed":
            employmentChance = randint(1, 3)
            if employmentChance == 1:
                valueToReturn = findNewJob(1)
            else:
                employmentChance = randint(1, 20)
                if employmentChance == 1:
                    valueToReturn = findNewJob(1)
                else:
                    valueToReturn = [5, 2, 10, 1]
        else:
            valueToReturn = salaryIllnessCheck()
    return valueToReturn

def runIllnessCheck(chance, requisite, healthChange):#requisite and healthChange are both 2 value lists
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    illnessChance = randint(1, chance)
    tripChance = randint(1, chance)
    if illnessChance == 1:
        if playerStats[1] <= randint(requisite[0], requisite[1]):
            playerStats[0] = playerStats[0] - randint(healthChange[0], healthChange[1])
            if playerStats[0] <= 0:
                p("You fell ill and died")
                isAlive = False
            else:
                p("You fell ill")
    elif tripChance == 1:
        if playerStats[2] <= randint(requisite[0], requisite[1]):
            playerStats[0] = playerStats[0] - randint(healthChange[0], healthChange[1])
        if playerStats[0] <= 0:
            p("You tripped over and broke your neck")
            isAlive = False
        else:
            p("You tripped over")

def chooseMagicType():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if playerStats[3] >= 1 and magicType == "Undefined":
        p("Select Magic type to experiment with")
        p("The Mage Arts(1), Enchanting(2), or Necromancy(3)")
        p("WARNING: choosing necromancy makes the game more difficult")
        magicTypeNumber = numericalQuestion(3)
        if magicTypeNumber == 1:
            magicType = "The Mage Arts"
        if magicTypeNumber == 2:
            magicType = "Enchanting"
        if magicTypeNumber == 3:
            magicType = "Necromancy"
    

def agingInfantStats(healthStat, strStat, dexStat, moneyStat):#all of these are lists with two values - lower and upper
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    statIncrease = randint(1, 5)
    if statIncrease == 1:
        statAmount = randint(healthStat[0], healthStat[1])
        p(playerName + " is an unusually healthy child")
        playerStats[0] = playerStats[0] + statAmount
    elif statIncrease == 2:
        statAmount = randint(strStat[0], strStat[1])
        p(playerName + " is Strong and competative")
        playerStats[1] = playerStats[1] + statAmount
    elif statIncrease == 3:
        statAmount = randint(dexStat[0], dexStat[1])
        p(playerName + " shows great quickness of motion - even as a child")
        playerStats[2] = playerStats[2] + statAmount
    elif statIncrease == 4:
        p(playerName + " shows no special traits")
    elif statIncrease == 5:
        statAmount = randint(moneyStat[0], moneyStat[1])
        p(playerName + " was born to Wealthy parents")
        playerStats[4] = playerStats[4] + statAmount

def agingToddlerStats(health, stre, Dex):#all three are double value lists
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    statIncreaseType = randint(1, 3)
    if statIncreaseType == 1:
        playerStats[0] = playerStats[0] + randint(health[0], health[1])
    elif statIncreaseType == 2:
        playerStats[1] = playerStats[1] + randint(stre[0], stre[1])
    elif statIncreaseType == 3:
        playerStats[2] = playerStats[2] + randint(Dex[0], Dex[1])

def agingMiscStats(health, stre, Dex, magic):#magic has its own lower and upper values, is list. same with health
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    statIncreaseType = randint(1, 4)
    if statIncreaseType == 1:
        playerStats[0] = playerStats[0] + randint(health[0], health[1])
    elif statIncreaseType == 2:
        playerStats[1] = playerStats[1] + randint(stre[0], stre[1])
    elif statIncreaseType == 3:
        playerStats[2] = playerStats[2] + randint(Dex[0], Dex[1])
    elif statIncreaseType == 4 and playerStats[3] >= 1 and magicType != "Undefined":
        playerStats[3] = playerStats[3] + randint(magic[0], magic[1])
        p("Your research into " + magicType + " bore fruit.")
    else:
        null = 0


    
def humanAging():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if playerAge == 0:
        playerJob = "Infant"
        agingMagicSpawn(10)
        agingInfantStats([10, 30], [2, randint(3, 7)], [2, randint(3, 7)], [10, 30])
    elif playerAge <= 4:
        playerJob = "Toddler"
        playerStats[0] = playerStats[0] + randint(1, 3)
        agingMagicSpawn(30)
        statIncrease = randint(0, 1)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingToddlerStats([1, playerStats[1]], [1, 3], [1, 3])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(2, [1, 2], [4, 10])
    elif playerAge <= 12:
        homeLife = playerEmployment(0)
        playerJob = "Child"
        playerStats[0] = playerStats[0] + randint(1, 5)
        agingMagicSpawn(200)
        statIncrease = randint(0, 5)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([1, playerStats[1]], [1, 4], [1, 4], [1, 1])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(5, [1, 4], [5, 15])
    elif playerAge <= 25:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(1, 5)
        statIncrease = randint(0,8)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([1, playerStats[1]], [1, 6], [1, 6], [1, homeLife[3]])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [5, 15])
    elif playerAge <= 40:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(-3, 3)
        statIncrease = randint(0, 3)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([1, playerStats[1]], [-1, 2], [-1, 2], [1, homeLife[3]])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [1, 10])
    else:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(-3, 1)
        statIncrease = randint(0, 2)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([-12, playerStats[1]], [-2, 0], [-2, 0], [1, homeLife[3] + 2])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [10, 30])

def goblinAging():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if playerAge == 0:
        playerJob = "Infant"
        agingMagicSpawn(100)
        agingInfantStats([2,8], [1, randint(2, 3)], [2, randint(5, 6)], [1, 4])
    elif playerAge <= 2:
        playerJob = "Toddler"
        playerStats[0] = playerStats[0] + randint(2, 5)
        statIncrease = randint(0, 1)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingToddlerStats([1, playerStats[1]], [1, 2], [1,5])
        elif townEvent == 0:
            largeTownEvent()
    elif playerAge <= 5:
        playerJob = "Child"
        playerStats[0] = playerStats[0] + randint(5, 10)
        agingMagicSpawn(200)
        statIncrease = randint(0, 3)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([1, playerStats[1]], [1, 4], [2, 8], [1, 1])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(5, [1, 4], [1, 10])
    elif playerAge <= 12:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(5, 15)
        statIncrease = randint(0,4)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([1, playerStats[1]], [2, 4], [4, 12], [1, homeLife[3]])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [1, 10])
    elif playerAge <= 18:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(-24, 2)
        statIncrease = randint(0, 2)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([-15, playerStats[1]], [-2, 1], [-1, 1], [1, homeLife[3]])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [1, 10])
    else:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(-20, 0)
        statIncrease = randint(0, 1)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([-30, playerStats[1]], [-3, 0], [-3, 0], [1, homeLife[3] + 1])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [4, 10])

def demigodAging():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if playerAge == 0:
        playerJob = "Infant"
        agingMagicSpawn(2)
        agingInfantStats([20, 50], [5, randint(10, 20)], [5, randint(10, 20)], [50, 400])
    elif playerAge <=6:
        playerJob = "Toddler"
        playerStats[0] = playerStats[0] + randint(3, 10)
        agingMagicSpawn(4)
        statIncrease = randint(0, 1)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingToddlerStats([2, playerStats[1]*2], [3, 9], [3, 9])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(5, [1, 2], [5, 10])
    elif playerAge <=12:
        playerJob = "Child"
        playerStats[0] = playerStats[0] + randint(5, 15)
        agingMagicSpawn(30)
        statIncrease = randint(0, 5)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([2, playerStats[1]*2], [3, 12], [3, 12], [1, 3])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(5, [1, 4], [5, 15])
    elif playerAge <= 36:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(5, 30)
        statIncrease = randint(0,8)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([2, playerStats[1]*2], [3, 18], [3, 18], [1, homeLife[3]*3])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [5, 15])
    elif playerAge <= 120:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(-4, 6)
        statIncrease = randint(0,4)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([2, playerStats[1]*2], [-2, 3], [-2, 3], [1, homeLife[3]*6])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1], homeLife[2]], [10, 20])
    else:
        homeLife = playerEmployment(1) #returns a list
        playerStats[0] = playerStats[0] + randint(-10, 5)
        statIncrease = randint(0, 2)
        townEvent = randint(0, 20)
        if statIncrease == 0:
            agingMiscStats([-20, playerStats[1]*2], [-3, 2], [-3, 2], [1, homeLife[3]*10])
        elif townEvent == 0:
            largeTownEvent()
        else:
            runIllnessCheck(homeLife[0], [homeLife[1]*3, homeLife[2]*3], [10, 30])




def agingEvent():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if playerSpecies == "Human":
        humanAging()

    elif playerSpecies == "Demigod":
        demigodAging()
        
    elif playerSpecies == "Goblin":
        goblinAging()
        
    else:
        p("AgingEventFail")
            

    if playerStats[0] <= 0 and isAlive == True:
        p("You died of old age")
        isAlive = False
    if playerStats[1] <= 0 and isAlive == True:
        p("You grew weak and withered away")
        isAlive = False
    if playerStats[2] <= 0 and isAlive == True:
        p("You couldent get up in the morning")
        isAlive = False

def largeTownEvent():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    p("PlaceholderTownEvent")
        
    

def speciesGeneration():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    randSpecies = randint(0, 100)
    if randSpecies <= 0:
        playerName = nameGeneration(0)
        playerAge = 0
        return "Demigod"
    elif randSpecies <= 10:
        playerName = nameGeneration(0)
        playerAge = 0
        return "Goblin"
    elif randSpecies <= 100:
        playerName = nameGeneration(0)
        playerAge = 0
        return "Human"
    else:
        return "Error: String out of range"
        playerName = nameGeneration(0)
        playerAge = ageGeneration(0)



def ageGeneration(ageType): #needs editing to be used for NPC
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if ageType == 0:
        ageRange = randint(0, 10)
        if ageRange == 0:
            playerJob = "Newborn"
            return 0
        elif ageRange <= 3:
            playerJob = jobGeneration(1)
            return randint(1, 12)
        elif ageRange <= 9:
            playerJob = jobGeneration(0)
            return randint(13, 40)
        elif ageRange == 10:
            playerJob = jobGeneration(0)
            return randint(10, 99)
        else:
            null = 0
    if ageType == 1:
        ageRange = randint(0, 10)
        if ageRange <= 1:
            playerJob = jobGeneration(1)
            return randint(6, 12)
        elif ageRange <= 9:
            playerJob = jobGeneration(0)
            return randint(13, 40)
        elif ageRange == 10:
            playerJob = jobGeneration(0)
            return randint(10, 99)
        else:
            null = 0
    else:
        null = 0

def nameGeneration(nameType):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    if nameType == 0:
        name_list  = ["John ", "David ", "Vrail ", "Harry ", "Jeffrey ", "Alex ", "Joe ", "Alfred ", "Barry "]
        surname_list = ["Smith", "Crow", "Hill", "Farmer", "Johnsson", "Franksson"]
        name1 = randint(0, 8)
        name2 = randint(0, 5)
        name = name_list[name1] + surname_list[name2]
    else:
        null = 0
    return name

    

def checkEquipment():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    #Weapon, and damage, and value
    #Armour, and resistance level, and value
    #playerEquipment = [["", 0, 0], ["", 0, 0], ["", 0, 0]]
    p(playerEquipment)

def goQuesting():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    chooseMagicType()
    p("You abandon your home, and job, and strike out into the world!")
    playerJob = "Unemployed"
    playerJobSalary = 0
    isQuesting = True
    while isQuesting == True:
        doQuestTick()
        p("Continue onwards(1) or abandon this Quest(2)")
        isQuestingQuestion = numericalQuestion(2)
        if isQuestingQuestion == 2:
            isQuesting = False
            p("Retreat in Shame")
        elif isQuestingQuestion == 1:
            isQuesting = True
            ("We Quest Onward!")
        else:
            p("Error")

def doQuestTick():
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    encounterDice = randint(0, 100)
    encounterType = randint(0, 9)
    if encounterType <= 3:
        staticEncounter(encounterDice)
    elif encounterType <= 8:
        entityEncounter(encounterDice)
    elif encounterType <= 9:
        miscEncounter(encounterDice)

def staticEncounter(encounterDice):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    #Static encounters are things like buildings, towns, necromantic towers. Something that doesnt, or shouldent move
    p("Do the encounter thing [static]")

def entityEncounter(encounterDice):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    #Entity encounters are some kind of living or lifelike being. A zombie army, a trader, a soldier, even a dead body.
    p("Do the encounter thing [entity]")

def miscEncounter(encounterDice):
    global playerName
    global playerAge
    global playerSpecies
    global playerJob
    global magicType
    global isAlive
    global playerStats #Health, Strength, Dexterity, Magic, and Gold
    global playerEquipment #Item:StatValue:Value - Weapon, Armour
    global playerJobSalary
    #Misc encounbters are something else. A pouch of coins on the floor, for instance
    p("Do the encounter thing [misc]")




while True:
    gameStart()
    input()

























    







