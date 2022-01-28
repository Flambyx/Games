import random
import os
import time
from pynput import keyboard

#options
K = 40
delai = 0.05
acc = 1
repr = "@"

perdu = False
grille = [[" " for i in range(K+1)]for j in range(K+1)]
grille[0],grille[K] = ['#' for i in range(K+1)],['#' for i in range(K+1)]
for i in range(K+1):
    grille[i][0],grille[i][K]="#","#"
direction = "right"
snake = [(K//2,K//2+1),(K//2,K//2+1),(K//2,K//2)]
cpt = 0

def roll(liste):
    for i in range(len(liste)-1,0,-1):
        liste[i]=liste[i-1]

def avance():
    global perdu
    global delai
    global cpt
    grille[snake[-1][0]][snake[-1][1]]=" "
    next = snake[0]
    roll(snake)
    if direction == "right":
        new = (next[0],next[1]+1)
        if grille[new[0]][new[1]] == "O":
            snake.insert(0,new)
            delai*=acc
            cpt+=1
            pomme()
        elif grille[new[0]][new[1]] == "#" or grille[new[0]][new[1]] == repr:
            perdu = True
        snake[0] = new
    if direction == "up":
        new = (next[0]-1,next[1])
        if grille[new[0]][new[1]] == "O":
            snake.insert(0,new)
            delai*=acc
            cpt+=1
            pomme()
        elif grille[new[0]][new[1]] == "#" or grille[new[0]][new[1]] == repr:
            perdu = True
        snake[0] = new
    if direction == "down":
        new = (next[0]+1,next[1])
        if grille[new[0]][new[1]] == "O":
            snake.insert(0,new)
            delai*=acc
            cpt+=1
            pomme()
        elif grille[new[0]][new[1]] == "#" or grille[new[0]][new[1]] == repr:
            perdu = True
        snake[0] = new
    if direction == "left":
        new = (next[0],next[1]-1)
        if grille[new[0]][new[1]] == "O":
            snake.insert(0,new)
            delai*=acc
            cpt+=1
            pomme()
        elif grille[new[0]][new[1]] == "#" or grille[new[0]][new[1]] == repr:
            perdu = True
        snake[0] = new

def afficher():
    for i in snake :
        grille[i[0]][i[1]] = repr
    for i in grille:
        print(str(i).replace("'","").replace(',','').replace('[','').replace(']',''))
    print("points : ",cpt)

def pomme():
    p = (random.randint(1,K-1),random.randint(1,K-1))
    while(grille[p[0]][p[1]] == repr):
        p = (random.randint(1,K-1),random.randint(1,K-1))
    grille[p[0]][p[1]] = 'O'

def on_press(key):
    global direction
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'left', 'right']:
        if (direction == 'up' and k == 'down') or (direction == 'down' and k == 'up') or (direction == 'left' and k == 'right') or (direction == 'right' and k == 'left'):
            pass
        else:
            direction = k
        return False

def jouer():
    pomme()
    while not perdu :
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        avance()
        afficher()
        time.sleep(delai)
        os.system('clear')
    afficher()
    print("perdu")
    

jouer()