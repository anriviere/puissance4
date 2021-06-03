import numpy as np
from plateau import Plateau
from network import Network


class Jeu:
    def __init__(self, id):


        self.plateau = Plateau()
        self.game_over = False
        self.turn = 0
        self.current_turn = 0


        self.joueur1 = False
        self.joueur2 = False
        self.ready = False
        self.id = id

        self.choix1 = 10

        # self.choix = [None, None]

    def joueur(self, joueur):
        if joueur == 0:
            self.joueur1 = True
        else:
            self.joueur2 = True


    def connected(self):
        return self.ready


    def deuxJoueurs(self):
        return self.joueur1 and self.joueur2


    def choix(self, joueur, choix):
        self.choix1 = int(choix)
        if joueur == 0:
            self.joueur1 = True
        else:
            self.joueur1 = False





    def jouer(self, plateau, ligne, colonne, piece):
        plateau[ligne][colonne] = piece

    def gagner(self, plateau, piece):
        # victoire horizontal
        for c in range(self.plateau.column_count-3):
            for r in range(self.plateau.row_count):
                if plateau[r][c] == piece and plateau[r][c+1] == piece and plateau[r][c+2] == piece and plateau[r][c+3] == piece:
                    return True

        # victoire Vertical
        for c in range(self.plateau.column_count):
            for r in range(self.plateau.row_count-3):
                if plateau[r][c] == piece and plateau[r+1][c] == piece and plateau[r+2][c] == piece and plateau[r+3][c] == piece:
                    return True


        # diagonal montante
        for c in range(self.plateau.column_count-3):
            for r in range(self.plateau.row_count-3):
                if plateau[r][c] == piece and plateau[r+1][c+1] == piece and plateau[r+2][c+2] == piece and plateau[r+3][c+3] == piece:
                    return True


        # diagonal descendante
        for c in range(self.plateau.column_count-3):
            for r in range(3, self.plateau.row_count):
                if plateau[r][c] == piece and plateau[r-1][c+1] == piece and plateau[r-2][c+2] == piece and plateau[r-3][c+3] == piece:
                    return True





    def resetJoueur(self):
        self.joueur1 = False
        self.joueur2 = False

