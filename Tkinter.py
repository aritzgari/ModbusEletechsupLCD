import tkinter as tk
import minimalmodbus
import serial
# Create the main window
window = tk.Tk()
window.title("7 Segmentos")

def button_click():
    slave_address = int(slave_entry.get())
    register_address = int(register_entry.get())
    value_to_write=int(value_entry.get())
    # Configure the serial port
    port = 'COM7'  # Change this to the appropriate COM port on your system
    baudratevar = 9600
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
    # Configure the Modbus RTU instrument
    instrument = minimalmodbus.Instrument(ser, slave_address, mode='rtu', close_port_after_each_call=True)
    try:
        # Write to the register
        instrument.write_register(register_address, value_to_write)
        
        # Print the result
        print(f"Value {value_to_write} written to register {register_address}")

    except Exception as e:
        print(f"Error writing to Modbus register: {e}")

    finally:
        # Close the serial port
        ser.close()
        
#Label del esclavo
slave_label = tk.Label(window, text="Slave Adress:")
slave_label.grid(row=0, column=0, padx=10, pady=5)
#Entrada del esclavo
slave_entry = tk.Entry(window)
slave_entry.grid(row=0, column=1, padx=10, pady=5)

#Label del registro
register_label = tk.Label(window, text="Segmento (0 o 1):")
register_label.grid(row=1, column=0, padx=10, pady=5)
#Entrada del registro
register_entry = tk.Entry(window)
register_entry.grid(row=1, column=1, padx=10, pady=5)

#Label del valor
value_label = tk.Label(window, text="Value to write (mirar tabla):")
value_label.grid(row=2, column=0, padx=10, pady=5)
#Entrada del valor
value_entry = tk.Entry(window)
value_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to trigger an action
button = tk.Button(window, text="Introducir", command=button_click)
button.grid(row=3, column=0, columnspan=2, pady=10)


# Start the tkinter event loop
window.mainloop()