Skapa en liten infrastruktur. En router, en switch och tre klient dator.

<img width="352" height="247" alt="Screenshot From 2026-09-01 08-42-48" src="https://github.com/user-attachments/assets/f554b4c4-7262-488e-aab7-18a70c0dcf10" />


Jag koplade en laptop dator till router med konsolkabel och börja konfigurera routern i terminal.

<img width="481" height="147" alt="Screenshot From 2026-09-01 08-47-54" src="https://github.com/user-attachments/assets/e231b6f7-a349-4a4b-9344-778aa30fec9c" />


Router> enable                                    -> Denna kod ska hämta dig från user mode till Priviledged mode.

Router# configure terminal     - or - conf t      -> Med denna kod du kan ändra settings i routern.

Router(config)# Hostname RT-01-Attila             -> Denna kod byta Hostname till routern. Viktig om du önskar en strukturerat dokumentation.

RT-01-Attila(config)# exit                        -> Denna kod ska ta dig tillbaka till priviledged mode

RT-01-Attila# write memory                        -> Denna kod sparas running-configuration till startup-configuration

<img width="426" height="195" alt="Screenshot From 2026-09-01 09-16-08" src="https://github.com/user-attachments/assets/9e700c63-91d7-4847-ab46-b7cb6dae62d9" />


RT-01-Attila# int g0/0                            -> Med denna kod du välja port eller interface GigabitEthernet 0/0 att konfigurera.

RT-01-Attila(config-if)# ip address 192.168.10.1 255.255.255.0 -> Här du konfigurera ip address på porten du vält förre.

RT-01-Attila(config-if)# no shutdown              -> Här du bestämmer att port ska aldrig gå ner. "konstant på".

<img width="597" height="195" alt="Screenshot From 2026-09-01 09-24-46" src="https://github.com/user-attachments/assets/d96abcc6-c9f1-4419-9ad1-857f6d4ea957" />

RT-01-Attila(config-if)#                          -> Nu vi är fortfarande i interface konfiguration mod och vi ska konfigurera DHCP server funktion.

RT-01-Attila(config-if)#ip dhcp pool lan          -> Denna kod skapa en dhcp pool heter "LAN".

RT-01-Attila(dhcp-config)#ip dhcp excluded-address 192.168.10.1 192.168.10.9 -> Här vi bestämmer "statik addresser". Sparats till servrar, skrivare, etc.


RT-01-Attila(dhcp-config)#network 192.168.10.0 255.255.255.0 -> Här vi skapa nätverk 192.168.10.0: Anger intervallet för IP-adresser som routern får tilldela DHCP-klienter (adresserna 192.168.10.1 till 192.168.10.254). 255.255.255.0: Tillämpar en /24-subnätmask som definierar värdintervallet för denna pool.

RT-01-Attila(dhcp-config)#default-router 192.168.10.1 -> Här vi bestämmer router ip-address (default-gateway).

RT-01-Attila(dhcp-config)#dns-server 8.8.8.8      -> Här vi skapa ansvarig domain-name-server vilken är googles domain-name server.

<img width="531" height="443" alt="Screenshot From 2026-09-01 10-16-09" src="https://github.com/user-attachments/assets/e0516e34-eba5-49a0-85c9-dc4cf2ec0605" />

Nu,vi kan testa om dhcp server funkar. Bara logga-in på datorerna och välja dhcp klient.

<img width="680" height="305" alt="Screenshot From 2026-09-01 10-19-19" src="https://github.com/user-attachments/assets/940cd013-b4df-455d-90a3-5b3bf8909a64" />

Jag har vält PC0 och kollat på DHCP och det funkar.

Nu, jag ska välja på andra två datoren också och pinga alla.

<img width="398" height="354" alt="Screenshot From 2026-09-01 10-23-40" src="https://github.com/user-attachments/assets/ec30947c-d734-4de4-992e-dff404ca3910" />

Jag byta konsol kabel och koppla till switchen. 

<img width="452" height="138" alt="Screenshot From 2026-09-01 10-28-19" src="https://github.com/user-attachments/assets/fd505ada-a97a-4288-9988-ad9539963ea0" />

Efter bytat hostname av switchen, bara exit och "write memory".

SW-01-Attila# show mac address-table           -> Denna kood visar alla enheter kopplat till switchen, med mac-address, hur switchen fått mac-address och vilken port enheten ligger också.

<img width="309" height="177" alt="Screenshot From 2026-09-01 10-51-56" src="https://github.com/user-attachments/assets/17936dc5-31f6-4769-8699-9d619a1efc19" />

SW-01-Attila#show interfaces status            -> Denna kommando visar alla portar, om de är kopplat eller inte, duplex-mode, och vilken hastighet porten har.

<img width="574" height="392" alt="Screenshot From 2026-09-01 10-58-10" src="https://github.com/user-attachments/assets/af77da4c-4411-4632-9dc4-3f8d2f2aa9e1" />


