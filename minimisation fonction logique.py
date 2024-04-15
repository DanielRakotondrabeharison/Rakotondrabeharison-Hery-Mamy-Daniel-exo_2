from itertools import product

# Définition des variables
variables = ['a', 'b', 'c']

# Création de la table de vérité
truth_table = []
for values in product([0, 1], repeat=len(variables)):
    a, b, c = values
    result = a and b or (not b and c) or (a and not c)
    truth_table.append((a, b, c, result))

# Affichage de la table de vérité
print("Table de vérité :")
print("{:2s} {:2s} {:2s} | {:2s}".format(*variables, "f"))
print("-" * 11)
for row in truth_table:
    print("{:2d} {:2d} {:2d} | {:2d}".format(*row))

# Groupement des termes avec la méthode de Karnaugh
groups = []
for i in range(8):
    if truth_table[i][3] == 1:
        a, b, c, _ = truth_table[i]
        group = []

        if i % 2 == 0:
            group.append(('0' if a == 0 else '1') + ' -')
        if (i + 1) % 2 == 0:
            group.append(('0' if b == 0 else '1') + ' -')
        if i < 4:
            group.append(('0' if c == 0 else '1') + ' -')

        groups.append(group)

# Simplification des groupes
simplified_groups = []
for group in groups:
    simplified_group = []

    for variable in variables:
        if variable in group:
            simplified_group.append(variable)
        elif 'non_' + variable in group:
            simplified_group.append('non_' + variable)

    if len(simplified_group) > 0:
        simplified_groups.append(simplified_group)

# Affichage des groupes simplifiés
print("\nGroupes simplifiés :")
for group in simplified_groups:
    print(" + ".join(group))

# Affichage de la fonction logique minimisée
print("\nFonction logique minimisée :")
minimized_function = " + ".join(["".join(group) for group in simplified_groups])
print(minimized_function)