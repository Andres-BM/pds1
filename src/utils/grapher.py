import matplotlib.pyplot as plt

def graficar_senal(t, señal_cont, n, señal_disc, tn, título):
    """
    Grafica una señal continua, su versión discreta y su superposición.
   
    Args:
        t (array): Tiempo continuo.
        señal_cont (array): Señal analógica.
        n (array): Índices discretos.
        señal_disc (array): Señal discreta.
        tn (array): Tiempo discreto (n*ts).
        título (str): Título descriptivo de la señal.
    """
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(hspace=0.6)

    # Señal continua
    plt.subplot(3, 1, 1)
    plt.plot(t, señal_cont, '-b', lw=2)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title(f"{título} (Continua)")
    plt.grid()

    # Señal discreta
    plt.subplot(3, 1, 2)
    plt.stem(n, señal_disc, linefmt='r', markerfmt='r.', basefmt="k")
    plt.xlabel('Índice de muestra (n)')
    plt.ylabel('Amplitud')
    plt.title("Señal Discreta")
    plt.grid()

    # Superposición
    plt.subplot(3, 1, 3)
    plt.plot(t, señal_cont, '-b', lw=2, label='Continua')
    plt.stem(tn, señal_disc, linefmt='r', markerfmt='r.', basefmt="k", label='Discreta')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title("Comparación: Continua vs. Discreta")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()