# 1. Vad säger en Ip-Address som en MAC-address inte säger?
     Mac-address är fysiska-hardvaruidentität. Det betyder vad är enheten.Ip-Address säger var ligger dator eller enhet i LAN eller i världet. det betyder var är enheten i nätet.

# 2. Vad gör netmasken?
     Det delar up en /24 nätverk till två mindre nätverk eller fyra, det bli /26. eller mer mindre nätverk.

# 3. Vilken address i en nät får ingen enhet ha, och varför är det två stycken?
     Netaddressen och Broadcast address.

# 4. Vad är blocksteget för /26, och vad användar du det till?
     Blocksteget är 64. 0-64-128-192. Jag användar att dela upp ett/24 nät till 4 mindre subnet. 

# 5. Varför måste Gatewayen ligga i samma nät som du?
    Gateway skicka (routa) packet från LAN till WAN. Om gateway är olika nummer, dator kan inte gå ut till internet.

# 6. Vad händer med en dator som har rätt address men ingen Gateway.
    Denna dator kan bara prata på local-LAN. (Finns inte dörr till internet).

# 7. Vilka fyra saker får en dator av DHCP, och vilken av dem säger hur länge de gäller?
     Ip-address, nätmask, default-Gateway och DNS-server. DHCP bara "hyr ut" ip addresser. typ 8-timmar, 24-timmar eller 8-dagar. 
     På halv-tiden, dator automatiskt kontakta DHCP-servern för att förnya (förlänga) sitt lån av ip-address så behöver inte att byta IP-address.

# 8. Vilka enheter ska ha statisk address, och varför?
     Nätverk-skrivare, Nas och servrar. De bhöver att sitta fasta på samma ip-address konstant så de kan nås hela tiden.

# 9. Hur skiljer du ett DNS-problem från ett DHCP-problem?
     Kolla om du fått ip-address från DHCP-server, oftast finns inte Deafult-Gateway address.
     ip-config or if-config, ping dns-server.

# 10.Vad betyder det att en dator har en address som börjar på 169.254?
     Det är en apipa address, eller link-local.
     Det händer om DHCP-server är nere eller nätverkproblem (trasig nätverkskabel). Eller DHCP-pool är fullt.

# 11.Räkna ut nätaddress, broadcast, och addressintervall för 192.168.1.200/26. Visa alla fyra stegen.
     1. Blocksteget är 64. 0-64-128-192.
     2. Host address är 200 ligger mellan 192-254.
     3. Nät börjar på 192 så Broadcast är 255. Första är 192 och det är nätaddress, Sista är 255 och det är broadcast address.
     4. Enheterna mellan 193-254 - 62 stycken
     
# 12.Räkna ut samma sak för 10.0.0.6/30. Hur många enheter får plats?
     
