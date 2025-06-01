import numpy as np
from scipy.signal import sawtooth, square
from src.utils.grapher import graficar_senal

def generar_senales():
    "Genera y grafica señales continuas y discretas"
    # Parámetros comunes
    f = 2
    fs = 40.0
    ts = 1.0 / fs
    t = np.linspace(-1.0, 5.0, 1000)
    n = np.arange(-40, 201)
    tn = n * ts

    # Definición de señales
    señales = [
        {
            "título": "x₁(t) = sin(2πft) — Señal sinusoidal",
            "cont": np.sin(2 * np.pi * f * t),
            "disc": np.sin(2 * np.pi * f * tn)
        },
        {
            "título": "x₂(t) = e^(–2t)·u(t) — Señal exponencial con escalón",
            "cont": np.exp(-2 * t) * (t >= 0),
            "disc": np.exp(-2 * tn) * (tn >= 0)
        },
        {
            "título": "x₃(t) = tri(t,f) — Señal triangular periódica",
            "cont": sawtooth(2 * np.pi * f * t, width=0.5),
            "disc": sawtooth(2 * np.pi * f * tn, width=0.5)
        },
        {
            "título": "x₄(t) = sq(t,f) — Señal cuadrada periódica",
            "cont": square(2 * np.pi * f * t),
            "disc": square(2 * np.pi * f * tn)
        }
    ]

    # Graficar cada señal
    for señal in señales:
        graficar_senal(t, señal["cont"], n, señal["disc"], tn, señal["título"])

if __name__ == "__main__":
    generar_senales()