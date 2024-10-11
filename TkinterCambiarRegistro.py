import tkinter as tk
import minimalmodbus
import serial

baudratevar = 9600

# Create the main window
window = tk.Tk()
window.title("Cambio de registro del LCD")
direccion=0
def button_click():
    global direccion
    com = int(comentry.get())
    port = 'COM'+str(com)  # Change this to the appropriate COM port on your system
    i=0
    for i in range(1,256):
        ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
        # Configure the Modbus RTU instrument
        instrument = minimalmodbus.Instrument(ser, i, mode='rtu', close_port_after_each_call=True)
        try:
            instrument.read_register(7, 0)
            direccion=i
            break
        except Exception as e:
            print(f"------Cargando------")
        finally:
            # Close the serial port
            ser.close()
    direccionueva=int(nuevoregistroentry.get())
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
    
    # Configure the Modbus RTU instrument
    slave_address = direccion  # Change this to the slave address of your Modbus device // valor de 1 a 247
    instrument = minimalmodbus.Instrument(ser, slave_address, mode='rtu', close_port_after_each_call=True)
    
    try:
        instrument.write_register(253, direccionueva)
    except Exception as e:
        print(f"Error reading Modbus register: {e}")
    finally:
        # Close the serial port
        ser.close()
        
    ser2 = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
    instrument2 = minimalmodbus.Instrument(ser2, direccionueva, mode='rtu', close_port_after_each_call=True)
    try:
        instrument2.write_register(7, direccionueva)
        print("La nueva dirección es: "+str(direccionueva))
    except Exception as e:
        print(f"Error reading Modbus register: {e}")

    finally:
        # Close the serial port
        ser2.close() 

              
#Label del esclavo
comlabel = tk.Label(window, text="Número del puerto COM (comprobar administrador de dispositivos):")
comlabel.grid(row=0, column=0, padx=10, pady=5)
#Entrada del esclavo
comentry = tk.Entry(window)
comentry.grid(row=0, column=1, padx=10, pady=5)

#Label del valor
nuevoregistrolabel = tk.Label(window, text="Nuevo registro:")
nuevoregistrolabel.grid(row=2, column=0, padx=10, pady=5)
#Entrada del valor
nuevoregistroentry = tk.Entry(window)
nuevoregistroentry.grid(row=2, column=1, padx=10, pady=5)

# Button to trigger an action
buttonexec = tk.Button(window, text="Ejecutar", command=button_click)
buttonexec.grid(row=3, column=0, columnspan=1, pady=10)

descripcion = tk.Label(window, text="Si se ejecuta correctamente podrás ver el numero del nuevo registro.")
descripcion.grid(row=4, column=0, padx=10, pady=5)

# Start the tkinter event loop
window.mainloop()