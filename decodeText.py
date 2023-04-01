from time import sleep
char, key, inputt, index, encode=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '], 1, input('Type your text here: '), 0, ''
for textchar in inputt:
    for charr in char:
        if charr == textchar:
            rindex = index
        else:
            index += 1
    if rindex-key < 0:
        rindex+=27
    index = 0
    encode = encode + char[rindex-key]
    key += 1
print(encode); sleep(10)
