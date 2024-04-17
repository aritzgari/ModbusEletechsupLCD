import minimalmodbus
import serial

# Configure the serial port
port = 'COM7'  # Change this to the appropriate COM port on your system
baudratevar = 9600

""" esclavos = {}
x=6 #Cantidad de cacharros

#Esta seria una lista de esclavos que ppodría ser una lista
listaesclavos = [i for i in range(1, x+1)]

#Una lista de valores de cada esclavo (puede ser 0)
listavalores = [i for i in range(1, x+1)]

#Generar el diccionario con la lista de registros y valores
for slave_address in listaesclavos:
    esclavos [slave_address]= {
        'registro': slave_address,
        'valor': listavalores[slave_address-1]
    } """
    
#Función especifica que coje las dos variables de direccion y valor.
def escrituraenesclavos(direccion, valor):
    """ for esclavo_id, esclavos_valor in esclavos.items(): """
        
    # Configure the Modbus RTU instrument
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
    instrument = minimalmodbus.Instrument(ser, direccion, mode='rtu', close_port_after_each_call=True)

    # Write to a holding register
    register_address = 7 # Change this to the register address you want to write to // el 7 es para enviarle un número

    try:
        # Write to the register
        instrument.write_register(register_address, valor)
            
        # Print the result
        print(f"Value {valor} written to register {register_address}")

    except Exception as e:
        print(f"Error writing to Modbus register: {e}")

    finally:
        # Close the serial port
        ser.close()
            
escrituraenesclavos(6,0)