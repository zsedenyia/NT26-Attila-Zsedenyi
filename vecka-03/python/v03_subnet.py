import ipaddress

# Byt ut mot det nat du vill rakna pa.
text = "10.0.0.6/30"

# Modulen ipaddress gor rakningen at dig.
net = ipaddress.ip_network(text, strict=False)

# Alla adresser du kan ge till en enhet.
usable = list(net.hosts())

print(f"Nat:            {net.network_address}")
print(f"Natmask:        {net.netmask}")
print(f"Broadcast:      {net.broadcast_address}")
print(f"Forsta adress:  {usable[0]}")
print(f"Sista adress:   {usable[-1]}")
print(f"Antal enheter:  {len(usable)}")





