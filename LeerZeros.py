import minimalmodbus
import serial
# Configure the serial port
port = 'COM7'  # Change this to the appropriate COM port on your system
baudratevar = 9600

#Lista con el range de los esclavos que tengamos
x=6
listaesclavos = [i for i in range(1, x+1)]

for esclavo in listaesclavos:
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
    instrument = minimalmodbus.Instrument(ser, esclavo, mode='rtu', close_port_after_each_call=True)

    # Read holding registers
    register_address = 7 # Change this to the register address you want to read
    number_of_registers = 0  # Este número no cambiarlo el 0 es para que coja números 

    try:
        # Read the registers
        value = instrument.read_register(register_address, number_of_registers)
        
        # Print the result
        if value == 0:
            print(f"El esclavo {esclavo} está resetado.")
        else:
            print(f"Leido del esclavo {esclavo} : {int(value)}")
            
    except Exception as e:
        print(f"Error reading Modbus register: {e}")
        ser.close()


        
        
        