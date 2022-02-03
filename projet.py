import numpy as np
import random
import matplotlib.pyplot as plt

#-----------------Apprentissage des paramètres d’un modèle à partir de données----------

#qst1
#   s i r 
# s . . .
# i . . . 
# r . . .
def estim_prob() : 
    matrice=np.array([[2/3,1/3,0],[0,5/6,1/6],[0,0,1]])
    return matrice
#qst2
#Construction de la matrice de transition
def proba_transition(data) : 
    nb_lignes=len(data)
    nb_colonnes=len(data[0])
    s_s=0 #nombre ou l'individu était sain et resté sain
    s_i=0 #nombre ou l'individu était sain et devenu infecté
    i_i=0 #nombre ou l'individu était infecté et resté infecté
    i_r=0 #nombre ou l'individu était infecté et devenu guerri
    for i in range(0,nb_lignes):#on parcourt les états de chaque individu
    
        for j in range(1,nb_colonnes):
            if (data[i][j-1])==0 and ((data[i][j])==0) :
                s_s+=1
            elif (data[i][j-1])==0 and ((data[i][j])==1) :
                s_i+=1
            elif (data[i][j-1])==1 and ((data[i][j])==1) :
                i_i+=1
            elif  (data[i][j-1])==1 and ((data[i][j])==2) :
                i_r+=1
    res=np.array([[s_s/(s_s+s_i),s_i/(s_s+s_i),0],[0,i_i/(i_i+i_r),i_r/(i_i+i_r)],[0,0,1]])

    return res
#-------------------------------Description du premier modèle--------------------------------------------------
#qst 1.1
def verif_stoch(matrice):
    #matrice carrée 
    if len(matrice)!= len(matrice[0]):
        return False
    #les lignes somment à 1
    for i in range(len(matrice)):
        cpt=0
        for j in range(len(matrice[0])):
            cpt+=matrice[i][j]
            #toute les proba sont positives
            if matrice[i][j]<0 :
                return False
        if cpt>=0.97 and cpt<=1.03 :
            return True
    
    return False
#qst 1.2
def dist_initiale():
    #d'aprés le sujet :
    n=np.array([0.9,0.1,0])
    return n 
#--------------------------Distribution πt---------------------------------------
#qst 1
#calculer pi_1 en utilisant π0 et A
def pi_1(pi_0,a):
    if verif_stoch(a)==False :
        return 
    vect=np.array([0.0,0.0,0.0])
     # π0 * A 
    for c in range(len(a[0])):
        for l in range(len(a)):
            vect[c]+=pi_0[l]*a[l][c]
    return vect
#qst 2
#calculer pi_t en utilisant π0 et A   
def pi_t(pi_0,a,t):
    if t <1 or t>150 :
        return 
    vect=pi_0
    # π0 * A**t
    for i in range(t):
        vect=pi_1(vect,a)
    return vect 
#qst 3   
"""
fonction pour la représentation graphique de la probabilité d’être dans chaque état en fonction du temps
: param : pi_0
: param : matrice :matrice de transition 
: param : t : le temps
"""  
def graphe_proba(pi_0,matrice,t):
    vect=pi_0
    s=list()#liste sain en fonction du temps
    i=list()#liste sain en fonction du temps
    r=list()#liste sain en fonction du temps
    t_liste=list()# liste du temps
    for j in range(t):     
        t_liste.append(j)
        s.append(vect[0])
        r.append(vect[2])
        i.append(vect[1])
        #changer le vecteur pour chaque temps passé en appelant la fonction qui mult pi * A
        vect=pi_1(vect,matrice)
    plt.plot(t_liste,s,label="sain")
    plt.plot(t_liste,i,label="infecté")
    plt.plot(t_liste,r,label="guéris")
    plt.legend()
    plt.show()
    return 
#-------------------------Tirage aléatoire des états-------------------------

