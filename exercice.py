#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    distance_entre_min_et_maj = ord("a") - ord("A")
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        if ord("a") <= ord(lettre) and ord(lettre) <= ord("z"):
            lettre = chr(ord(lettre) - distance_entre_min_et_maj)
        resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'arbre',
        '360 no-scope'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
