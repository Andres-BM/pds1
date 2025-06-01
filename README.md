## PDS: Actividades y Tareas

## Estructura del proyecto
├── main.py  
├── src/  
│ ├── utils/  
│ │ └── grapher.py  
│ └── tarea1.py


## Requisitos
- Python 3.8+
- Bibliotecas:
  - numpy
  - matplotlib
  - scipy
Estas bibliotecas están en el archivo requirements.txt

## Instalación
 - Clonar el repositorio 
```bash
git clone https://github.com/Andres-BM/pds1.git
cd pds1
```
 - Crea y activa un entorno virtual
 ``` bash
 py -m venv venv
source venv/bin/activate
```
 - Instalar dependencias:
   ```bash
   pip install -r requirements.txt

## uso
**tarea1:** Graficación de Señales Continuas y Discretas
en esta tarea se generaran cuatro gráficas de señales diferentes, tanto en forma continua como discreta y su superposición de ambas.

-Señales que se generarán:
1.  Sinusoidal: x₁(t) = sin(2πft)
    
2.  Exponencial: x₂(t) = e^(–2t)·u(t)
    
3.  Triangular: x₃(t) = tri(t,f)
    
4.  Cuadrada: x₄(t) = sq(t,f)

-Que tendrá los siguientes parámetros 
-   Frecuencia (f): 2 Hz
    
-   Frecuencia de muestreo (fs): 40 Hz
    
-   Tiempo continuo: -1.0 a 5.0 segundos
    
-   Muestras discretas: -40 a 200 índices

**-Para ejecutar tarea1**
```bash
  python main.py 
```
**-Al ejecutar podrás ver:**
   - Para cada señal muestra 3 gráficos en una misma figura:
     1. Señal continua
     2. Señal discreta
     3. Superposición de ambas
   - Incluye elementos gráficos como:
     - Títulos descriptivos
     - Ejes etiquetados
     - Cuadrículas de referencia
     - Leyendas explicativas
