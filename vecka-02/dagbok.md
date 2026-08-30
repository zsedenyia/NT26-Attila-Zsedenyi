Jag har började bygga en infrestruktur i cisco packettracer.
Skapat en router och koplat till med en dator via konsolkabel.

<img width="432" height="117" alt="Screenshot From 2026-08-30 09-09-35" src="https://github.com/user-attachments/assets/27d4cd83-29f8-4f0f-8dc5-712db294af88" />


Efter jag fixat router namn och aktiverad gigabit ethernet 0/0 och vält no shutdown.
slutligen, sparat i startup minne så alla ändringar är sparas.

<img width="475" height="435" alt="Screenshot From 2026-08-30 09-15-33" src="https://github.com/user-attachments/assets/f242560d-35a9-4d8b-9da4-b07968735ac0" />

Som nästa steg jag har skapat två switch och koplat till router. 
Gigabit ethernet från både switch till gigabit ethernet i router.

<img width="906" height="225" alt="Screenshot From 2026-08-30 09-40-56" src="https://github.com/user-attachments/assets/181cc574-fae2-48b8-bddb-aa5a8554d89a" />

Jag konfigurerat ip address till båda gigabit ethernet och aktiverat DHCP server funktion.

<img width="648" height="558" alt="Screenshot From 2026-08-30 09-51-54" src="https://github.com/user-attachments/assets/8c88e65d-ad65-40c1-915b-58417ff77322" />

Nu Gigabit Ethernet 0/0 konfigurerat med ip-address och dhcp pool. Också. "no shutdown" menar att porten ska stanna aktiverat. "do write memoory" menar at ändringar i router sparat i startup-memory (NVRAM).

här är hur jag konfigurerat Gigabit ethernet 0/1.

<img width="648" height="467" alt="Screenshot From 2026-08-30 09-57-41" src="https://github.com/user-attachments/assets/6f7438b8-fd81-4b20-8c77-4638b7ce1245" />

Som nästa steg, jag koplade min dator till swiitchone och ändrat namn.

<img width="449" height="271" alt="Screenshot From 2026-08-30 10-02-16" src="https://github.com/user-attachments/assets/640a5538-c5ea-4b4c-9654-e79340ffe518" />
