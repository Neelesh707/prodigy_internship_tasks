from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        protocol = packet['IP'].proto

        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {protocol}")
        
        if packet.haslayer('Raw'):
            payload_data = packet['Raw'].load
            print(f"Payload: {payload_data}")

def start_sniffing(interface=None):
    print("Starting packet sniffing...")
    sniff(iface=interface, prn=process_packet, store=False)

start_sniffing()
