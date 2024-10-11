import minimalmodbus
import serial

def write_one_register():
    # Configure the serial port
    port = 'COM7'  # Change this to the appropriate COM port on your system
    baudratevar = 9600
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1) 
    
    # Configure the Modbus RTU instrument
    slave_address = 7  # Change this to the slave address of your Modbus device // de 1 a 247
    instrument = minimalmodbus.Instrument(ser, slave_address, mode='rtu', close_port_after_each_call=True)

    # Write to a holding register
    register_address = 7 # Change this to the register address you want to write to // el 7 es para enviarle un número // 8 es el blink // 9 es el brillo // 0-5 es para letras y demás según los códigos en el digito especificado
    value_to_write = 1  # Change this to the value you want to write

    try:
        # Write to the register
        instrument.write_register(register_address, value_to_write, functioncode=6)
        
        # Print the result
        print(f"Value {value_to_write} written to register {register_address}")

    except Exception as e:
        print(f"Error writing to Modbus register: {e}")

    finally:
        # Close the serial port
        ser.close()
        
write_one_register()