import numpy as np
from src.utils.grapher import continuous_plotter

def dft_propia(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    return np.exp(-2j * np.pi * k * n / N) @ x

def analizar_espectro(senal, fs, nombre):
    X = dft_propia(senal)
    N = len(senal)
    frecuencias = np.arange(N) * fs / N
    magnitudes = np.abs(X) / N
    
    mitad = N // 2
    delta_f = fs / N
    
    #picos principales
    picos = []
    for i in range(1, mitad-1):
        if magnitudes[i] > magnitudes[i-1] and magnitudes[i] > magnitudes[i+1] and magnitudes[i] > 0.001:
            picos.append((frecuencias[i], magnitudes[i]))
    picos.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\n{nombre.upper()}: Δf = {delta_f:.4f} Hz, N = {N}")
    print("Picos principales:")
    for i, (f, a) in enumerate(picos[:3], 1):
        print(f"  {f:.2f} Hz - Amplitud: {a:.4f}")
    
    return frecuencias[:mitad], magnitudes[:mitad], delta_f

def examen_p1():
    print("PARTE 1: ANÁLISIS DE SEÑAL CON DFT")
    
    fm, fc, m, fs, duracion = 0.5, 8.0, 0.5, 80.0, 10.0
    
    t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)
    senal = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)
    
    frecuencias, magnitudes, delta_f = analizar_espectro(senal, fs, "Señal modulada")
    continuous_plotter(t, senal, f'x(t) = [1+{m}cos(2π{fm}t)]sin(2π{fc}t)', "", "Tiempo (s)", "Amplitud")
    continuous_plotter(frecuencias, magnitudes, f'Espectro (Δf={delta_f:.3f}Hz)', "", "Frecuencia (Hz)", "Magnitud")

def examen_p2():
    print("PARTE 2: ANÁLISIS DE SEÑAL CON RUIDO CON DFT")
    
    fs, duracion, f1, f2 = 256.0, 6.0, 8.0, 20.0
    
    n = np.arange(int(fs * duracion))
    t = n / fs
    señal_base = np.sin(2 * np.pi * f1 * t) + 0.8 * np.sin(2 * np.pi * f2 * t)
    
    #ruido
    ruido = 0.3 * np.sin(2 * np.pi * 35.0 * t)
    señal_con_ruido = señal_base + ruido
    
    frecuencias_base, magnitudes_base, delta_f = analizar_espectro(señal_base, fs, "Señal base")
    frecuencias_ruido, magnitudes_ruido, _ = analizar_espectro(señal_con_ruido, fs, "Señal con ruido")
    
    continuous_plotter(t, señal_base, f'sin(2π{f1}t) + 0.8sin(2π{f2}t)', "", "Tiempo (s)", "Amplitud")
    continuous_plotter(frecuencias_base, magnitudes_base, f'Espectro base (Δf={delta_f:.3f}Hz)', "", "Frecuencia (Hz)", "Magnitud")
    continuous_plotter(t, señal_con_ruido, 'Señal con ruido a 35Hz', "", "Tiempo (s)", "Amplitud")
    continuous_plotter(frecuencias_ruido, magnitudes_ruido, f'Espectro con ruido (Δf={delta_f:.3f}Hz)', "", "Frecuencia (Hz)", "Magnitud")
