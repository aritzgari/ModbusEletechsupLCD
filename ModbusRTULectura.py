import minimalmodbus
import serial
while True:
    # Configure the serial port
    port = 'COM7'  # Change this to the appropriate COM port on your system
    baudratevar = 9600
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)

    # Configure the Modbus RTU instrument
    slave_address = 20  # Change this to the slave address of your Modbus device // valor de 1 a 247
    instrument = minimalmodbus.Instrument(ser, slave_address, mode='rtu', close_port_after_each_call=True)

    # Read holding registers
    register_address = 32 # Change this to the register address you want to read
    number_of_registers = 2  # Change this to the number of registers you want to read

    try:
        # Read the registers
        value = instrument.read_register(register_address, number_of_registers)

        # Print the result
        print(f"Value read from register {register_address}: {value}")
        
        if value==0:
            print("El valor está resetado.")

    except Exception as e:
        print(f"Error reading Modbus register: {e}")

    finally:
        # Close the serial port
        ser.close()