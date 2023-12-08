def wordToDigit(word):
    digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    text = ""
    for c in word:
        text += c
        if text in digits:
            return digits[text]
    return " "


def findFirst(word):
    digit = " "
    for index, c in enumerate(word):
        if c.isdigit():
            digit = c
        else:
            digit = wordToDigit(word[index:])
        if digit != " ":
            return str(digit)
    

def findLast(word):
    digit = " "
    for index, c in enumerate(word[::-1]):
        if c.isdigit():
            digit = c 
        else:
            digit = wordToDigit(word[-(index+1):])
        if digit != " ":
            return str(digit)

def findFirst1(word):
    for c in word:
        if c.isdigit():
            digit = c
            return digit
def findLast1(word):
    for c in word[::-1]:
        if c.isdigit():
            digit = c
            return digit
def resultat():
    sum1 = 0
    sum2 = 0
    with open("Day 1/input.txt","r",encoding="utf-8") as f:
        for index ,line in enumerate(f):
            sum1 += int(findFirst1(line)+ findLast1(line))
            #print(index,findFirst(line),findLast(line))
            sum2 += int(findFirst(line) + findLast(line))
    print(sum1)
    print(sum2)
resultat()