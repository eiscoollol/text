import time as tm
print('Hello, this is a text changer')
txt = input('Type the text you want to change:\n')
while True:
    funcno = int(input('Type which function you want:\n1.Uppercase\n2.Lowercase\n3.Replace word (or characters)\n4.Reverse all characters\' position\n5.Swaps all characters case\n6.Stop\n'))
    if funcno<=6 and funcno>=1:
        if funcno == 1:
            txt = txt.upper()
            print(txt)
        elif funcno == 2:
            txt = txt.lower()
            print(txt)
        elif funcno == 3:
            wantedword, replaceword = input('Type the word you need to replace:\n'), input('Type the word you want to replace:\n')
            txt = txt.replace(wantedword,replaceword)
            print(txt)
        elif funcno == 4:
            txt = txt[::-1]
            print(txt)
        elif funcno == 5:
            txt = txt.swapcase()
            print(txt)
        elif funcno == 6:
            break
    else:
        print('Invalid value, please try again!')
        tm.sleep(0.5)
