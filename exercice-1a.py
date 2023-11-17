'''''#Exercice 1a :
N = int(input("Entrez la valeur de N : "))
somme = 0

for i in range(N + 1):
    somme += i

print("La somme des N premiers entiers naturels est :", somme)


#Exercice 1b :
valeur = 0

while valeur != 100:
    valeur = int(input("Entrez une valeur (entrez 100 pour terminer") : "))

print("La boucle d'attente est terminée.")

#Exercice 1c :
valeurs_inf_10 = 0
valeurs_10_15 = 0
valeurs_sup_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    while valeur < 0 or valeur > 20:
        print("Valeur invalide. Veuillez réessayer.")
        valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    if valeur < 10:
        valeurs_inf_10 += 1
    elif valeur < 15:
        valeurs_10_15 += 1
    else:
        valeurs_sup_15 += 1

print("Nombre de valeurs inférieures à 10 :", valeurs_inf_10)
print("Nombre de valeurs entre 10 et 15 inclus :", valeurs_10_15)
print("Nombre de valeurs supérieures ou égales à 15 :", valeurs_sup_15)


#Exercice 1d)
X = float(input("Entrez un nombre supérieur à 1 : "))
N = 0
somme = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme soit inférieure ou égale à", X, "est :", N - 1)

'''''
