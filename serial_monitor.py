"""
serial_monitor.py

Display incoming serial port traffic

Requires port and baudrate arguments, for example:

    python serial_monitor.py COM8 115200

"""
import sys
import serial


def serial_connection(port_str, baud):
    """ Make serial port connection """
    connection = serial.Serial(
        port=port_str,
        baudrate=baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0)
    print("connected to: " + connection.portstr)
    return connection


def main():
    """ Main function """
    port = sys.argv[1]
    baudrate = int(sys.argv[2])
    connection = serial_connection(port, baudrate)
    line = ""
    # Main loop
    while True:
        in_byte = connection.readline()
        in_string = in_byte.decode("utf-8")
        if in_string != "":
            line += in_string
            if "\n" in in_string:
                print(line)
                line = ""
    connection.close()


if __name__ == "__main__":
    main()
