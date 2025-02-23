import numpy as np
import matplotlib.pyplot as plt

def plot_response(filename):
    # Cargar los datos desde el archivo, omitiendo la primera fila (encabezados)
    data = np.loadtxt(filename, skiprows=1)
    
    # Extraer columnas
    time = data[:, 0]
    v_escalon = data[:, 1]
    v_out = data[:, 2]
    
    # Crear la figura y graficar
    plt.figure(figsize=(10, 5))
    plt.plot(time, v_escalon, label='Señal Entrada: Escalon', linestyle='dashed', linewidth=3)
    plt.plot(time, v_out, label='Señal de Salida: (V_out)',color = 'red', linewidth=3)
    
    # Etiquetas y leyenda
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Tensión (V)')
    plt.title('Respuesta del Circuito')
    plt.legend()
    plt.grid()
    
    # Mostrar la gráfica
    plt.show()

# Llamada a la función con el nombre del archivo
def main():
    filename = 'Simulaciones Ltspice/TP/RTA_escalon.txt'  # Cambia esto al nombre de tu archivo
    plot_response(filename)

if __name__ == "__main__":
    main()
