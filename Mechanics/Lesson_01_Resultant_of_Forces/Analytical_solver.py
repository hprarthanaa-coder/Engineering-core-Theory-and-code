# =================================================================
# Subject: Engineering Mechanics (Lesson 1 - Coplanar Forces)
# Concept: Analytical Resolution & Resultant of Forces
# Author: Prarthana Holambe 
# Description: This script takes individual force magnitudes and 
#              angles to compute the total Resultant (R) and theta.
# =================================================================

import math

def resultant_force(forces):
    sum_fx = 0
    sum_fy = 0

    for force in forces:
        F = force["magnitude"]
        angle = math.radians(force["angle"])

        if force["reference"] == "vertical":
            fx = F * math.sin(angle)
            fy = F * math.cos(angle)
        else: # reference = horizontal
            fx = F * math.cos(angle)
            fy = F * math.sin(angle)

        if force["horizontal"] == "left":
            fx = -fx
        elif force["horizontal"] == "none":
            fx = 0

        if force["vertical"] == "down":
            fy = -fy
        elif force["vertical"] == "none":
            fy = 0

        sum_fx += fx
        sum_fy += fy

    R = math.sqrt(sum_fx**2 + sum_fy**2)
    theta = math.degrees(math.atan2(abs(sum_fy), abs(sum_fx)))

    # Print ΣFx  with value and direction
    if sum_fx > 0:
            print("Horizontal Direction : →")
    elif sum_fx < 0:
           print("Horizontal Direction : ←")

    # Print ΣFy with value and direction
    if sum_fy > 0:
            print("Vertical Direction : ↑")
    elif sum_fy < 0:
            print("Vertical Direction : ↓")



    print(f"ΣFx = {sum_fx:.2f} N")
    print(f"ΣFy = {sum_fy:.2f} N")
    print(f"Resultant Force = {R:.2f} N")
    print(f"Angle = {theta:.2f}°")


# ==========================
# INPUT FORCES HERE
# ==========================

forces = [
    {
        "magnitude": 20,
        "angle": 16.69,
        "reference": "horizontal",
        "horizontal": "right",
        "vertical": "up",
    },
    {
        "magnitude": 25,
        "angle": 79.69,
        "reference": "horizontal",
        "horizontal": "right",
        "vertical": "up",
    },
    {
        "magnitude": 10,
        "angle": 26.56,
        "reference": "horizontal",
        "horizontal": "left",
        "vertical": "up", 
    },
    {
        "magnitude": 15,
        "angle": 68.19,
        "reference": "horizontal",
        "horizontal": "right",
        "vertical": "down", 
    }
]

resultant_force(forces)
