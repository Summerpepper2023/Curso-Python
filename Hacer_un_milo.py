print("Voy a revisar la nevera")
hay_leche = input("¿Hay leche? (s/n)")
print("Voy a la despensa")
hay_milo = input("¿Hay milo? (s/n)")

if hay_leche != "s" or hay_milo != "s":
    print("Voy a la tienda de la esquina")
    if hay_leche != "s":
        print("Compro leche")
    if hay_milo != "s":
        print("compro milo")

print("regreso a mi casa")
print("hecho la leche y el milo en un vaso")
print("revuelvo el milo y la leche")
print("disfruto de mi milo :D")