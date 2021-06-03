import numpy as np
from plateau import Plateau
from network import Network
from jeu import Jeu



def partie():
    run = True
    n = Network()

    joueur = int(n.getP())
    print("Vous êtes le joueur " , joueur)

    while run:
        try:
            jeu = n.send("get")
            if not 'plato' in locals(): 
                plato = jeu.plateau.creation_plateau()
        except:
            run = False
            print("Couldn't get game")
            break

        if not(jeu.connected()):
            print("En attente d'un deuxième joueur")


        if jeu.connected():
                print("ok")
                if joueur == 0:
                    
                    if not jeu.joueur1:
                        if  jeu.choix1 != 10:
                            ligne = jeu.plateau.emplacement_libre(plato, jeu.choix1)
                            jeu.jouer(plato, ligne, jeu.choix1, 2)
                            jeu.plateau.print_plateau(plato)
                            jeu.choix1 = 10



                        if jeu.gagner(plato, 2):
                            print("Le joueur 2 a gagné!")
                            run = False
                        else:
                            jeu.plateau.print_plateau(plato)
                            colonne = str(input("Joueur 1 choisi la colonne (0-6)"))

                            colonne_int = int(colonne)

                            if jeu.plateau.colonne_dispo(plato, colonne_int):
                                ligne = jeu.plateau.emplacement_libre(plato, colonne_int)
                                jeu.jouer(plato, ligne, colonne_int, 1)
                                jeu.plateau.print_plateau(plato)
                                n.send(colonne)

                                print('test')
 


                                if jeu.gagner(plato, 1):
                                    print("Tu as gagné! Bravo!")

                            else:
                                print("colonne non dispo, retente")

                    if jeu.joueur1 and not jeu.joueur2:
                        print('attendre que le joueur 2 joue...')
                        print(jeu.choix1)
                            


                else:
                    if not jeu.joueur2 and not jeu.joueur1:
                        print('attendre que le joueur 1 joue...')


                    if not jeu.joueur2 and jeu.joueur1:

                        ligne = jeu.plateau.emplacement_libre(plato, jeu.choix1)
                        jeu.jouer(plato, ligne, jeu.choix1, 1)
                        jeu.plateau.print_plateau(plato)

                        if jeu.gagner(plato, 1):
                               print("Le joueur 1 a gagné!")
                               run = False


                        else:

                        
                            colonne = str(input("Joueur 2 choisi la colonne (0-6)"))
                            colonne_int = int(colonne)

                            if jeu.plateau.colonne_dispo(plato, colonne_int):
                                ligne = jeu.plateau.emplacement_libre(plato, colonne_int)
                                jeu.jouer(plato, ligne, colonne_int, 2)
                                jeu.plateau.print_plateau(plato)
                                n.send(colonne)

                                if jeu.gagner(plato, 2):
                                    print("Tu as gagné! Bravo!")
                                        
                            else:
                                print("colonne non dispo, retente")

                            
                        
                       

partie()
