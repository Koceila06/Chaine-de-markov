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

<img width="302" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169701661-16458b14-2e6f-4073-98d7-204da72a97ff.PNG">


## Modèle ergodique
<p> Nous allons maintenant considérer un second modèle, les individus guéris peuvent redevenir sains avec
une probabilité de 0.02. Ils-elles peuvent perdre leur immunité face à la maladie </p> 

<img width="430" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169701690-aefeb5d8-079e-4509-94b3-bce2c0012dd5.PNG">

## Distribution observée sur une population de 200 individus

<img width="286" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169701751-30b425cc-0f0c-4652-8a06-37410e77d3b3.PNG">

## Proportion d’individus sains, infectés et guéris

<img width="300" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169703331-819d0f04-55fa-4169-be13-a89c2113b83f.PNG">

<p> D'aprés les graphes,pour un temps assez grand, on remarque que la population a 65% de chance d'être guéris ,et 0.19% d'être infecté, et 0.16% d'être sain, l'état R n'est plus absorbant. </p>

<Strong> En changeant la distribution initiale π0, on remarque que les etats converge vers les même valeurs précedentes (65% de chance d'être guéris ,0.19% d'être infecté et 0.16% d'être sain), on conclut que la distribution finale ne dépend pas de π0.</Strong>

## Natures des états 

<ul> 
  <li> Récurrents car on peut y retourné infiniment de fois </li> 
  <li> Apériodiques car l'état "sain" boucle sur lui même </li> 
  <li> Irréductibles car avec un etat "n" on peut accéder à tout les autres états </li> 
  </ul>
  
  ## Affichage de la distribution théorique et de la distribution observée de la longueur d’infection
  
  <img width="300" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169704117-253cd59a-916f-4274-bc66-16ff70d11e8f.PNG">
<p> 

la distribution stationnaire est :
[0.01662708 0.21852732 0.76484561]

On remarque que plus on augmente la probabilité de sain à infecté, plus les individus deviennent infectés plus rapidement. On remarque aussi que la longueur de l'imunité observé se rapproche de la théorique même pour un temps inférieur à 20 (ce qui est normal vue que on ce retrouve plus vite à l'état R)
 </p>
 
 ## Confinement 
 On peut imaginer que si des mesures de distanciation sociale sont mises en place, la probabilité de
devenir infecté devient nulle.
Nous allons donc alterner entre les périodes de non distanciation et de distanciation : 
<ul> 
  <li> En période de non-confinement, nous utilisons la matrice de transition précédentd  </li>
  <li> En période de confinement, la probabilité de devenir infecté pour un individu sain devient nulle </li>
  </ul>
<Strong> On décide que  : </Strong> 
<ul>
  <li> Quand il y a 25% d’individus infectés dans la population, nous passons en période de confinement </li>
  <li> Le nombre d’individus infectés va décroître. Quand il y a moins de 10% d’infectés, le confinement
est levé</li>
  </ul> 
  
  ##  Représentation de l’évolution du nombre d’indi-vidus à chaque temps t en respectant les conditions précédentes 
  
  <img width="282" alt="Capture" src="https://user-images.githubusercontent.com/77555379/169704537-2f214823-c1f1-4a86-8533-882bf2ee88c2.PNG">

<Strong> On remarque que pour un t==150 jours : 
  <p> Le nombre de confinement nécessaires est : 7 </p>
  <p> Le nombre de deconfinement nécessairesest 7 </p>
</Strong> 

## Auteur
Koceila Kemiche
