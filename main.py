try:
    pas_zero = True
    entier = int(input("Saisir un entier"))
    result = str("")
    if entier == 0:
        pas_zero = False

    while entier > 0:
        if entier % 2 == 0:
            result += str("0")
        else:
            result += str("1")
        entier //= 2
        if entier == 1:
            result += str('1')
            break

    result = result[::-1]
    if pas_zero:
        print("conversion en binaire:", result)
    else:
        print("conversion en binaire: 0")
except ValueError:
    print("Mauvaise saisie")