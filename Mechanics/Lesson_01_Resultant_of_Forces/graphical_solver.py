# =================================================================
# Subject: Engineering Mechanics (Lesson 1 - Coplanar Forces)
# Concept: Graphical vector Representation of Resultant of Forces
# Author: Prarthana Holambe 
# Dependencies: Matplotlib
# Description: This script visually plots coplanar forces as vectors originating from a central point and maps the final calculated resultant force (R) on a 2D coordinate plane.
===============================================================

import matplotlib.pyplot as plt
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
        else:
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

    if sum_fx > 0:
        print("Horizontal Direction : →")
    elif sum_fx < 0:
        print("Horizontal Direction : ←")

    if sum_fy > 0:
        print("Vertical Direction : ↑")
    elif sum_fy < 0:
        print("Vertical Direction : ↓")

    print(f"ΣFx = {sum_fx:.2f} N")
    print(f"ΣFy = {sum_fy:.2f} N")
    print(f"Resultant Force = {R:.2f} N")
    print(f"Angle = {theta:.2f}°")

    return sum_fx, sum_fy


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

sum_fx, sum_fy = resultant_force(forces)

# ---------------- GRAPH ----------------

plt.figure(figsize=(8, 8))

# Draw axes
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Plot each force
for i, force in enumerate(forces, start=1):

    F = force["magnitude"]
    angle = math.radians(force["angle"])

    if force["reference"] == "vertical":
        fx = F * math.sin(angle)
        fy = F * math.cos(angle)
    else:
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

    plt.quiver(
        0, 0,
        fx, fy,
        angles='xy',
        scale_units='xy',
        scale=1,
        label=f"F{i}"
    )

# Plot resultant vector in red
plt.quiver(
    0, 0,
    sum_fx, sum_fy,
    angles='xy',
    scale_units='xy',
    scale=1,
    color='red',
    label='Resultant'
)

limit = max(abs(sum_fx), abs(sum_fy), 30) + 10

plt.xlim(-limit, limit)
plt.ylim(-limit, limit)

plt.grid(True)
plt.gca().set_aspect("equal")
plt.legend()

plt.title("Resultant of Forces")
plt.xlabel("Fx (N)")
plt.ylabel("Fy (N)")

plt.show()
