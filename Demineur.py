import random
import os

taille = 10
nombreDeMines = 30


mines = [(random.randint(0, taille-1), random.randint(0, taille-1))
         for i in range(nombreDeMines)]
grille = [['▩' for i in range(taille)]for i in range(taille)]
perdu = False


def Autour(l, c):
    cpt = 0
    if l != 0:
        if (l-1, c) in mines:
            cpt += 1
        if c != 0:
            if(l-1, c-1) in mines:
                cpt += 1
        if c != taille-1:
            if (l-1, c+1) in mines:
                cpt += 1
    if c != 0:
        if (l, c-1) in mines:
            cpt += 1
        if l != taille-1:
            if (l+1, c-1) in mines:
                cpt += 1
    if l != taille-1:
        if (l+1, c) in mines:
            cpt += 1
        if c != taille-1:
            if (l+1, c+1) in mines:
                cpt += 1
    if c != taille-1:
        if (l, c+1) in mines:
            cpt += 1
    return cpt


def Alentours(l, c):
    liste = []
    if l != 0:
        liste.append((l-1, c))
        if c != 0:
            liste.append((l-1, c-1))
        if c != taille-1:
            liste.append((l-1, c+1))
    if c != 0:
        liste.append((l, c-1))
        if l != taille-1:
            liste.append((l+1, c-1))

    if l != taille-1:
        liste.append((l+1, c))
        if c != taille-1:
            liste.append((l+1, c+1))
    if c != taille-1:
        liste.append((l, c+1))
    return liste


def decouvrir(l, c, n):
    if grille[l][c]=="▩":
        global perdu
        if n == "y":
            grille[l][c]="◎"
        else : 
            if (l, c) in mines:
                grille[l][c]="◎"
                perdu = True
            else:
                if Autour(l, c) == 0:
                    grille[l][c] = "▢"
                    for i in Alentours(l,c):
                        decouvrir(i[0],i[1],"n")
                else :
                    grille[l][c] = Autour(l,c)


def afficher():
    for i in grille:
        print(str(i).replace("'","").replace(',','').replace('[','').replace(']',''))

def jouer():
    global perdu
    while not perdu:
        os.system('clear')
        afficher()
        l=int(input("ligne : "))
        c=int(input("colonne : "))
        chx = input("mine ? (y or n) : ")
        decouvrir(l-1,c-1,chx)
    for l in range(taille):
        for c in range(taille):
            decouvrir(l,c,"n")
    os.system('clear')
    afficher()
    print("perdu")

jouer()