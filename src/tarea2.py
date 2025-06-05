import numpy as np
from src.utils.grapher import continuous_plotter

def graficar_onda(frecuencia_deseada):

    #Parámetros de la señal
    amplitud = 1.0 
    frecuencia = float(frecuencia_deseada)
    t = np.linspace(0.0, 5.0, 1000)
    xt = amplitud * np.sin(2 * np.pi * frecuencia * t)

    titulo = f"Onda Senoidal Continua - Frecuencia: {frecuencia} Hz"
    subtitulo = "Señal senoidal"
    xlabel = "Tiempo [s]"
    ylabel = "Amplitud"

    #Llamada a la función de graficado
    continuous_plotter(t, xt, titulo, subtitulo, xlabel, ylabel)
