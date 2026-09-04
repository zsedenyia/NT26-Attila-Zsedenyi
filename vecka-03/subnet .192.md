Denna vecka vi lära subnetting och jag försöker att skapa en infrastruktur i Cisco packet tracer.

Började med en router och fyra switchar. Alla switchar simulera en "avdelning" i en företag. Att konfigurera router, använda jag en laptop kopplat med konsol kabel. 
Det bli 4 subnet så /26 CIDR, subnet mask är 255.255.255.192. Blocksteget är 64. 0-64-128-192.

<img width="1185" height="354" alt="Screenshot From 2026-09-03 19-22-18" src="https://github.com/user-attachments/assets/de327bfc-e565-4056-881f-767d6dcd7c70" />


Jag använda en Cisco IR8340 Router och fyra Cisco 2960 switch. Min nätverk plan är ligger nere:


<img width="834" height="226" alt="Screenshot From 2026-09-03 19-23-47" src="https://github.com/user-attachments/assets/4dc6d4a6-df51-4eac-b917-6205eb3aa79a" />


Jag ska har DHCP server på varje subnet, men första 18 addresser är reserverat till static enheter. T.ex: skrivare, server, Nas... etc.


<img width="408" height="159" alt="Screenshot From 2026-09-03 21-08-23" src="https://github.com/user-attachments/assets/5e4dc5ce-cb11-4d9a-8cd8-a14207d8094e" />


Började konfigurera routern, först bytat hostnamn och efter varje port fått sin egen ip address och bo shut down, på slutet, write memory så alla saker sparat i NVRAM.


<img width="777" height="531" alt="Screenshot From 2026-09-03 19-29-15" src="https://github.com/user-attachments/assets/54c4c67a-6cad-4d6f-a7b6-6df32ae23627" />


Efter jag har bestämt alla portar ip address och no shutdown, jag gick till nästa steg och fixat dhcp-server till varje subnet med 19 port reserverat till statik ip-addresser.

Första subnet med dhcp pool var sales.


<img width="789" height="229" alt="Screenshot From 2026-09-03 20-51-42" src="https://github.com/user-attachments/assets/d47aaa9c-2fef-4076-bcd2-6c3a57d8aeac" />


Andra subnet med dhcp pool är ekonomi.


<img width="799" height="171" alt="Screenshot From 2026-09-03 20-55-14" src="https://github.com/user-attachments/assets/f24097ce-f997-472f-89a8-99b6eb105462" />


Tredje subnet med dhcp pool är lager.


<img width="814" height="358" alt="Screenshot From 2026-09-03 20-56-59" src="https://github.com/user-attachments/assets/3708968b-9893-4535-9e90-fd4d8756dd88" />


Ocg sista subnet med dhcp pool är guest.


<img width="814" height="358" alt="Screenshot From 2026-09-03 20-58-07" src="https://github.com/user-attachments/assets/97fa1033-0beb-475c-a0fa-d655e3cc7597" />


Efter alla konfiguration är färdig, nu det dags att koppla datorer till alla switcharna och fråga dhcp server för ip-addresser.


<img width="1371" height="586" alt="Screenshot From 2026-09-03 21-01-08" src="https://github.com/user-attachments/assets/ffeb213f-f195-4308-918b-0bcff613deb6" />


PC 0


<img width="574" height="577" alt="Screenshot From 2026-09-03 21-02-20" src="https://github.com/user-attachments/assets/b4ba6b74-558b-483c-bda6-bf96f559e698" />


PC 2


<img width="574" height="577" alt="Screenshot From 2026-09-03 21-03-13" src="https://github.com/user-attachments/assets/a8573d49-5012-451b-a8a3-612df0be28cb" />


PC 4


<img width="574" height="489" alt="Screenshot From 2026-09-03 21-04-09" src="https://github.com/user-attachments/assets/7d82f6f7-0e33-484d-97e6-021b36d7762f" />


PC 6


<img width="574" height="489" alt="Screenshot From 2026-09-03 21-05-05" src="https://github.com/user-attachments/assets/c3ca73af-877a-4131-acfd-81ad43688970" />


Bonus: 

Jag har kopplat en access-punkt till guest nätverk och konfigurerat SSID och Lösenord. Efter, jag kopplat med en laptop till access-punkten och fått Ip-address direkt från DHCP-server.


<img width="1531" height="639" alt="Screenshot From 2026-09-03 21-59-37" src="https://github.com/user-attachments/assets/1e7cf2d5-e55b-453d-9089-e765a00b9bd8" />


Setting av Access-punkt.


<img width="1045" height="639" alt="Screenshot From 2026-09-03 22-01-31" src="https://github.com/user-attachments/assets/fc2b2bcf-77ef-4f28-a871-12dea4cc8468" />


Och Auto-IP address via DHCP


<img width="1045" height="565" alt="Screenshot From 2026-09-03 22-03-16" src="https://github.com/user-attachments/assets/92573c4a-8ce1-4b82-b07f-f28c05ac05f6" />


Finished.

