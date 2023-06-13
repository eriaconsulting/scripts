import subprocess
import time

def check_service(service_name):
    try:
        # Verificar si el servicio está en ejecución utilizando el comando pgrep
        subprocess.check_output(['pgrep', service_name])
        return True
    except subprocess.CalledProcessError:
        return False

def restart_system():
    # Reiniciar el equipo utilizando el comando adecuado para tu sistema operativo
    subprocess.call(['sudo', 'reboot'])

def monitor_service(service_name):
    while True:
        if not check_service(service_name):
            print(f"El servicio {service_name} no está en funcionamiento. Reiniciando el equipo...")
            restart_system()
        else:
            print("Chromium-browser está activo")
        # Esperar 5 segundos antes de verificar nuevamente
        time.sleep(5)

if __name__ == '__main__':
    service_name = 'chromium'
    monitor_service(service_name)
