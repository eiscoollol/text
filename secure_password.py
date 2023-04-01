import os as s, time as t, random as r
def passworgenerator(n):
    listforpass = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!@#$%&?/=*']
    passw = ''
    for secupass in range(n):
        compuchoice = r.choice(listforpass)
        if compuchoice == 'abcdefghijklmnopqrstuvwxyz' or compuchoice == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            passw = compuchoice[r.randint(0, 25)] + passw
        else:
            passw = compuchoice[r.randint(0,9)] + passw
    print('Your auto-generated password is:', passw)
passworgenerator(int(input('How long is the password?: ')))
while True:
    choice = input('Again? (y for yes, n for no): ')
    if choice == 'n' or choice == 'N':
        break
    h0wI0n9 = int(input('How long is the password?: '))
    if choice == 'y' or choice == 'Y':
        if s.name == 'nt':
            s.system('cls')
            loadtext = 'In progress'
            for load in range(r.randint(10, 20)):
                print(loadtext)
                t.sleep(0.5)
                if loadtext != 'In progress...':
                    loadtext = loadtext + '.'
                else:
                    loadtext = 'In progress'
                s.system('cls')
            passworgenerator(h0wI0n9)
        else:
            s.system('clear')
            loadtext = 'In progress'
            for load in range(r.randint(10, 20)):
                print(loadtext)
                t.sleep(0.5)
                if loadtext != 'In progress...':
                    loadtext = loadtext + '.'
                else:
                    loadtext = 'In progress'
                s.system('clear')
            passworgenerator(h0wI0n9)
    elif choice == 'n' or choice == 'N':
        break
    else:
        if s.name == 'nt':
            s.system('cls')
            print('Invalid value!')
            t.sleep(1)
            s.system('clear')
        else:
            s.system('clear')
            print('Invalid value!')
            t.sleep(1)
            s.system('clear')
    t.sleep(5)