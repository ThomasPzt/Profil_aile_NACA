import numpy as np
import matplotlib.pyplot as plt


def coordonnees_naca(profile, corde, nb_points, type_distribution):
    # Extraire les paramètres du code du profil (1)
    t = int(profile[2:]) / 100.0

    # Créer le tableau des valeurs de xc en fonction du type de distribution
    if type_distribution == 'linéaire':
        valeurs_xc = np.linspace(0, 1, nb_points)
    elif type_distribution == 'non-uniforme':
        valeurs_theta = np.linspace(0, np.pi, nb_points)
        valeurs_xc = 0.5 * (1 - np.cos(valeurs_theta))
    else:
        raise ValueError("Type de distribution invalide. Choisissez 'linéaire' ou 'non-uniforme'.")

    # Calculer les valeurs d'yt en fonction de l'équation NACA (2)
    valeurs_yt = 5 * t * (0.2969 * np.sqrt(valeurs_xc) - 0.1260 * valeurs_xc -
                          0.3516 * valeurs_xc ** 2 + 0.2843 * valeurs_xc ** 3 - 0.1036 * valeurs_xc ** 4)

    # Calculer les coordonnées pour les surfaces supérieure et inférieure
    # d'après (3) et (4)
    xsup = valeurs_xc * corde
    ysup = valeurs_yt * corde
    xinf = xsup
    yinf = -ysup

    return xsup, ysup, xinf, yinf


def principal():
    # Entrée utilisateur: le numéro du profil, la corde le nombre de points désiré et la distribution
    # avec vérifications de types
    while True:
        try:
            code_profil = input("Entrez le code du profil NACA 4 chiffres symétrique : ")
            assert len(code_profil) == 4 and code_profil.isdigit(), "Le code du profil doit contenir 4 chiffres."

            longueur_corde = float(input("Entrez la longueur de la corde (en mètres) : "))
            assert longueur_corde > 0, "La longueur de la corde doit être un nombre positif."

            nb_points = int(input("Entrez le nombre de points le long de la corde : "))
            assert nb_points > 0, "Le nombre de points doit être un entier positif."

            type_distribution = input("Entrez le type de distribution (linéaire/non-uniforme) : ").lower()
            assert type_distribution in ['linéaire',
                                         'non-uniforme'], ("Type de distribution invalide. Choisissez 'linéaire' ou "
                                                           "'non-uniforme'.")

            break
        # pour des erreurs dans le try
        except ValueError as ve:
            print(f"Erreur : {ve}")
        except AssertionError as ae:
            print(f"Erreur : {ae}")

    # Génération des coordonnées de l'aile
    xsup, ysup, xinf, yinf = coordonnees_naca(code_profil, longueur_corde, nb_points, type_distribution)

    # Calcule de l'épaisseur maximale et sa position
    # On cherche pour ysup car ysup=-yinf
    epaisseur_maximale = 2 * np.max(ysup)
    # on récupère la position associée
    position_epaisseur_maximale = xsup[np.argmax(ysup)]

    # Afficher les résultats
    print(f"Épaisseur maximale : {epaisseur_maximale:.4f} mètres")
    print(f"Position de l'épaisseur maximale : {position_epaisseur_maximale:.4f} mètres")

    # Tracer la forme de l'aile
    # légende
    plt.plot(xsup, ysup, label='Extrados')
    plt.plot(xinf, yinf, label='Intrados')
    # titre axes
    plt.xlabel('Longueur de la Corde (m)')
    plt.ylabel('Épaisseur (m)')
    # titre graphique
    plt.title(f'Profil NACA {code_profil}')
    plt.grid(True)
    plt.legend()
    plt.show()

# appel de la fonction
principal()
