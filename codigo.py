import serial
import csv

blackpill_port = "/dev/ttyACM0"
baud = 115200

data = serial.Serial(blackpill_port, baud)
print("Conexion exitosa en puerto: " + blackpill_port)

csvname = "sglicechido.csv"
print("Medición:")
n = input()
print("SIS:")
sis = input()
hdata = "med:" + str(n) + ", sis:" + str(sis)

# Abre el archivo CSV en modo append
with open(csvname, "a", newline="", encoding='UTF8') as file:
    writer = csv.writer(file)
    
    # Escribe las cabeceras solo una vez al inicio
    writer.writerow([hdata, "n°", "V"])

print("Archivo creado y/o abierto")
linea = 0

# Envía el caracter 'm' al dispositivo
caracter = b'm'
data.write(caracter)

# Loop principal
while True:
    # Verifica si hay datos disponibles en el puerto serie
    if data.inWaiting() > 0:
        # Lee una línea de datos
        getData = data.readline().decode().strip()
        adata = getData.split(',')
        
        # Escribe los datos en el archivo CSV
        with open(csvname, "a", newline="", encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(adata)
        
        print(adata)
        linea += 1  # Incrementa el contador de línea

# Cierra la conexión serial
data.close()