"""
Fonction qui génére une séquence de taille T en utilisant la chaine de markov
: param : t : la taille de la chaine 
: param : matrice : matrice de transition
: param : pi_0
"""
def tirage_alea(t,matrice,pi_0):
    seq=list()
    vect=pi_0
    for i in range(t): #Pourr chaque temps(jours)
        #prendre une probabilité au hasard entre 0 et 1
        p=random.random()
        #si p< pi[0] : on choisi l'etat "0(saint)" et on change pi
        if p < vect[0] :
            seq.append(0)
            vect=matrice[0]
        elif p< (vect[1]+vect[0]):
            seq.append(1)
            vect=matrice[1]
        else :
            seq.append(2)
            vect=matrice[2]
    return seq

"""
Fonction qui génére une séquence de taille T en utilisant la chaine de markov
: param : t : la taille de la chaine 
: param : matrice : matrice de transition
: param : pi_0
: param : n : nombre de personnes
"""
def seq_n(t,matrice,pi_0,n):
    seq=list()
    for i in range(n):#nbr de personnes
        seq.append(tirage_alea(t,matrice,pi_0))
    return seq
#-------------------------Modélisation d’une population----------------------------------------
#qst 1
"""
 Affichage du pourcentage d’indivudus sains infectés et guéris en fonction du temps.
 : param matrice : la séquence 
 : param t : le temps( nombre de jours)
"""
def nb_indiv_s_i_r(matrice,t): #Q2.1.1
    s=list()#liste sain
    il=list()#liste infecté
    r=list()#liste guéris
    t_liste=list()#liste temps
    #pour chaque jours
    for j in range(t):
        s_t=0
        r_t=0
        i_t=0
        t_liste.append(j)  
        #pour chaque individu 
        for i in range(len(matrice)):
            
            if matrice[i][j]==0 :
                s_t+=1
            if matrice[i][j]==1:
                i_t+=1
            if matrice[i][j]==2 :
                r_t+=1
        s.append(s_t)
        il.append(i_t)
        r.append(r_t)
    return t_liste,s,il,r
"""
dessine le graphe d'évolution
: param t_liste: liste du temps
: param s : liste sain en fonction du temps
: param i1 : liste infecté en fonction du temps
: param r : liste guéris en fonction du temps
"""
#qst 2
def graphe_evolution(t_liste,s,i1,r): 
    plt.plot(t_liste,s,label="sain")
    plt.plot(t_liste,i1,label="infécté")
    plt.plot(t_liste,r,label="guérie")
    plt.legend()
    plt.show()
    return 
"""
dessine le graphe de pourcentage
: param t_liste: liste du temps
: param s : liste sain en fonction du temps
: param i1 : liste infecté en fonction du temps
: param r : liste guéris en fonction du temps
"""
#qst 3
def graphe_pourcentage_pratique(t_liste,s,i1,r): 
    liste_s=list()
    liste_r=list()
    liste_i=list()
    nb_indiv=s[0]+r[0]+i1[0]
    for t1 in t_liste:
        liste_s.append(s[t1]/nb_indiv)
        liste_i.append(i1[t1]/nb_indiv)
        liste_r.append(r[t1]/nb_indiv)
    
    plt.plot(t_liste,liste_s,label="pourcentage sain")
    plt.plot(t_liste,liste_i,label="pourcentage infécté")
    plt.plot(t_liste,liste_r,label="pourcentage guérie")
    plt.legend()
    plt.show()
    return 
#--------------------Pic de l’épidémie-----------------------------------------
#qst 2.6 
"""
Fonction qui trouve le pic d'une pidémie
: return : un couple qui représente la valeur maximale et son temps d'apparition
"""
def pic(t_liste,i):
    max_value = max(i)
    temps=np.argmax(i)

    return max_value, temps

#--------------------Longueur de l’infection-------------------------------------------
#qst 1
"""
Estimation de la longueur moyenne d’une séquence de I
: param liste_i : liste de nombre d'infécté en fonction de t
: param nb_individus : nombre d'individus
"""
def longueur_moyenne_i(liste_i, nb_individus):
    #la somme de tout les nombre de séquence d'infectés
    somme= sum(liste_i)
    moyenne = int(somme/nb_individus)
    return moyenne #parce que quand on sort d 'un etat on ne peut plus revenir
