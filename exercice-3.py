import random

def deviner_nombre_mystere():
    nombre_mystere = random.randint(0, 100)
    essais = 0

    print("Bienvenue dans le jeu Devine le Nombre Mystère entre 0 et 100!")

    while True:
        essai_utilisateur = int(input("Devine le nombre : "))
        essais += 1

        if essai_utilisateur < nombre_mystere:
            print("Plus grand! Essaye encore.")
        elif essai_utilisateur > nombre_mystere:
            print("Plus petit! Essaye encore.")
        else:
            print(f"Félicitations! Tu as trouvé le nombre mystère {nombre_mystere} en {essais} essais.")
            break

if __name__ == "__main__":
    deviner_nombre_mystere()
