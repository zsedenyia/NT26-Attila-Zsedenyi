# Uppslagstabell: tillverkarprefix -> namn.
# Fyll pa med de prefix du hittar i switchens MAC-tabell.
vendors = {
"a4:c3:f0": "Intel",
"3c:d9:2b": "Hewlett-Packard",
"00:1a:a1": "Cisco Systems",
}
# Adresserna du vill sla upp. Byt ut mot dina egna.
addresses = [
"a4:c3:f0:11:3a:b7",
"3c:d9:2b:d2:11:88",
"8c:85:90:44:12:0e",
]
for address in addresses:
# De forsta atta tecknen ar tillverkarprefixet.
prefix = address[0:8]
# Finns prefixet i tabellen? Annars skriver vi "okand".
if prefix in vendors:
name = vendors[prefix]
else:
name = "okand tillverkare"
print(f"{address}
->
{name}")
