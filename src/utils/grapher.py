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


def continuous_plotter(t, señal_modificada, titulo, subtitulo, xlabel, ylabel, señal_referencia=None):
    plt.figure(figsize=(8, 4))

    # Señal modificada 
    plt.plot(t, señal_modificada, label=subtitulo, color='blue', linewidth=2)

    # Señal de referencia
    if señal_referencia is not None:
        plt.plot(t, señal_referencia, linestyle='--', color='red', label='Señal de referencia')

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()



def discrete_plotter(n, señal_modificada, señal_referencia, titulo, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.stem(n, señal_modificada, linefmt='b-', markerfmt='bo', basefmt="k", label='Señal modificada')
    plt.stem(n, señal_referencia, linefmt='r--', markerfmt='ro', basefmt="k", label='Señal de referencia')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