"""
Estimation de la longueur moyenne d’une séquence de R
: param a : la séquence de tout les individus
"""
#qst d'une autre partie
def longueur_moyenne_r(a):
    som=0
    nb_seq=0
    
    for l in range(len(a)):
        tmp=0
        for c in range(1,len(a[0])):
            if a[l][c-1]==2 and a[l][c]==2:
                 tmp+=1
                 
            elif a[l][c-1]==2 and a[l][c]==0:
                som+=tmp+1
                nb_seq+=1

    return som/nb_seq,nb_seq

#qst 2 
def longueur_theorique_i(matrice):#on s'interesse au moment de passé de i à R

    return 1/matrice[1][2]
def longueur_theorique_r(matrice):#on s'interesse au moment de passé de r à s

    return 1/matrice[2][0]

#théoriquement , la distribution suit une loi géométrique de paramétre p
"""
Fonction qui représente la loi géométrique
: param p : le paramétre de la loi
: param n : le temps
"""
def loi_geo(p,n):
    liste=list()
    j=0
    for i in range(n):
        j=p*((1-p)**i)
        liste.append(j)
    return liste 
#qst 3
"""
Dessiner de le graphe de distribution de i
: param p : proba d'aller de passer de i à r
: param list_t : la liste du temps
: liste_i : liste des individu infecté par jours
"""
def graphe_distribution_i(p,liste_t,liste_i,nb_indiv):
    liste_pratique=list()
    liste_theo=list()
    loi_geom=loi_geo(p,len(liste_t))

    for tmp in liste_t:
        liste_theo.append(loi_geom[tmp])
        #vect=pi_1(vect,matrice)
        liste_pratique.append((liste_i[tmp])/((nb_indiv)*(tmp+1)))
    plt.bar(liste_t,liste_pratique,label="Pratique",color='green')
    plt.plot(liste_t,liste_theo,label="Theorique",color='red')
    plt.legend()
    plt.show()
    return

#-------------------------------Modèle ergodique---------------------

#------------Analyse du modèle---------
#qst 5
"""
Calculer la distribution stationnaire 
: param pi_0 : pi 0
: param matrice : matrice de transition
"""
def distributionStationnaire(pi_0,matrice):
    pi_t=pi_0
    pi_t_1=pi_1(pi_0,matrice)
    # tant que π (t-1) != π (t) : on continue
    while(np.array_equal(pi_t,pi_t_1)==False):
        #pi_t : π (t-1)
        #pi_t_1 : π (t)
        pi_t = pi_1(pi_t,matrice)#π (t-1) * matrice de transition
        pi_t_1 = pi_1(pi_t_1,matrice)#π (t) * matrice de transition
    return pi_t
#-------------------------Longueur de l’immunité-------------------------------
#qst 3
"""
Afficher la distribution théorique et la distribution observée de la longueur de l’immunité.
: param p : le parametre de la loi géométrique
: matrice :  la séquence de tout les individus
"""
def graphe_distribution_r(p,matrice):
    liste_pratique=list()
    liste_theo=list()
    liste_r=list()
    r=0#nombre guéris
    n=0#nombre de séquences
    liste_t=list()
    #pour chaque individus
    for j in range(len(matrice[0])-1):
        r=0
        #pour chaque temps( jour)
        for i in range(len(matrice)):
            trouve=False
            if matrice[i][j]==2:
                #on regarde si y'a un "s" qui suit aprés un "r" pour incrémenter le nombre de séquence 
                for col in range(j+1,len(matrice[0])):
                    if matrice[i][col]==0 :
                        trouve=True
                        break
                #nombre de "r"
                if trouve :
                    r+=1
                #si on troouve un s devant donc il y'a une nouvelle séquence
                if matrice[i][j+1]==0:
                    n+=1
        #liste des nombre de "r" de tout les individus en fontion du temps

        liste_r.append(r)
        #liste du temps
        liste_t.append(j)
    #distribution théorique
    loi_geom=loi_geo(p,len(liste_t))
    # on calcule la longeur moyenne EN FONCTION DU TEMPS
    for tmp in range(len(liste_t)):
        #liste théorique
        liste_theo.append(loi_geom[tmp])
        #pour ne pas diviser sur 0
        if tmp!=0:
            #moy = (liste_r[tmp]))/((n)) et puisque c'est en fonction du temps on divise sur tmp
            liste_pratique.append(((liste_r[tmp]))/((n)*(tmp)))
        else :
            liste_pratique.append((liste_r[tmp])/((n)))
    plt.bar(liste_t,liste_pratique,label="Pratique",color='green')
    plt.plot(liste_t,liste_theo,label="Theorique",color='red')
    plt.legend()
    plt.show()
    return


