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
Para ejecutar tarea_1
```bash
  python main.py 
```
Esto generará cuatro gráficas de señales diferentes, tanto en forma continua como discreta y su superposición de ambas:
1.  Sinusoidal: x₁(t) = sin(2πft)
    
2.  Exponencial: x₂(t) = e^(–2t)·u(t)
    
3.  Triangular: x₃(t) = tri(t,f)
    
4.  Cuadrada: x₄(t) = sq(t,f)
