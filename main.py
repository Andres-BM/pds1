import sys
from src.tarea1 import generar_senales
from src.tarea2 import graficar_onda
from src.tarea3 import graficar_senal_con_parametros
from src.tarea4 import calcular_dac
from src.examen_p1 import examen_p1, examen_p2
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <tarea> [argumentos]")
    elif sys.argv[1] == "tarea1":
        generar_senales()

    elif sys.argv[1] == "tarea2":
        if len(sys.argv) >= 3:
            frecuencia = float(sys.argv[2])
            graficar_onda(frecuencia)
        else:
            print("Falta argumento de frecuencia para tarea2")

    elif sys.argv[1] == "tarea3":
        if len(sys.argv) >= 5:
            A = float(sys.argv[2])
            f = float(sys.argv[3])
            phi = float(sys.argv[4])
            graficar_senal_con_parametros(A, f, phi)
        else:
            print("Uso: python main.py tarea3 <amplitud> <frecuencia> <fase>")

    elif sys.argv[1] == "tarea4":
        if len(sys.argv) >= 3:
            bits = int(sys.argv[2])
            calcular_dac(bits)
        else:
            print("Uso: python main.py tarea4 <bits>")
    
    elif sys.argv[1] == "examen_p1":
        examen_p1()

    elif sys.argv[1] == "examen_p2":
        examen_p2()

    else:
        print(f"Tarea desconocida: {sys.argv[1]}")