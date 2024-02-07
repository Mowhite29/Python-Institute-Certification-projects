
def print_display(output):
    
     if output == go:
         print(
        "","".join(display[0][0:3]),  "".join(display[0][3:6]), "".join(display[0][6:9]), "".join(display[0][9:12]), "".join(display[0][12:15]), "".join(display[0][15:18]), "".join(display[0][18:21]), "".join(display[0][21:24]), "".join(display[0][24:27]), "".join(display[0][27:30]),"\n",
        "".join(display[1][0:3]), "".join(display[1][3:6]), "".join(display[1][6:9]), "".join(display[1][9:12]), "".join(display[1][12:15]), "".join(display[1][15:18]), "".join(display[1][18:21]), "".join(display[1][21:24]), "".join(display[1][24:27]), "".join(display[1][27:30]),"\n",
        "".join(display[2][0:3]), "".join(display[2][3:6]), "".join(display[2][6:9]), "".join(display[2][9:12]), "".join(display[2][12:15]), "".join(display[2][15:18]), "".join(display[2][18:21]), "".join(display[2][21:24]), "".join(display[2][24:27]), "".join(display[2][27:30]),"\n",
        "".join(display[3][0:3]), "".join(display[3][3:6]), "".join(display[3][6:9]), "".join(display[3][9:12]), "".join(display[3][12:15]), "".join(display[3][15:18]), "".join(display[3][18:21]), "".join(display[3][21:24]), "".join(display[3][24:27]), "".join(display[3][27:30]),"\n",
        "".join(display[4][0:3]), "".join(display[4][3:6]), "".join(display[4][6:9]), "".join(display[4][9:12]), "".join(display[4][12:15]), "".join(display[4][15:18]), "".join(display[4][18:21]), "".join(display[4][21:24]), "".join(display[4][24:27]), "".join(display[4][27:30])
        )


def one(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][2+n]='#'
    display[1][2+n]='#'
    display[2][2+n]='#'
    display[3][2+n]='#'
    display[4][2+n]='#'
    
def two(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][2+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][0+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'
    
def three(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][2+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][2+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'
    
def four(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][2+n]='#'
    display[1][0+n]='#'
    display[1][2+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][2+n]='#'
    display[4][2+n]='#'
    
def five(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][0+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][2+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'
    
def six(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][0+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][0+n]='#'
    display[3][2+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'
    
def seven(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][2+n]='#'
    display[2][1+n]='#'
    display[3][1+n]='#'
    display[4][1+n]='#'
    
def eight(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][0+n]='#'
    display[1][2+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][0+n]='#'
    display[3][2+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'
    
def nine(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][0+n]='#'
    display[1][2+n]='#'
    display[2][0+n]='#'
    display[2][1+n]='#'
    display[2][2+n]='#'
    display[3][2+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'

def zero(place):
    n = 0
    place += 1
    if place == 1:
        n = 0
    elif place == 2:
        n = 3
    elif place == 3:
        n = 6
    elif place == 4:
        n = 9
    elif place == 5:
        n = 12
    elif place == 6:
        n = 15 
    elif place == 7:
        n = 18
    elif place == 8:
        n = 21
    elif place == 9:
        n = 24
    elif place == 10:
        n = 27
    
    display[0][0+n]='#'
    display[0][1+n]='#'
    display[0][2+n]='#'
    display[1][0+n]='#'
    display[1][2+n]='#'
    display[2][0+n]='#'
    display[2][2+n]='#'
    display[3][0+n]='#'
    display[3][2+n]='#'
    display[4][0+n]='#'
    display[4][1+n]='#'
    display[4][2+n]='#'
  
 
go = ""
n = ""
display = []

for i in range(5):
    row = [" " for i in range(31)]
    display.append(row)
 
number = input(str("enter number "))

length = len(number)

while length != 0:
    for i in range(len(number)):
    
        n = 0
    
        if number[i] == "1":
            one(i)
            length -= 1
        elif number[i] == "2":
            two(i)
            length -= 1
        elif number[i] == "3":
            three(i)
            length -= 1
        elif number[i] == "4": 
            four(i)
            length -= 1
        elif number[i] == "5":
            five(i)
            length -= 1
        elif number[i] == "6":
            six(i)
            length -= 1
        elif number[i] == "7":
            seven(i)
            length -= 1
        elif number[i] == "8":
            eight(i)
            length -= 1
        elif number[i] == "9":
            nine(i)
            length -= 1
        elif number[i] == "0":
            length -= 1
            zero(i)
            
else:
    print_display(go)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    