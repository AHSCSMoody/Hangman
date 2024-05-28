import random
lstSecretWords = ['an', 'no' , 'be', 'do' , 'it' , 'to' , 'as' , 'me' , 'no' , 'if' , 'he' , 'see' , 'ace' , 'set' , 'eat' , 'met' , 'him' , 'rat' , 'cat' , 'dog' , 'fox', 'get' , 'nip' , 'dip' , 'zoo' , 'wet' , 'fit' , 'pop' , 'gap', 'bee' , 'run' , 'rot' , 'yes' , 'and' , 'ant' , 'mat' , 'jug' , 'ten' , 'pop' , 'gas', 'vat', 'like' , 'look' , 'tuck' , 'tire' , 'raft' , 'five' , 'rift' , 'quit' , 'fads', 'faid' , 'paid' , 'said' , 'meet' , 'team' , 'took' , 'tree' , 'reed' , 'give' , 'gift' , 'jump' , 'gunk' , 'sift' , 'nick', 'nook' , 'nice' , 'boys' , 'boot' , 'hive' , 'dump' , 'were' , 'what' , 'veer', 'fizzy' , 'jazzy' , 'dizzy' , 'pizza' , 'jerky' , 'cozey' , 'woozy' , 'jiffy' , 'other', 'which' , 'there' , 'stock' , 'eagle' , 'ether' , 'extra' , 'enemy', 'shady' , 'shaft' , 'seven' , 'sheer' , 'sizes' , 'check', 'chaff' , 'chick' , 'equip' , 'zebra', 'dozen' , 'fizzle' , 'snazzy' , 'number' , 'people' , 'before' , 'supper' , 'racing', 'tonics' , 'stared' , 'spread' , 'acorns' , 'allies' , 'axioms' , 'muzzle', 'dazzle' , 'guzzle' , 'nozzle' , 'squawk' , 'quirky' , 'frenzy' , 'breezy' , 'quiche' , 'quench', 'jackey' , 'koozie' , 'wizard' , 'quaker' , 'suffix' , 'tester' , 'tattle' , 'tarter', 'stones' , 'stilts' , 'stone' , 'street' , 'series' , 'senses' , 'senior' , 'router', 'rulers' , 'saints' , 'sailor' , 'rustle' , 'saloon' , 'resist' , 'return' , 'resell' , 'outlet', 'raisin' , 'rattle' , 'noises' , 'eraser' , 'errors' , 'assist' , 'assent' , 'alerts' , 'antler' , 'annual', 'strong' , 'studio' , 'jackpot' , 'jetpack' , 'checkup' , 'through' , 'picture' , 'country', 'believe' , 'between' , 'bedroom' , 'behooze' , 'beanbag' , 'bathing' , 'climbed' , 'capable' , 'calling' , 'cavalry', 'closely' , 'wanting' , 'wizards' , 'whacked' , 'equally' , 'exactly' , 'firebox' , 'jawbone' , 'jumbled', 'jamming' , 'jumping' , 'showoff' , 'psychic' , 'hemlock' , 'hyphens' , 'bowling' , 'mixtape' , 'mudpack', 'pathway' , 'playoff' , 'sickbay' , 'sixfold' , 'skydive' , 'bewitch' , 'calcify' , 'chamfer' , 'crunchy', 'fickled' , 'fuzzball' , 'absolute' , 'mountain' , 'sentence' , 'elephant' , 'platypus' , 'flamingo' , 'hijacker' , 'slapjack' , 'chockful', 'jumpshot' , 'squeaked' , 'vocalize' , 'backflip' , 'barbeque' , 'cakewalk' , 'checkups' , 'chipmunk' , 'paybacks', 'symphony' , 'walkaway' , 'textbook' , 'backyard' , 'flextime' , 'farmwork' , 'humidify' , 'washaway' , 'aquatics' , 'strainer', 'stroller' , 'sunstone' , 'stations' , 'sinister' , 'senators' , 'routines' , 'embezzled' , 'chocolate' , 'essential' , 'advantage', 'strength' , 'dystrophy' , 'stylishly' , 'abhorrent' , 'abilities' , 'abrasions' , 'acquitted' , 'baseboards' , 'bleachers' , 'drizzling' , 'lifehacks', 'newlyweds' , 'recognize' , 'technique' , 'reflexive' , 'yellowish' , 'whichever' , 'adulthood' , 'haphazard' , 'oxidizing', 'objectify' , 'windowbox' , 'transient' , 'solitaire' , 'retainers' , 'rainsuits' , 'intrusion' , 'absolutely' , 'especially', 'incredibly' , 'understand' , 'appreciate' , 'compliment' , 'accelerate' , 'additional' , 'activities' , 'admiringly' , 'admissilbe', 'rotisserie' , 'rotational' , 'runestones' , 'satellites' , 'irrational' , 'triangular' , 'tailgaters' , 'sunglasses' , 'stringline' , 'sidestreet', 'renditions' , 'litigation' , 'interested' , 'gentleness' , 'grassroots' , 'editorials' , 'dreariness' , 'disastrous' , 'adrenaline' , 'understand', 'absorbingly' , 'absorbition' , 'application' , 'affirmation' , 'apologizing' , 'approaching' , 'applaudable' , 'appalachian' , 'barbershops' , 'battleships', 'badmouthing' , 'bibliograph' , 'bookkeeping' , 'boilerworks' , 'certificate' , 'certainness' , 'chainmaking' , 'chairperson' , 'defenseless' , 'decomposite', 'exceedingly' , 'filmography' , 'hairbrushes' , 'hushpuppies' , 'incessantly' , 'pincushions' , 'prospective' , 'reorganzied', 'abstractions' , 'barrelhouses' , 'basketmaking' , 'compartments' , 'computerlike' , 'concatenated' , 'complimented' , 'encyclopedia' , 'incontinuity' , 'neoclassical', 'neurosurgeon' , 'precertified' , 'uncultivated' , 'unprovokable' , 'unremorseful' ]
#lstModifiedWords = []
#lstHistoryGuess = []
#intLives = 0
strWord = ''
strWordList = []
strLetter = ''
def split(word): 
    return [char for char in word]  
