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

