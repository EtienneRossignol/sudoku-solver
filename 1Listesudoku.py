from __future__ import division
from lycee import *
from Tkinter import *
from time import*

def OK (rien):
    global STOP,coups,Listechainecaractere
    coups = 0
    STOP = False
    Listechainecaractere = []
    creationchainecaractere()
    go()
def go():
    global STOP,coups,Listechainecaractere
    transformationderien()
    verifSTOP()
    block()
    #if coups > 8 : valeurseules()
    #if 18 < coups < 22 :valeurseules2()
    Remplacer()
    #valeursaunendroit()
    verifblock()
    coups =coups +1
    affich()
    if STOP == False:fen.after(1,go)
    else:print coups
def creationchainecaractere ():
    global Listechainecaractere
    #fichier = open("D:/Mes Documents/Etienne/Sudok1.txt", 'r')
    #for i in fichier:
    #    i=list(i)
#        for l in i:
 #           if l.replace('\n',"") != "":Listechainecaractere.append((l.replace('\n',"")).replace(" ",""))
    for i in range(81):
        Listechainecaractere.append(ListeEntry[i].get())
     #   ListeEntry[i].delete(0,END)
     #   ListeEntry[i].insert(END,Listechainecaractere[i])
     #   if len(ListeEntry[i].get()) == 1 :ListeEntry[i].config(fg  = 'BLUE')
    #fichier.close()
def transformationderien():
    for i in range (81):
        res = valeurspossibles(Listechainecaractere[i])
        Listechainecaractere[i] = res

def valeurspossibles(valeur):
    resultat = valeur
    if valeur == "" :
        resultat = "123456789"
    else:
        for i in range (9):
            if valeur == str(i+1): resultat = Listechiffreenlettre[i]
    return resultat

def verifSTOP ():
    global STOP,coups
    chaine = ""
    for i in range (81) :
        chaine =chaine + Listechainecaractere[i]
    if len (chaine) == 81 or coups == 25: STOP = True
def block ():
    global listeblock
    listeblock = []
    for i in range (9):
        chaineL = []
        chaineC = []
        chaineLnb = []
        chaineCnb = []
        for J in range (9):
            chaineL.append(Listechainecaractere[i*9+J])
            chaineLnb.append(i*9+J)
            chaineC.append(Listechainecaractere[i+J*9])
            chaineCnb.append(i+J*9)
        listeblock.append(chaineL)
        listeblock.append(chaineC)
        Listecoordonee.append(chaineLnb)
        Listecoordonee.append(chaineCnb)
    for X in range (3):
        for i  in range (3):
            chaineCarre =[]
            chaineCarrenb =[]
            for J in range(3):
                for K in range (3):
                    chaineCarre.append(Listechainecaractere[K+J*9+i*3+X*27])
                    chaineCarrenb.append(K+J*9+i*3+X*27)
            listeblock.append(chaineCarre)
            Listecoordonee.append(chaineCarrenb)
def valeurseules():
    global listeblock
    for nb in range (9):
        for nb2 in range (9):
            for PI in range (27):
                passa = 0
                val = []
                for i in range (9):
                    if str (nb)+str(nb2)  == listeblock[PI][i]:
                        passa = passa + 1
                        val.append(i)
                    if passa == 2:
                        for fe in range (9):
                                if Listechainecaractere[Listecoordonee[PI][fe]] != str(nb)+str(nb2):
                                    Listechainecaractere[Listecoordonee[PI][fe]] = (Listechainecaractere[Listecoordonee[PI][fe]].replace(str(nb),"")).replace(str(nb2),"")



def valeurseules2():
    for bloc in range (27):
        for cas1 in range (9):
            for cas2 in range (9):
                for cas3 in range (9):
                    if cas1 != cas2 != cas3 != cas1 :
                        chaine = listeblock[bloc][cas1]+listeblock[bloc][cas2]+listeblock[bloc][cas3]
                        chaine2 = ''
                        for rang in range (len(chaine)):
                            for i in range (9):
                                if Listechiffreenlettre[i] in chaine[rang]:chaine2 = chaine2+ str(i+1)
                                else : chaine2 = chaine2 + chaine[rang]
                        cont = 0
                        chaine3 = ''
                        for car1 in range (9):
                            if str(car1 +1) in chaine2 :
                                cont = cont + 1
                                chaine3 = chaine3+ str(car1 + 1)
                        if cont == 3 :
                            for remplacer in range(9):
                                if remplacer != cas1 and remplacer != cas2 and remplacer != cas3:
                                    for j in range(3):
                                        Listechainecaractere[Listecoordonee[bloc][remplacer]] = Listechainecaractere[Listecoordonee[bloc][remplacer]].replace(chaine3[j],"")
