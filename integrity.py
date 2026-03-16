data = input("Enter data packet: ")

if data == data[::-1]:
    print("Data Integrity Verified: Packet is intact.")
else:
    print("Warning: Data corruption detected!")