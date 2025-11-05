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
from collections import defaultdict
N = 10

with open("C:\Coding\Esame\superenalotto\estrazioni.txt", "r") as f:
    matrice = [riga.strip().split() for riga in f]

limite = input('Inserisci anno limite: ')
lim = int(limite[-2:])
matrix = []

for i in range(2, len(matrice)) :
    if int(matrice[i][0][-2:]) >= lim:
        matrix.append(matrice[i])
    else:
        break
numeri = {f"{i:02}" for i in range(1, 91)}
numeriEstratti = set()
for riga in matrix:
    for i in range(2,8):
        if riga[i] not in numeriEstratti:
            numeriEstratti.add(riga[i])

numeriBuoni = numeri - numeriEstratti
if len(numeriBuoni) >= 6:
    estrazione = random.sample(list(numeriBuoni), 6)
elif len(numeriBuoni) != 0:
    estrazione = list(numeriBuoni)
else:
    estrazione = []
print('schedina dopo il punto 1: ', estrazione)
#2
print(f'punto 2, provo a cercare tra gli {N} meno presenti...')
if len(estrazione) < 6:
    frequenza = defaultdict(int)
    numeriFrequenzaMinore = set()
    for riga in matrix:
        for i in range(2,8):
            frequenza[riga[i]] += 1
    print(frequenza)
    for _ in range(N):
        minValue = min(frequenza, key = lambda x:  frequenza[x])
        numeriFrequenzaMinore.add(minValue)
        frequenza.pop(minValue)
    
    
    for _  in range(6 - len(estrazione)):
        num = random.choice(list(numeriFrequenzaMinore))
        coOccorrenza = False
        if estrazione == []:
            print(f'{num} mai estratto insieme ad {estrazione}')
            estrazione.append(num)
        
        else:
            for riga in matrix:
                if coOccorrenza: break
                for el in estrazione:
                    if el in riga[2:8] and num in riga[2:8]:
                        print(f'numero {num} già presente insieme a {el}')
                        coOccorrenza = True
                        break
            if not coOccorrenza:    
                print(f'numero {num} mai estratto insieme a {estrazione}')
                estrazione.append(num)
                
                
        numeriFrequenzaMinore.remove(num)
        print(f'schedina corrente {estrazione}')
#32006

if len(estrazione) != 6:
    print(f'schedina non conclusa, mancano {6 - len(estrazione)} per completarla, concludo con la generazione random')
    for _ in range(0, (6 - len(estrazione))):
        estrazione.append(random.choice(list(numeri - set(estrazione))))
print('schedina finale: ', estrazione)