def Remplacer():
    global listeblock
    for PI in range (27):
        for i in range (9):
            chainelisteblock = ','.join(listeblock[PI])
            if Listechiffreenlettre[i] in chainelisteblock:
                for PO in range (9):
                    Listechainecaractere[Listecoordonee[PI][PO]]=Listechainecaractere[Listecoordonee[PI][PO]].replace(str(i+1),"")

def valeursaunendroit():
    global Listechainecaractere
    for bloc in range (27):
        for nb1 in range (9):
            for nb2 in range (9):
                if nb1 != nb2:
                    if not Listechiffreenlettre[nb1] in listeblock[bloc] and not Listechiffreenlettre[nb2] in listeblock[bloc]:
                        chainelisteblock = ','.join(listeblock[bloc])
                        if chainelisteblock.count(str(nb1+1)) == 2 and chainelisteblock.count(str(nb2+1))==2:
                            memecase = 0
                            coordonnee_de_la_case_a_changer = []
                            for recherchenb in range(9):
                                if str(nb1+1) in listeblock[bloc][recherchenb] and str(nb2+1) in listeblock[bloc][recherchenb]:
                                    memecase=memecase+1
                                    coordonnee_de_la_case_a_changer.append(recherchenb)
                            if memecase == 2:
                                for detruire in range(2):
                                    Listechainecaractere[Listecoordonee[bloc][coordonnee_de_la_case_a_changer[detruire]]]=str(nb1+1)+str(nb2+1)
def verifblock():
    for PI in range (27):
        for i in range (9):
            chainelisteblock = ','.join(listeblock[PI])
            if chainelisteblock.count(str(i+1)) == 1 and not Listechiffreenlettre[i] in chainelisteblock:
                for PO in range (9):
                    if str(i+1) in Listechainecaractere[Listecoordonee[PI][PO]]:Listechainecaractere[Listecoordonee[PI][PO]] = str(i+1)

def affich ():
    for i in range (81):
        if len(Listechainecaractere[i]) == 1:ListeEntry[i].config(bg  = 'grey')
        if len(Listechainecaractere[i]) > 1 :ListeEntry[i].config(bg  = 'red')
        if len(Listechainecaractere[i]) < 1 :ListeEntry[i].config(bg  = 'PURPLE')
    verifregle()
    for S in range(81):
        for i in range (9):
            if Listechiffreenlettre[i] in Listechainecaractere[S]:Listechainecaractere[S] = str(i+1)
    for i in range (81):
        ListeEntry[i].delete(0,END)
        ListeEntry[i].insert(END,Listechainecaractere[i])

def verifregle():
    for i in range (27):
        for lettre in range(9):
            if  (','.join(listeblock[i])).count(Listechiffreenlettre[lettre]) > 1:
                for PLIS in range (9): ListeEntry[Listecoordonee[i][PLIS]].configure(bg = 'purple')
x,y = 0,0
STOP = False
ListeEntry=[]
Listechiffreenlettre = ["A","B","C","D","E","F","G","H","I"]
Listecoordonee = []
fen = Tk()
fen.geometry("440x260")
fen.title("Sudoku")
fen.resizable(width = False, height=False)
C= Canvas(fen, height=5000,width=5000)
C.place(x=0,y=0)
for i in range (9):
    for j in range(9):
        ListeEntry.append(Entry(fen, width = 4, fg = 'BLACK'))
        ListeEntry[i*9+j].place(x=x,y=y)
        x=x+50
    x=0
    y=y+30
C.create_line(140,0, 140,500)
C.create_line(290,0, 290,500)
C.create_line(0,85, 600,85)
C.create_line(0,175, 600,175)
fen.bind_all('<Return>', OK)
fen.mainloop()