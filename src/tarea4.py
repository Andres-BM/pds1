import numpy as np
from src.utils.grapher import continuous_plotter

def calcular_dac(bits):
    VFS = 5.0
    niveles = 2 ** bits
    paso = VFS / (niveles - 1)
    resolucion = 100 / (niveles - 1)

    entradas = np.arange(niveles)
    salidas_analogicas = entradas * paso

    print("\nResultados del DAC: ")
    print(f"Bits: {bits}")
    print(f"Niveles: {niveles}")
    print(f"Tama\u00f1o del paso: {paso:.4f} V")
    print(f"Resoluci\u00f3n: {resolucion:.4f} %")

    
    titulo = f"Salida Anal\u00f3gica del DAC de {bits} bits"
    continuous_plotter(entradas, salidas_analogicas, titulo,
                       "DAC Output", "Entrada Digital", "Voltaje de Salida [V]")
