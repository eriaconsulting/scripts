import time

def obtener_temperatura():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as archivo:
            temperatura_raw = archivo.read()
            temperatura = int(temperatura_raw) / 1000.0
            return temperatura
    except FileNotFoundError:
        print("No se puede acceder a la temperatura de la CPU.")
        return None

def monitorizar_temperatura():
    temperatura_maxima = 0
    
    while True:
        temperatura_actual = obtener_temperatura()
        
        if temperatura_actual is not None and temperatura_actual > temperatura_maxima:
            temperatura_maxima = temperatura_actual
            print(f"Temperatura: {temperatura_maxima}")
            # Escribir la temperatura máxima en el archivo de texto
            with open('temperatura_maxima.txt', 'w') as archivo:
                archivo.write(str(temperatura_maxima))
        
        # Esperar 5 minutos
        time.sleep(300)

monitorizar_temperatura()
