import tkinter as tk
import random as rd
from tkinter.constants import ALL

WIDTH = 600
HEIGHT = 600
mouvement = 10
vitesse = 60
snake_positions = [[300, 300], [290, 300], [280, 300]]
direction = "Right"
score = 0
coord_serpent = []
demarrage = 1


def mouvement_snake():
    """Pour faire bouger le serpent dans différentes directions.
        Son mouvement est réalisé en 2 étapes: effacer le serpent puis en
        créer un nouveau avec les nouvelles coordonnées."""
    global snake_positions
    head_x_position, head_y_position = snake_positions[0]
    if direction == "Left":
        new_head_position = [head_x_position - mouvement, head_y_position]
    elif direction == "Right":
        new_head_position = [head_x_position + mouvement, head_y_position]
    elif direction == "Down":
        new_head_position = [head_x_position, head_y_position + mouvement]
    elif direction == "Up":
        new_head_position = [head_x_position, head_y_position - mouvement]
    snake_positions = [new_head_position] + snake_positions[:-1]
    for i in range(len(coord_serpent)):
        canvas.delete(coord_serpent[i])
    for x_positions, y_positions in snake_positions:
        snake = canvas.create_rectangle(x_positions - 5, y_positions - 5,
                                        x_positions + 5, y_positions + 5,
                                        fill="green")
        coord_serpent.remove(coord_serpent[0])
        coord_serpent.append(snake)
    collision_pomme()
    collision_mur()
    collision_serpent()

    
 
