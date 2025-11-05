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
from collections import defaultdict
def getPrenotatiDict(file):
    with open(file, 'r') as f:
        fileList = [line.strip() for line in f]
    d =defaultdict(int)
    for user in fileList:
        d[user[:6]] = user
    return d

def getConsegneSet(file):
    s = set()
    with open(file, 'r') as f:
        fileList = [line.strip() for line in f if line.strip()]

        for user in fileList:
            for i in range(len(user)):
                 if user[i] == 'S' or user[i] == 's':
                    s.add(user[i+1:i+7])
    return s

dict1 = getPrenotatiDict('prenotati_appello1.txt')
dict2 = getPrenotatiDict('prenotati_appello2.txt')
dict3 = getPrenotatiDict('prenotati_appello3.txt')

set1 = getConsegneSet('consegne_appello1.txt')
set2 = getConsegneSet('consegne_appello2.txt')
set3 = getConsegneSet('consegne_appello3.txt')

assenti1 = dict1.keys() - set1
assenti2 = dict2.keys() - set2
assenti3 = dict3.keys() - set3

print(f'assenti al primo appello:')
for assente in iter(assenti1):
    print(dict1[assente])
print(f'in totale ci sono {len(assenti1)} assenti')
print('assenti al second appello')
for assente in iter(assenti2):
    print(dict2[assente])
print(f'in totale ci sono {len(assenti2)} assenti')
for assente in iter(assenti3):
    print(dict3[assente])   
print(f'in totale ci sono {len(assenti3)} assenti') 

print('matricole degli studenti che non si sono presentati a nessun appello: ')
for assente in iter(assenti1.intersection(assenti2).intersection(assenti3)):
    print(int(assente))