# En funktion som bygger konfigurationen for ett enda VLAN.
def vlan_config(number, name):
    rader = []
    rader.append(f"vlan {number}")
    rader.append(f" name {name}")
    return rader
# Naten pa Nordvik. Byt ut mot era egna.
vlans = {
    10: "KONTOR",
    20: "EKONOMI",
    30: "GAST",
    99: "DRIFT",
}
# Kor funktionen en gang per VLAN och skriv ut resultatet.
for number in vlans:
    for rad in vlan_config(number, vlans[number]):
        print(rad)
