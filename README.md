# Chaine-de-markov

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
