# Este script es para cambiar la dirección de un esclavo, por defecto es 1 y puede repetirse por lo que da errores.
# Para conectar en daisy chain no hay muchos problemas pero igual es necesario poner un resistencia para distancias largas de cable.
import minimalmodbus
import serial

# Configure the serial port
port = 'COM7'  # Change this to the appropriate COM port on your system
baudratevar = 9600
ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)

# Configure the Modbus RTU instrument
slave_address = 1  # Change this to the slave address of your Modbus device // valor de 1 a 247
instrument = minimalmodbus.Instrument(ser, slave_address, mode='rtu', close_port_after_each_call=True)

# Read holding registers
register_address = 253 # Es el registro especifico de lectura escritura de la dirección.
direccion_nueva = 7  # Cambiar a la nueva dirección

try:
    instrument.write_register(register_address, direccion_nueva)

except Exception as e:
    print(f"Error reading Modbus register: {e}")

finally:
    # Close the serial port
    ser.close()