def pickword(intLength):
    global lstSecretWords
    lstModifiedWords = []
    global strWord 
    global strWordList
    k = 0
    while k < len(lstSecretWords):
        if len(lstSecretWords[k]) == intLength:
            lstModifiedWords.append(lstSecretWords[k])
        k += 1
    strWord = random.choice(lstModifiedWords)
    strWordList = split(strWord)
def playHangman():
    global lstSecretWords
    #global lstModifiedWords
    global strWord 
    global strWordList 
    intUserLength = 0    
    intLives = 0
    strLetter = ''
    lstHistoryGuess = []
    print("\n\n\n\n\n----------------Hello and welcome to the hangman game!----------------")
    print("------------We have words from 2 letters to 12 letters long------------")
    print('How many letters would you like to guess?')
    while (intUserLength <= 1 or intUserLength > 12):
        intUserLength = int(input())
        if intUserLength <= 1 or intUserLength > 12:
            print("Sorry that length is not available, please choose again.")
    intLives = intUserLength + 6
    pickword(intUserLength)
    strHypenWordList = []
    intHypen = 0
    while intHypen < len(strWord):
        strHypenWordList.append('-')
        intHypen += 1
    intL = 3
    print(*strHypenWordList)
    while strHypenWordList != strWordList:
        print("\n\nYou have", str(intLives), 'guesses remaining.\n')
        strLetter = input("\nWhat letter would you like to guess? ").lower()
        if strLetter in lstHistoryGuess:
            print('You\'ve already made that guess.')
            #intLives += 1
        intCount = strWord.count(strLetter)
        for i, strValue in enumerate(strWordList):
            if strValue == strLetter:
                print('I found your letter(s).')
                strHypenWordList[i] = strLetter
        if (strLetter not in strWordList) and strLetter not in lstHistoryGuess:
                intLives -= 1
                if intLives == 0:
                    print('You are out of guesses.')
                    print("The word was: ", strWord)
                    print("Would you like to play again?")
                    strUserPlayAgain = input().lower()
                    if strUserPlayAgain == 'y' or strUserPlayAgain == 'yes':
                        intUserLength = 0
                        playHangman()
                    else:
                        print("      Thanks for playing")
                    break                
        lstHistoryGuess.append(strLetter)
        print(*strHypenWordList)#, sep=",")
        print('You have guessed: ', *lstHistoryGuess) #, '\n')
    if strHypenWordList == strWordList:
        print("\n----------------Congratulations on winning!----------------")
        print('You had', intLives, 'guesses remaining.')
        print('Would you like to play again?')
        strUserPlayAgain = input().lower()
        if strUserPlayAgain == 'y' or strUserPlayAgain == 'yes':
            intUserLength = 0
            intLives = 0
            playHangman()
        else:
            print("      Thanks for playing!  ")
playHangman()
