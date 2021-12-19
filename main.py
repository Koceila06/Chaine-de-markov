
# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib 
import projet

if __name__=='__main__':
    p=projet.estim_prob()
    fichier=np.loadtxt('data_exo1.txt')
    #print(fichier)
    n=projet.proba_transition(fichier)
    #print(projet.verif_stoch(n))
    pi_0=projet.dist_initiale()
    matrice=np.array([[0.92,0.08,0],[0,0.93,0.07],[0,0,1]])
    #print(projet.pi_1(pi_0,matrice))
    #print(projet.pi_t(pi_0,matrice,20))
    #projet.graphe_proba(pi_0,matrice,100)
    nb_jours=150
    nb_individus=200
    s=projet.seq_n(nb_jours,matrice,pi_0,nb_individus)
    (liste_t,liste_s,liste_i,liste_r)=projet.nb_indiv_s_i_r(s,nb_jours)
    #projet.graphe_evolution(liste_t,liste_s,liste_i,liste_r)
    #projet.graphe_pourcentage_pratique(liste_t,liste_s,liste_i,liste_r)

    (pic_value, temps_pic)=projet.pic(liste_t,liste_i)
    #print("Nombre d'individus inféctés au pic de l'épidémie :"+str(pic_value)+", au temps: " +str(temps_pic))
    
    estimation_longueur_moyenne_i = projet.longueur_moyenne_i(liste_i,nb_individus)
    print("estimation_longueur_moyenne_i : "+str(estimation_longueur_moyenne_i))
    longueur_theorique_i = projet.longueur_theorique_i(matrice)
    print("longueur_theorique_i : "+str(longueur_theorique_i))
    p_i=np.array([0,0.93,0.07])
    #projet.graphe_distribution_i(0.07,liste_t,liste_i,nb_individus)
    
    #-----------------------------------------------------

    pi_0=projet.dist_initiale()
    #pi_0=np.array([0.92,0.08,0]) #Q3.2
    matrice=np.array([[0.92,0.08,0],[0,0.93,0.07],[0.02,0,0.98]])
    #print(projet.pi_1(pi_0,matrice))
    #print(projet.pi_t(pi_0,matrice,20))
    #projet.graphe_proba(pi_0,matrice,100)
    nb_jours=150
    nb_individus=200
    s=projet.seq_n(nb_jours,matrice,pi_0,nb_individus)
    (liste_t,liste_s,liste_i,liste_r)=projet.nb_indiv_s_i_r(s,nb_jours)
    #projet.graphe_evolution(liste_t,liste_s,liste_i,liste_r)
    #projet.graphe_pourcentage_pratique(liste_t,liste_s,liste_i,liste_r)

    (pic_value, temps_pic)=projet.pic(liste_t,liste_i)
    print("Nombre d'individus inféctés au pic de l'épidémie :"+str(pic_value)+", au temps: " +str(temps_pic))

    #projet.graphe_distribution_i(0.07,liste_t,liste_i,nb_individus)
    #Q3.1 : la population a 65% de chance d'etre guerit ,et le prcntage d'infection 0.19 et de saint=0.16
    #Q3.2 : on remarque qu'a partir d'un t (environ 60) les etats converge vers les meme valeur précedente 

    #Q3.3 :  nature des etats : récurrents car on peut y retourné infiniment de fois
    # elle est apériodique 
    # elle est irréductible car avec un etats i on peut acceder a tous les autres etats 
    """m=matrice.dot(matrice)
    m=m.dot(m)
    print(m)
    print(projet.pi_t(pi_0,matrice,3))"""
    #Qst.4 : la matrice A*A correspond aux probabilités en  t=2 qu'on soit à l'un des états(s,i,r)
    #sachant l'état initiale (P(X2=j|X0=i)) Pareil pour A**2,A**3,A**4
    #Elle est stochastique car c'est une matrice carrée et les lignes somment à 1
    print(projet.distributionStationnaire(pi_0,matrice))
    #q3.5 meme resultat que l'observation 
    estimation_longueur_moyenne_r = projet.longueur_moyenne_r(s,liste_r)
    print(estimation_longueur_moyenne_r)
    longueur_theorique_r = projet.longueur_theorique_r(matrice)
    print(longueur_theorique_r)
    print()
    exit()