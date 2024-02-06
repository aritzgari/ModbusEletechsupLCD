import minimalmodbus
import serial

# Configure the serial port
port = 'COM7'  # Change this to the appropriate COM port on your system
baudratevar = 9600
registroesclavo=6 #Direccion del esclavo en el que escribir
       
# Configure the Modbus RTU instrument
ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
instrument = minimalmodbus.Instrument(ser, registroesclavo, mode='rtu', close_port_after_each_call=True)

# Write to a holding register
register_address = 9 # Change this to the register address you want to write to // el 7 es para enviarle un número
valor=1

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