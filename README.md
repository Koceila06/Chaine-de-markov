# Chaine de Markov

## Présentation du projet
<p>
  L’objectif de ce projet est de manipuler des chaînes de Markov pour étudier la propagation d’une épi-
démie dans une population
  </p>
  <p> 
Les populations sont constituées de 3 types d’individus. Chaque individu est dans un
des 3 états suivant : sain S, infecté I ou guéri R
  </p>
  
  ## Premier modèle 
  Dans un premier temps, nous allons considérer qu’à chaque temps :
  <ul> 
  <li> Chaque individu sain peut rester sain ou devenir infecté </li>
  <li> Chaque individu infecté peut rester infecté ou devenir guéri </li>
  <li> Chaque individu guéri reste guéri </li>
  </ul>
  et que la probabilité de passer d’un état à l’autre <Strong >ne dépend que de l’état précédent </Strong>
  
  ## Base de données 
 Note base de données contient une population de 100 individus, pendant 200 jours.
 Les individus sains sont note 0, les infecté 1 et les guéris 2
 
  ## Probabilités de transition 
  <img width="452" alt="first_model" src="https://user-images.githubusercontent.com/77555379/169696000-37d16e86-975f-4257-97ea-4915f04a9edd.PNG">

  ## Matrice de transition 
 Représentaion des probabilités de transition sous forme de matrice ( 3 × 3 ) où chaque ligne correspond à l'état actuel et chaque colonne à un état futur possible
 
 
 ## Vérification de matrice de transition 
 
 Avant de pouvoir utiliser les chaines de Markov, on doit d'abord vérifier que la matrice de transition est stochastique 
 
 ## Distribution πt 
 On considère π0 = [0.9,0.1,0] la distribution de probabilité initiale tel que : 
 La première colonne représente la probabilité d'un individu d'être sain, la deuxième colonne d'être infecté et la troisième d'être  gueri  
 et Soit A, la matrice de transition : 
 Pour calculer la distribution d'un t donné, on aura besoin juste de la distribution  de l'état précédent, on a donc : πt+1 = πt * A
 ## Représentation graphique de la probabilité d’être dans chaque état en fonction du temps
 <img width="289" alt="Représentation" src="https://user-images.githubusercontent.com/77555379/169699202-c3fefce9-a1da-4bc8-89cf-087f323874b4.PNG">
 
 

<p>
  <Strong> Description :</Strong>  pour un temps assez grand, on remarque que les états sain et infecté converge vers 0 alors que l'état guéris converge vers 1, on peut expliquer cela du fait que l'état guéris est un état absorbant.
  </p>

## Génération d'une séquence de taille T en utilisant la chaîne de Markov
Pour générer une séquence aléatoire, on choisit un état initial au hasard (en utilisant π0) ; puis on choisit les états suivants
en suivant les probabilités de transition (= la matrice de transition A).

<p> Une fois cela est fait, Nous allons générer un ensemble de séquences pour une population de 200 individus </p>

## Evolution du nombre d’individus dans les trois états en fonction du temps

<img width="412" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169700286-e8985a25-5f49-4a4e-a436-94b4ce5edfc4.PNG">

## Proportion d’individus sains, infectés et guéris

<img width="288" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169700472-c129ed50-d3b4-408e-b4ec-813261d41f29.PNG">

<p> Pour un t trés grand, la proportion d’individus sains, infectés et guéris sont 0,0,1 réspectivement. </p>

## Pic de l’épidémie

Le pic de épidémie représente le temps où nous avons constaté plus de cas infectés  : Pour notre cas, on voit qu'il est enrigistré au temps 9 avec 89 individus infectés (parmis 150 )
## Longueur de l’infection
À partir des simulations, On estime la longueur moyenne d’une séquence de infectés à 14 jours.

Pour calculer la longeur théorique de l'infection, on utilise l'espérance de la loi géométrique, pour notre cas, elle est de 14.28.

## Affichage de la distribution théorique et de la distribution observée de la longueur d’infection
<p> La distribution théorique est une loi géométrique </p>

![Capture](https://user-images.githubusercontent.com/77555379/169701343-7f8ddee7-040d-4699-9227-12a7a2609cff.JPG)

## Modèle ergodique
<p> Nous allons maintenant considérer un second modèle, les individus guéris peuvent redevenir sains avec
une probabilité de 0.02. Ils-elles peuvent perdre leur immunité face à la maladie </p> 

![Capture](https://user-images.githubusercontent.com/77555379/169701556-c1b8440e-fa9c-4d93-8d56-511bb47e950a.JPG)
