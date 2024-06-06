import bluetooth
import argparse

def create_fake_access_point(name, mac_address):
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind((mac_address, 1))
    server_sock.listen(1)

    print(f"Fake access point created with name: {name} and MAC address: {mac_address}")

    while True:
        client_sock, address = server_sock.accept()
        print(f"Accepted connection from {address}")

        while True:
            data = client_sock.recv(1024)
            if not data:
                break

            print(f"Received data: {data}")

        client_sock.close()
        print(f"Connection from {address} closed")

def main():
    parser = argparse.ArgumentParser(description="Bluetooth Fake Access Point Tool")
    parser.add_argument("name", help="Name of the fake access point")
    parser.add_argument("mac_address", help="MAC address of the fake access point")

    args = parser.parse_args()

    create_fake_access_point(args.name, args.mac_address)

if _name_ == "_main_":
    main()
