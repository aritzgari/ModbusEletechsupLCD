import time
import minimalmodbus
import serial
# Configure the serial port
port = 'COM7'  # Change this to the appropriate COM port on your system
baudratevar = 9600
esclavos = {}
x=6
listaesclavos = [i for i in range(1, x+1)]

#Generar el diccionario con la lista de registros
for esclavo_id in listaesclavos:
    esclavos [esclavo_id]= {
        'registro': esclavo_id,
        'valor': 0
    }

#Función que muestra por pantalla cuando un valor a cambiado 
def detectarcambios():
    while True:
        for esclavo_id, esclavos_info in esclavos.items():
            try:
                # Read holding registers
                register_address = 7  # Change this to the register address you want to read
                number_of_registers = 0 #
                direccion=esclavos_info['registro']
                # Create and configure the serial port
                ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
                instrument = minimalmodbus.Instrument(ser, direccion, mode='rtu', close_port_after_each_call=True)
                # Read the registers
                value = instrument.read_register(register_address, number_of_registers)
                if esclavos[esclavo_id]['valor'] != value:
                    if esclavos[esclavo_id]['valor'] !=0:
                        print(f"Valor diferente en el esclavo {esclavos[esclavo_id]['registro']} antes {esclavos[esclavo_id]['valor']} ahora {value}")
                    esclavos[esclavo_id]['valor'] = value
            except Exception as e:
                print(f"Error reading Modbus register for esclavo {esclavo_id}: {e}")
            finally:
                # Close the serial port
                ser.close()
        time.sleep(1)
detectarcambios()
        
        