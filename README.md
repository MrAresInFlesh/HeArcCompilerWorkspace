# Introduction

## Définition
Un compilateur est un programme qui prend en entrée le texte d'un programme dans un certain langage et donne en sortie le texte dans un autre langage tout en préservant la signification .

 C'est donc essentiellement un processus de traduction:

## Principe
Un compilateur fonctionne par une méthode d'analyse-synthèse:

### Analyse: Vise à comprendre un objet en le décomposant en ses constituants. Elle établit donc tout d'abord des critères permettant d'identifier les composants.
Synthèse: Opération par laquelle on rassemble, en un tout homogène divers éléments d'un domaine de connaissance.

- L'analyse :
  - Découpe le programme source en mots (Lexèmes)
  - Fait une analyse syntaxique et sémantique
  - Construit une représentation intermédiaire

- La synthèse :
  - Optimise et génère le langage de cible à partir de la représentation intermédiaire

- La représentation intermédiaire  doit:
  - être indépendante du langage source
  - permettre de facilement générer du code cible
permettre de refléter l'analyse de plusieurs langages sources
  - conserver la sémantique oppérationnelle du programme.

`**Important** : La représentation intermédiaire est généralement représentée par un Arbre Syntaxique Abstrait (AST)`

## Structure

![](https://i.imgur.com/LbBFgTe.png)



# À retenir
Les spécifications par ordre d'importance d'un compilateur sont:

**Capital**
- Conserver la sémantique
- Ne pas introduire d'erreurs

**Important**
- Traiter des programmes de grande taille
- Traiter des programmes en un temps acceptable 
- Générer du code optimisé en taille et en performances

**Dépend du contexte**
- Fournit un bon diagnostique d'erreur
