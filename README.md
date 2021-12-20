# Estrellas-regulares
Mi dirreción de GitHub es: https://github.com/claudiaalozano/Estrellas-regulares.git

A continuación muestro un esquema previo para realizar el código de las estrellas regulares:
![Figma estrellas](https://user-images.githubusercontent.com/91722847/146838427-fecacb6d-3736-43da-b8a9-f090de0c9996.png)


El código finalmente realizado para las estrellas regulares es:
```import turtle
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
```
