# 1.  Vad är skillnaden mellan ett VLAN och ett IP-nät?
      Vlan är layer-2. En ram som kommer in på en port i VLAN 10 släps bara ut på andra portar i VLAN 10.
      IP-nät är layer-3 och det handlar om addresserna. Vilket subnät en enhet tillhör, avgjört av IP-address och nätmask.

# 2.  Vad skiljer en access-port från en trunk?
      Access-port tillhör ett enda VLAN.
      Trunk-port bär flera VLANs samtidigt över samma kabel. (dot1q)

# 3.  Vilka två rader behövs för att lägga en port i ett VLAN, och varför räcker inte den ena?
      Switchport mode access - Denna kommando säger att porten är en access-port - men säger inte vilken.
      Switchport access vlan 10 - denna kommando säger vilket VLAN porten ska tillhöra
      show vlan brief - porten ska stå listad på raden för rätt VLAN-numme, inte kvar på VLAN-1 raden-

# 4.  Vad gör taggningen, och var i nätet finns taggen?
      Taggen finns i rammen och det användas bara i trunk portarna. Mellan switch och router eller mellan switch och en annan switch.
      Sista switch, var trunk slutar, läser taggen och vet att ramen måste gå till access port VLAN-10 till exempel.

# 5.  Varför ska en trunk aldrig kopplas till en dator?
      Trunk portarna bära flera VLANs samtidigt. (Det är en korridoren). Alla ram bära egen VLAN tag.
      Om vi koppla en dator på andra slutet, datorens NIC ska inte förstår VLAN tag och det ska inte funkar allt.

# 6.  Vad är native VLAN, och vad är standardvärdet?
      Native VLAN är det VLAN vilken otaggat över trunken. Det finns ett per Trunk.
      Rammar som kommer in på trunken otaggade, det automatisk i native VLAN.
      På alla Cisco switchar standard värde är VLAN 1.

# 7.  Vad går fel om två switchar har olika native VLAN?
      Det ska inte funkar 100% korrekt och kan ledas till data läkage. Resten av nätverk i trunk ska funkar bra. 
      Cisco router ska log en error också.

# 8.  Vad förhindrar STP, och hur gör den det?
      
