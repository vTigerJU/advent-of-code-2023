
maxCubes = {"red":12,"green":13,"blue":14}

def checkDraw(cubes):
    colors = cubes.split(",")
    for color in colors:
        temp = color.split()
        if maxCubes[temp[1]] < int(temp[0]):
            return False
    return True

def taskOne():
    sum = 0
    with open("Day 2/input.txt","r",encoding="utf-8") as f:
        for line in f:   
            game = line.split(":")
            gameId = game[0].split()[1]
            draws = game[1].split(";")
            for i in draws:
                checker = checkDraw(i)
                if checker == False:
                    break
            if checker:
                sum += int(gameId)
    print(sum)

def checkDraws(draws):
    minCubes = dict()#{"red":0,"green":0,"blue":0}
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            temp = color.split()
            if temp[1] not in minCubes:
                minCubes[temp[1]] = int(temp[0])
            if minCubes[temp[1]] < int(temp[0]):
                minCubes[temp[1]] = int(temp[0])
    result = 1
    for x in minCubes.values():
        result = result *x 
    return result
                

def taskTwo():
    sum = 0
    with open("Day 2/input.txt","r",encoding="utf-8") as f:
        for line in f:   
            game = line.split(":")
            gameId = game[0].split()[1]
            draws = game[1].split(";")
            sum += checkDraws(draws)
    print(sum)

taskTwo()
                
           
