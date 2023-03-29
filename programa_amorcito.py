import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def potencia(numero):
    potencia = numero * numero
    return potencia

end = False
while not end:
    titulo = "Bienenido a mi potenciador de numeros"
    print("\n" + titulo + "\n" + "-" * len(titulo))
    numero = int(input("¿De que numero quieres sacar potencia?: "))

    if numero:
        print(potencia(numero))

    salida = input("¿Quieres continuar? [S/N]: \n")

    if salida == "S":
        pass
    else:
        end = True

verification = input("¿Eres mi amorcito? [S/N]: \n")

if verification == "N" or verification == "n":
    print("Gracias hijo de la re mil puta ;)")

elif verification == "S" or verification == "S":
    print("Gracias mi vida hermosa por ayudarme a probar mis programas y por hacerme sentir mejor \n"
          "siempre que me estoy sintiendo mal, edes hermosa mi vida nunca dudes de esu pu favu,\n"
          "tadoro con todo mi corazoncito de poio :((( de veditas de veidtas.\n")

    cancion = input("¿Quieres una sorpresita? [S/N]: ")
    while cancion != "S":

        print("¿Apuka nu kiedes mi sorpresita? :[[[\n")
        cancion = input("¿Quieres una sorpresita? [S/N]: \n")

    if cancion == "S":
        print("Midaaaaa :DDDD\n")

        # Crear la interfaz
        ventana = tk.Tk()
        ventana.title("Imagen del amorcito")
        ventana.geometry("600x600")


        # Imagen
        def imagen():
            img = Image.open("corazon-cafe.jpg")
            new_img = img.resize((510, 300))
            render = ImageTk.PhotoImage(new_img)
            img1 = Label(ventana, image=render)
            img1.Image = render
            img1.place(x=100, y=100)


        # Crear botones
        boton = tk.Button(ventana, command=imagen, text="Abrir imagen", height=2, width=20)
        boton.place(x=150, y=450)

        ventana.mainloop()
