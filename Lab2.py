import numpy as np
import re

kwdlst = ["auto", "break", "case", "char", "levelst", "leveltinue", "default", "do",
          "double", "else", "enum", "extern", "float", "for", "goto", "if",
          "int", "long", "register", "return", "short", "signed", "sizeof", "stastic",
          "struct", "switch", "typedef", "union", "unsigned", "void", "else-if", "while"]

path = "test.cpp"
f = open(path, "r")

kwd_len = len(kwdlst)
num0, flag_if, flag_else_if, num_if_else, num_if_else_if_else = 0, 0, 0, 0, 0
num0s, sentences = [], []
x_len = 999
count = np.zeros(kwd_len, dtype=int)

line = f.readline()
line = line[:-1]

while line:
    line = f.readline()
    line = line[:-1]
    line = line.replace("else if", "else-if")
    x = re.split(' |\(|\;|\\t|\:|\{|\/\/', line)
    for i in x:
        for j in range(kwd_len):
            if i == kwdlst[j]:
                if i == "switch":
                    num0s.append(num0)
                    num0 = 0
                if i == "case":
                    num0 += 1
                count[j] += 1
    for i in x:
        if i == "if" or i == "else" or i == "else-if":
            sentences.append(x)
            continue
f.close()
num0s.append(num0)

sumres = 0
for i in range(kwd_len):
    if count[i] != 0:
        sumres += count[i]
        if (i == 30):
            sumres += count[i]
for i in sentences:
    if len(i) < x_len:
        x_len = len(i)
for j in range(x_len):
    for i in sentences:
        if i[j] == "if":
            flag_if = 1
        if i[j] == "else-if":
            flag_else_if = 1
        if i[j] == "else":
            if flag_else_if == 1:
                num_if_else_if_else += 1
            elif flag_if == 1:
                num_if_else += 1
            flag_else_if = 0
            flag_else = 0

level = int(input("level of stastic (from 1 to 4): "))
if level > 1 or level == 1:
    print("sum : ", sumres)
    if level > 2 or level == 2:
        print(kwdlst[25], " num : ", count[25])
        print("case num", num0s[1:3])
        if level > 3 or level == 3:
            print("if-else num:", num_if_else)
            if level == 4:
                print("if-elseif-else num:", num_if_else_if_else)
