# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
import random
playing = True
gameNumber = 1
ALFABETO = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
wins = 0
losses = 0
def getListaParole(file1):
    with open(file1, 'r') as f:
        parole = [line.strip() for line in f if line.strip()]
        return parole
sceltaDict = {
    1: 'facile',
    2: 'medio',
    3: 'difficile'
}
while playing:
    alfabetoGame = ALFABETO.copy(   )
    points = 10
    guessed = False
    scelta = random.randint(1,3)
    print(f'partita numero {gameNumber}')
    print(f'il bot seleziona la difficoltà: {sceltaDict[scelta]}')
    if scelta == 1:
        parole = getListaParole(r'C:\Coding\Esame\akinator\facile.txt')
    elif scelta == 2:
        parole = getListaParole(r'C:\Coding\Esame\akinator\medio.txt')
    elif scelta == 3:
        parole = getListaParole(r'C:\Coding\Esame\akinator\difficile.txt')
    parola = random.choice(parole)
    gameParola = ['_' for _ in range(len(parola))]
    while points > 0 and guessed == False:
        print(f'Punti {points} \nla parola da indovinare è {' '.join(gameParola)}')
        guess = random.choice(list(alfabetoGame))
        alfabetoGame.remove(guess)
        print(f'    la lettera scelta dal bot é: {guess}')

        if guess not in parola:
            print(f'lettera {guess} non presente')

        if guess in parola:
            for i in range(len(parola)):
                if parola[i] == guess:
                    gameParola[i] = guess
            print(f'    lettera {guess} presente: {' '.join(gameParola)}')
        
        if '_' not in gameParola:
            print(f'complimenti il bot ha vinto la parola {parola.upper()} è stata indovinata correttamente')
            guessed = True
            wins +=1
        points -= 1
    if guessed == False:
        print(f'il bot non ha vinto la parola era: {parola.upper()}')
        losses += 1

    gameNumber +=1

    failed = False
    while True:
        if failed == False:
            replayStatus = input('Vuoi continuare a giocare [S/N]? ')
        
        if replayStatus == 'S':
            break
        elif replayStatus =='N':
            playing = False
            print(f'SESSIONE TERMINATA\nil bot ha vinto {wins} partita/e\nil bot ha perso {losses} partita/e')
            break
        else:
            failed = True
            replayStatus = input('[S/N]: ')
            
        



    
    