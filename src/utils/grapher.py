import matplotlib.pyplot as plt

def graficar_senal(t, señal_cont, n, señal_disc, tn, título):

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
    plt.stem(tn, señal_disc, linefmt='r', markerfmt='r.', basefmt="k", label='Discreta')
    plt.plot(t, señal_cont, '-b', lw=2, label='Continua')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title("Comparación: Continua y Discreta")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()