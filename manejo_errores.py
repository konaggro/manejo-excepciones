num1 =input("Ingrese el primer número:")
num2 =input("Ingrese el segundo número:")


try:
    num1 = float(num1)
    num2 = float(num2)

    resultado = num1 / num2

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

except ValueError:
    print("Error: Por favor, ingrese números válidos.")

else:
    print(f"El resultado de la división es: {resultado}")

class CustomError(Exception):
    pass

def validar_dato(dato):
    if edad <0:
      raise CustomError("Error: La edad no puede ser negativa.")  
    else:
        print("Dato válido.")

try:
    edad = int(input("Ingrese su edad: "))
    validar_dato(edad)  

except CustomError as e:
    print(f"Se ha producido un error personalizado: {e}")

except ValueError:
    print("Error: Por favor, ingrese un número válido para la edad.")

try:
    print("Intentando acceder a un índice fuera de rango...")

    x= 10/0 

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

finally:
    print("Este bloque se ejecuta siempre, independientemente de si ocurrió un error o no.") 



