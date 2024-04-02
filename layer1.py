class Device:
  def __init__(self, name,mac_address):
    self.name = name
    self.mac_address=mac_address
    self.buffer = []

  def send(self, data, destination):
    packet = {"source": self.name, "destination": destination, "data": data}
    self.buffer.append(packet)


  def receive(self):
    if self.buffer:
      packet = self.buffer.pop(0)
      print(f"{self.name} received data: {packet['data']} from {packet['source']}")



class Hub:
  def __init__(self):
    self.connected_devices = []

  def connect(self, device):
    self.connected_devices.append(device)
    # print(self.connected_devices)
  def transmit(self):
    if self.connected_devices:
      # Iterate through a copy of connected_devices to avoid modification issues
      for device in list(self.connected_devices):
        if device.buffer:
          packet = device.buffer.pop(0)
          for connected_device in self.connected_devices:
            if connected_device != device:
              connected_device.buffer.append(packet.copy())

# Example Usage
device1 = Device("Device 1","1111111")
device2 = Device("Device 2","222222")
device3 = Device("Device 3","333333")
hub = Hub()
hub.connect(device1)
hub.connect(device2)
hub.connect(device3)

device1.send("Hello from Device 1!", "Device 2")
hub.transmit()
device2.receive()  # Call receive before transmit to ensure data is present
device3.receive()

# Output: Device 2 received data: Hello from Device 1! from Device 1
