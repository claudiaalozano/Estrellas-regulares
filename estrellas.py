import turtle
puntas= int(input("¿Cuantas puntas quieres que tenga la estrella?:"))

def calculo(puntas):
    angulo=0
    if puntas%2 == 0:
        angulo= 360 - (180/puntas)
    if puntas% 3 == 0:
        angulo= 120 + (180/puntas)
    