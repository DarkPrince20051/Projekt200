import turtle
import tkinter as tk

# Funkcija za crtanje linije
def linija(duzina):
    if duzina < 10:
        turtle.forward(duzina)
        return
    else:
        linija(duzina / 3)
        turtle.left(60)
        linija(duzina / 3)
        turtle.right(120)
        linija(duzina / 3)
        turtle.left(60)
        linija(duzina / 3)

# Funkcija za crtanje snježne pahuljice
def pahuljica(duzina):
    turtle.begin_fill()  # Počni punjenje bojom
    for _ in range(3):
        linija(duzina)
        turtle.right(120)
    turtle.end_fill()  # Završi punjenje bojom

# Postavke prozora za crtanje
turtle.setup(width=500, height=500, startx=200, starty=200)
root = turtle.Screen()._root
root.resizable(False, False)  # Postavljamo prozor kao neresizabilan
turtle.speed(0)  # Postavljamo brzinu na maksimum

# Postavljamo početnu poziciju
turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()

# Postavljamo boju punjenja
turtle.fillcolor("lightblue")

# Crta snježnu pahuljicu
pahuljica(300)

# Zatvara prozor kad se klikne
turtle.done()
