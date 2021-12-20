import turtle
ws= turtle.Screen()
geekyTurtle= turtle.Turtle()



def generar_estrella(puntas):
    def calculo(puntas):
        angulo=0
        if puntas%2 == 0:
             angulo= 360 - (180/puntas)
        if puntas% 3 == 0:
            angulo= 120 + (180/puntas)
        else:
            pass
        return angulo

puntas= int(input("¿Cuántas puntas quieres que tenga la estrella?:"))
generar_estrella(puntas)