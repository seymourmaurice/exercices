# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:06:43 2021

@author: Networks
"""




# # " choix du plus grand nombre"

def choixduplusgrand():
    a=int(input("entrer nombre a :"))
    b=int(input("entrer nombre b :"))
    c=int(input("entrer nombre c :"))



    if a > b and a > c:
        print("a est le plus grand nombre") 
    elif b > a and b > c:
        print("b est le plus grand nombre")
    elif a==b==c :
        print("les 3 nombres sont egaux")
    else:
        print("c est le plus grand nombre")
    
######################################################################
    
#pair ou non?
def pairounon():
    a=int(input("entrer nombre a definir :"))

    if (a%2)==0:
        print("le nombre",a,"est paire")
    else:
        print("le nombre",a,"est impaire")
        
#######################################################################

#boucles nombres paire jusque a 100
def jusqua100():
    a=int(input("entrer nombre depart :"))
    if (a%2)== 0:
        while a<100:
            a =a+2
            print(a)
    else: print("chiffre donné impaire!!"),jusqua100()
    

#######################################################################

# #detection voyelle
def voyelledetection():
    a = str(input("entrer la lettre: "))

    voyelle = ("a","e","i","o","u","y")

    if a in voyelle :
        print(a, "est une voyelle")
    else:
        print(a, "n'est pas une voyelle"), voyelledetection()
   


#######################################################################  
  
# #table de ?

def tablede():
    n=int(input("entrer le nombre a multiplier: "))
    b=1
   
    while b <10:
        print(n,"x",b,"=",(n*b))
        b=b+1
#######################################################################  
def appeldefonctions():
    appel=input("""appel fonction:\n
            choix du plus grand:1 \n
            chiffre pair ou non:2 \n
            chiffre paire <> 100 :3 \n
            detection de voyelle:4 \n
            table de ? :5 \n
  Fonction demandé: """)
    if appel == "1" :
        choixduplusgrand()
    elif appel == "2":
        pairounon()
    elif appel == "3":
      jusqua100()
    elif appel == "4":
        voyelledetection()
    elif appel == "5":
        tablede()
    else:
        print("appeler une fonction valable"), appeldefonctions()
        
appeldefonctions()