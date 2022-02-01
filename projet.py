import numpy as np
import random
import matplotlib.pyplot as plt

""" 
Partie 1
"""
def estim_prob() : #qst1.1
    matrice=np.array([[2/3,1/3,0],[0,5/6,1/6],[0,0,1]])
    return matrice

def proba_transition(data) : #qst1.2
    nb_lignes=len(data)
    nb_colonnes=len(data[0])
   
    s_s=0
    s_i=0
    i_i=0
    i_r=0
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
def verif_stoch(matrice):
    if len(matrice)!= len(matrice[0]):
        return False
    for i in range(len(matrice)):
        cpt=0
        for j in range(len(matrice[0])):
            cpt+=matrice[i][j]
            if matrice[i][j]<0 :
                return False
        if cpt!=1 :
            return False
    
    return True
def dist_initiale():
    n=np.array([0.9,0.1,0])
    return n
def pi_1(pi_0,a):
    if verif_stoch(a)==False :
        return 
    vect=np.array([0.0,0.0,0.0])
    for c in range(len(a[0])):
        for l in range(len(a)):
            vect[c]+=pi_0[l]*a[l][c]
    return vect
def pi_t(pi_0,a,t):
    if t <1 or t>200 :
        return 
    vect=pi_0
    for i in range(t):
        vect=pi_1(vect,a)
    return vect       
def graphe_proba(pi_0,matrice,t):
    vect=pi_0
    s=list()
    i=list()
    r=list()
    t_liste=list()
    for j in range(t):
        
        t_liste.append(j)
        s.append(vect[0])
        r.append(vect[2])
        i.append(vect[1])
        vect=pi_1(vect,matrice)
    plt.plot(t_liste,s)
    plt.plot(t_liste,i)
    plt.plot(t_liste,r)
    plt.show()
    return 
def tirage_alea(t,matrice,pi_0):
    seq=list()
    vect=pi_0
    for i in range(t): #t:nombre de jours
        p=random.random()
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
def seq_n(t,matrice,pi_0,n):
    seq=list()
    for i in range(n):#nombre de personne
        seq.append(tirage_alea(t,matrice,pi_0))
    return seq
def nb_indiv_s_i_r(matrice,t): #Q2.1.1

    s=list()
    il=list()
    r=list()
    t_liste=list()
    for j in range(t):
        s_t=0
        r_t=0
        i_t=0
        t_liste.append(j)   
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
    """
    plt.plot(t_liste,s)
    plt.plot(t_liste,il)
    plt.plot(t_liste,r)
    plt.show()
    """
    return t_liste,s,il,r
def graphe_evolution(t_liste,s,i1,r): #Q2.1.2
    plt.plot(t_liste,s,label="sain")
    plt.plot(t_liste,i1,label="infécté")
    plt.plot(t_liste,r,label="guérie")
    plt.legend()
    plt.show()
    return 
def graphe_pourcentage_pratique(t_liste,s,i1,r): #Q2.2
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

#q2.3 : pour un t tres grand, on remarque que tous les individus deviennent guéries, le vecteur est donc (0.0.1), on peut dire aussi que l'etat guerie est un etat absorbant 
#pareil pour la q2.4

def pic(t_liste,i):#Pic de l'épidémie
    max_value = max(i)
    temps=np.argmax(i)

    return max_value, temps

def longueur_moyenne_i(liste_i, nb_individus):#longueur .. q2.1
    somme= sum(liste_i)
    moyenne = int(somme/nb_individus)
    return moyenne #juste psk si on sort d 'un etat on nee peut plus revenir
def longueur_moyenne_r(a,liste_r):#longueur .. q2.1
   
    som= 0
    nb_seq=0
    somme=0
    for l in range(len(a)):
        som=0
        nb_seq=0
        for c in range(1,len(a[0])):
            """
            if a[l][c-1]==2 and a[l][c]== 2:
                som+=1
            if a[l][c-1]==1 and a[l][c]== 2:
                som+=1    
                nb_seq+=1
            if a[l][c-1]==2 and a[l][c]== 0:
                break"""
            if a[l][c-1]==1 and a[l][c]== 2 or a[l][c-1]==2 and a[l][c]== 2  :
                som+=1
            if a[l][c-1]==2 and a[l][c]== 0:
                break
        somme+=som/len(a)
   
    return int(somme)

def longueur_theorique_i(matrice):#on s'interesse au moment de passé de i à R

    return 1/matrice[1][2]
def longueur_theorique_r(matrice):#on s'interesse au moment de passé de i à R

    return 1/0.02
def loi_geo(p,n):
    liste=list()
    j=0
    for i in range(n):
        j=p*((1-p)**i)
        liste.append(j)
    return liste 

def graphe_distribution_i(p,liste_t,liste_i,nb_indiv):
    liste_pratique=list()
    liste_theo=list()
    #p=proba d'aller de passer de i à r
    #list_t: la liste du temps
    #liste_i:liste des individus infectés par jours


    loi_geom=loi_geo(p,len(liste_t))

    for tmp in liste_t:
        liste_theo.append(loi_geom[tmp])
        #vect=pi_1(vect,matrice)
        liste_pratique.append((liste_i[tmp])/((nb_indiv)*(tmp+1)))
    print(liste_pratique[0])
    plt.bar(liste_t,liste_pratique,label="Pratique",color='green')
    plt.plot(liste_t,liste_theo,label="Theorique",color='red')
    plt.legend()
    plt.show()
    return

#-------------------------------3
def distributionStationnaire(pi_0,matrice):
    pi_t=pi_0
    pi_t_1=pi_1(pi_0,matrice)
    while(np.array_equal(pi_t,pi_t_1)==False):
        pi_t = pi_1(pi_t,matrice)
        pi_t_1 = pi_1(pi_t_1,matrice)
    return pi_t
