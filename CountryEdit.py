file = open("D:\\Coding\\Python Development\\country2.txt", "r")

text = file.readlines()
file.close()
text2 = []
for x in text:
    if x[-1] == '\n':
        text2.append('(' + x[:-1] + '),')
    else:
        text2.append('(' + x + '),')

for x in text2:
    print(x)

file = open("D:\\Coding\\Python Development\\country2.txt", "w")
for x in text2:
    file.write(x + '\n')

file.close()
