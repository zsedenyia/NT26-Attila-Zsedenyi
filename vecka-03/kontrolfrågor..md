# 1. Vad säger en Ip-Address som en MAC-address inte säger?
     Mac-address är fysiska-hardvaruidentität. Ip-Address säger var ligger dator eller enhet i LAN eller i världet.

# 2. Vad gör netmasken?
     Det delar up en /24 nätverk till två mindre nätverk eller fyra, det bli /26.

# 3. Vilken address i en nät får ingen enhet ha, och varför är det två stycken?
     Netaddressen och Broadcast address.

# 4. Vad är blocksteget för /26, och vad användar du det till?
     subnet 1  192.168.1.0     användbar 192.168.1.1.-62.  Broadcast .63
     subnet 2  192.168.1.64    användbar 192.168.1.65-126. Broadcast .127
     subnet 3  192.168.1.128   användbar 192.168.1.129-190 Broadcast .191
     subnet 4  192.168.1.192   användbar 192.168.1.193-254 Broadcast .255

# 5. Varför måste Gatewayen ligga i samma nät som du?
    Gateway skicka (routa) packet från LAN till WAN. Om gateway är olika nummer, sin dator kan inte gå ut till internet.

# 6. Vad händer med en dator som har rätt address men ingen Gateway.
    Denna dator kan bara prata på local-LAN. (Finns inte dörr till internet).

# 7. Vilka fyra saker får en dator av DHCP, och vilken av dem säger hur länge de gäller?
     Ip-address, nätmask, default-Gateway och DNS-server. DHCP bara "hyr ut" ip addresser. typ 8-timmar, 24-timmar eller 8-dagar. 
     På halv-tiden, dator automatiskt kontakta DHCP-servern för att förnya (förlänga) sitt lån av ip-address så behöver inte att byta IP-address.

# 8. Vilka enheter ska ha statisk address, och varför?
     Nätverk-skrivare, Nas och servrar. De bhöver att sitta fasta på samma ip-address konstant så de kan nås hela tiden.

     
     
