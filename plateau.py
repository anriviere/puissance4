import numpy as np


class Plateau:
    def __init__(self):
        self.row_count = 6
        self.column_count = 7

    def creation_plateau(self):
        plateau = np.zeros((self.row_count, self.column_count))
        return plateau

    def colonne_dispo(self, plateau, col):
        return plateau[self.row_count - 1][col] == 0

    def emplacement_libre(self, plateau, colonne):
        for r in range(self.row_count):
            if plateau[r][colonne] == 0:
                return r

    def print_plateau(self, plateau):
        print(np.flip(plateau, 0))