#-------------------------------------Confinement-----------------------------------
"""
Fonction qui génère une séquence en fonction du pourcentage d'individus infectés 
:param pi : la distribution initiale 
: matrice_dec:matrice de trasition quand il y'a un déconfinement
: matrice_conf : matrice de trasition quand il y'a un confinement 
: param nb_indiv : nombre d'individus
: nb_jours: le temps(nombre de jours)
"""
def gener_seq(pi,matrice_dec,matrice_conf,nb_indiv,nb_jours):
    nb_i=0
    liste=list()
    vect=pi
    nb_conf=0
    nb_deconf=0
    matrice=np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])#matrice intermédiare pour passer de conf à déconf ou l'inverse
    #un dictionnaire pour chaque début et fin d'un confinement
    liste_temps_conf={"debut":list(),"fin":list()}
    #un dictionnaire pour chaque début et fin d'un déconfinement
    liste_temps_dec={"debut":list(),"fin":list()}
    #on vérifie d'abord le pourcentage d'infecté pour chaque colonne(pout chaque t)
    for t in range(nb_jours):
        #CONFINEMENT
        if (nb_i/nb_indiv)>0.25 :
            #si on était et qu'on est toujours en confinement : on continue 
            if  np.array_equal(matrice,matrice_conf)==False:
                matrice=matrice_conf
                nb_conf+=1
                #début confinement
                liste_temps_conf["debut"].append(t-1)
                if len(liste_temps_dec["debut"])> len(liste_temps_dec["fin"]):
                    liste_temps_dec["fin"].append(t-1)
        #DECONFINEMENT
        if  (nb_i/nb_indiv)<0.1 : 
            if np.array_equal(matrice,matrice_dec)==False:
                matrice=matrice_dec
                nb_deconf+=1
                if len(liste_temps_conf["debut"])> len(liste_temps_conf["fin"]):
                    liste_temps_conf["fin"].append(t-1)
                if t==0 :
                    liste_temps_dec["debut"].append(0)
                else :
                    liste_temps_dec["debut"].append(t-1)
        nb_i=0
        #une fois la matrice fixé : on passe à la génération: on va se représenter les séquences comme une liste de colonne 
        for n in range(nb_indiv):
            p=random.random()
            if t == 0:
                #il  y'a juste une ligne qui va représenter les colonnes : aprés on rajoutera des listes pour chaque case de cette ligne
                new_list=list()#lignes
                liste.append(new_list)
                if p < vect[0] :
                    liste[n].append(0)
                    
                elif p< (vect[1]+vect[0]):
                    liste[n].append(1)
                    nb_i+=1
                else :
                    liste[n].append(2)
            #On est pas à la premiere ligne : donc on rajoute pour chaque colonne une séquence tout en changant le vecteur 
            else :    
                vect=matrice[liste[n][t-1]]
                if p < vect[0] :
                    liste[n].append(0)
                    
                elif p< (vect[1]+vect[0]):
                    liste[n].append(1)
                    
                else :
                    liste[n].append(2)
                if liste[n][t]==1:
                    nb_i+=1
    return liste,nb_conf,nb_deconf,liste_temps_conf,liste_temps_dec       
            




