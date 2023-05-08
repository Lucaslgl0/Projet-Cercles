from cercles import *
import turtle
import math


def cercle(centre, rayon):
    """
    Pour dessiner un cercle en connaissant son centre et son rayon.
    """
    turtle.penup()
    turtle.goto(centre[0], centre[1] - rayon)
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()
    turtle.goto


cercle1_rayon = 150 / (int(input("Quel est le rayon de courbure du cercle 1:")))
cercle2_rayon = 150 / (int(input("Quel est le rayon de courbure du cercle 2:")))
cercle3_rayon = 150 / (int(input("Quel est le rayon de courbure du cercle 3:")))

turtle.setup(1000, 1000, 500, 500)
turtle.speed(5)
turtle.hideturtle()
"""cercle((0, 0), cercle1_rayon)
cercle((cercle1_rayon + cercle2_rayon, 0), cercle2_rayon)
cercle(
    (
        -(
            cercle2_rayon
            - cercle1_rayon
            - cercle1_rayon**2
            - cercle2_rayon**2
            - 2 * cercle1_rayon * cercle2_rayon
        )
        / (2 * cercle1_rayon + 2 * cercle2_rayon),
        (
            math.sqrt(
                abs(
                    cercle1_rayon
                    + cercle3_rayon
                    - (
                        (
                            cercle2_rayon
                            - cercle1_rayon
                            - cercle1_rayon**2
                            - cercle2_rayon**2
                            - 2 * cercle1_rayon * cercle2_rayon
                        )
                        / (2 * cercle1_rayon + 2 * cercle2_rayon)
                    )
                    ** 2
                )
            )
        ),
    ),
    cercle3_rayon,
)"""

turtle.exitonclick()
