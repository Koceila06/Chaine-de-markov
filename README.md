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
## Apprentissage des paramètres d’un modèle à partir de données
