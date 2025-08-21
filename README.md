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
   -  tres gráficas en una misma figura que mostraran:
      - Señal continua
      - Señal discreta
      - Superposición de ambas
   - Incluye elementos gráficos como:
     - Títulos descriptivos
     - Ejes etiquetados
     - Cuadrículas de referencia
     - Leyendas explicativas


**tarea2:** Graficación de Señales Senoidales Continuas
En esta tarea se genera una señal senoidal continua en función de la frecuencia proporcionada por el usuario.  
Se observa cómo varía la señal al cambiar su frecuencia.

-   **Ecuación utilizada**:  
    x(t)=A⋅sin⁡(2πft)
    
-   **Parámetros definidos**:
    
    -   Amplitud (A): 1
        
    -   Fase (ϕ): 0
        
    -   Frecuencias de prueba: 1 Hz, 2 Hz, 5 Hz
        
    -   Tiempo continuo: 0.0 a 5.0 segundos


**-Para ejecutar tarea2**
```bash
  python main.py tarea2 <frecuencia>
```
**Ejemplo**
```bash
  python main.py tarea2 2
```
**-Al ejecutar podrás ver:**
-   Una gráfica continua
    
-   Título con la frecuencia actual
    
-   Ejes etiquetados: `"Tiempo [s]"` y `"Amplitud"`
    
-   Cuadrícula y leyenda


### **tarea3: Señal Continua y Discreta con Parámetros Personalizados**

En esta tarea se genera una señal senoidal con parámetros definidos por el usuario: amplitud, frecuencia y fase.  
Además, se compara visualmente con una señal de referencia en forma continua y discreta.

-   **Ecuaciones utilizadas**:
    
    -   Continua: x(t)=A⋅sin⁡(2πft+ϕ)
        
    -   Discreta: x[n]=A⋅sin⁡(2πfnTs+ϕ)
-   **Parámetros a definir**:
    
    -   Amplitud (A)
        
    -   Frecuencia (f)
        
    -   Fase (ϕ) en radianes
        
    -   Período de muestreo: Ts = 0.01 s
        
    -   Tiempo continuo: 0 a 2 s
        
    -   Discreto: 0 a 200 muestras
    
    
**-Para ejecutar tarea3**
```bash
 python main.py tarea3 <amplitud> <frecuencia> <fase>
```
**Ejemplo**
```bash
  python main.py tarea3 1 2 0.785
```
**Al ejecutar se muestran**:

-   Una gráfica de la señal continua (modificada y referencia)
    
-   Una gráfica de la señal discreta (modificada y referencia)
    
-   Título con los parámetros
    
-   Ejes etiquetados
    
-   Leyenda que diferencia ambas señales


### **tarea4: Simulación de un DAC (Digital-to-Analog Converter)**

En esta tarea se simula un DAC que convierte una entrada digital a una salida analógica.  
Se calcula la resolución, el tamaño del paso, y se grafica la salida analógica.

-   **Fórmulas utilizadas**:
    
    -   Niveles: 2^N
        
    -   Paso: VFS/(2^N - 1)
        
    -   Resolución: 100/(2^N - 1)%
        
-   **Parámetros definidos**:
    
    -   Voltaje de escala completa: VFS = 5 V
        
-   **Para ejecutar tarea4**:
```bash
 python main.py tarea4 <bits>
```
**Ejemplo**
```bash
  python main.py tarea4 8
```
-   **Al ejecutar se muestra**:
    
    -   Tabla con:
        
        -   Número de niveles
            
        -   Tamaño del paso
            
        -   Resolución porcentual
            
    -   Gráfica tipo rampa
        
    -   Ejes etiquetados: `"Nivel digital de entrada"` y `"Voltaje analógico [V]"`
        
    -   Título con el número de bits

## EXAMEN: Transformada de Fourier Discreta
**examen parte 1:** 
**Objetivo:**
-   Aplicar la Transformada de Fourier Discreta (DFT) a señales muestreadas
    
-   Identificar picos espectrales, estimar frecuencias y amplitudes relativas
    
-   Calcular y usar la resolución en frecuencia (Δf = fₛ/N)
    

**Señal analizada:**  
x(t) = [1 + m_cos(2π_fm_t)]_sin(2π_fc_t)

**Parámetros:**

-   fm = 0.5 Hz
    
-   fc = 8 Hz
    
-   m = 0.5
    
-   fs = 80 Hz
    
-   Duración = 10 s

**-Para ejecutar examen parte 1**
```bash
python main.py examen_p1
```
**-Al ejecutar podrás ver:**
-   Gráfica de la señal modulada en tiempo
    
-   Espectro de frecuencia con identificación de picos
    
-   Cálculo de resolución espectral Δf
    
-   Listado de frecuencias y amplitudes principales

**examen parte 2:** 
**Objetivo:**

-   Generar una señal discreta y agregarle ruido de frecuencia específica
    
-   Analizar su espectro con la DFT
    
-   Identificar picos en presencia de ruido
    
-   Estimar la resolución (Δf = fₛ/N)

**Señal base:**  
x[n] = sin(2π*8*n*ts) + 0.8*sin(2π*20*n*ts)

**Ruido añadido:**  
0.3_sin(2π_40*n*ts)

**Parámetros:**

-   Frecuencia de muestreo: fₛ = 256 Hz
    
-   Duración: 6 s → N = 1536 muestras
    
-   Frecuencias: f₁ = 8 Hz, f₂ = 20 Hz
    
-   Ruido: 40 Hz con amplitud 0.3
    
**-Para ejecutar examen parte 2**
```bash
 python main.py examen_p2
```

**Al ejecutar se muestran**:

-   Gráficas de señal base y señal con ruido
    
-   Espectros de frecuencia comparativos
    
-   Identificación de componentes originales y ruido
    
-   Análisis de resolución espectral
