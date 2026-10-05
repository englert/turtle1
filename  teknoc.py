import turtle

# Ablak beállítása
ablak = turtle.Screen()
ablak.title("Célba érő teknős")
ablak.setup(width=600, height=600)
ablak.bgcolor("lightgreen")

# Játékos teknős
jatekos = turtle.Turtle()
jatekos.shape("turtle")
jatekos.color("blue")
jatekos.penup()
jatekos.goto(-250, -250)

# Cél
cel = turtle.Turtle()
cel.shape("square")
cel.color("red")
cel.penup()
cel.goto(250, 250)


# Mozgató függvények
def fel():
    jatekos.sety(jatekos.ycor() + 20)

def le():
    jatekos.sety(jatekos.ycor() - 20)

def balra():
    jatekos.setx(jatekos.xcor() - 20)

def jobbra():
    jatekos.setx(jatekos.xcor() + 20)


# Billentyűzet kezelése
ablak.listen()

ablak.onkeypress(fel, "Up")
ablak.onkeypress(le, "Down")
ablak.onkeypress(balra, "Left")
ablak.onkeypress(jobbra, "Right")


# A cél ellenőrzése
def cel_ellenorzese():
    if jatekos.distance(cel) < 25:
        jatekos.goto(0, 0)
        jatekos.write(
            "Ügyes voltál!",
            align="center",
            font=("Arial", 24, "bold")
        )
        cel.hideturtle()
    
    else:
        ablak.ontimer(cel_ellenorzese, 100)


# Játék indítása
cel_ellenorzese()

ablak.mainloop()