Plan är här, att skapa en infrastruktur med /26 subnet och 4 VLAN trunk melllan en router och två olika switch.

<img width="695" height="561" alt="Screenshot From 2026-09-08 13-48-39" src="https://github.com/user-attachments/assets/2cff767a-3ce8-4c2a-a643-f2a8e0f9c4a1" />


Började med Routern. Fixat hosname och port till första switchen aldrig stängs av.


<img width="518" height="204" alt="Screenshot From 2026-09-08 13-47-24" src="https://github.com/user-attachments/assets/dad43de9-0ae7-4529-89aa-a696df84b5d0" />


Efter det är klart, vi stanna i routern och skapa alla nätverk-addresser, dhcp och vlan.

En till, på alla nätverk det bli 10 addresser reserverat till statik enheter.


<img width="681" height="199" alt="Screenshot From 2026-09-08 14-24-07" src="https://github.com/user-attachments/assets/434c267d-9e2b-4710-926e-652def3613c7" />


Alla VLAN med nätverk-addresser är färdig på router på port Gi 0/0/0


<img width="623" height="466" alt="Screenshot From 2026-09-08 14-28-23" src="https://github.com/user-attachments/assets/acb885ec-f4fc-41c7-816d-2602fde312a2" />


Nästa steg är fixa alla statik ip addresser. T.ex: till server, skrivare...osv.


<img width="521" height="72" alt="Screenshot From 2026-09-08 14-31-59" src="https://github.com/user-attachments/assets/6b240696-c6de-4786-a406-a1bdd5e58a9a" />


När det klart, vi bestämmer alla nätverk och default-gateway.


<img width="521" height="388" alt="Screenshot From 2026-09-08 14-41-49" src="https://github.com/user-attachments/assets/317de2fb-0581-4ee9-8ec5-f4f8fcefd90d" />


Nu, jag byta konsol kabel till switch 0 och börja konfigurera alla VLAN och TRUNK och ACCESS port.

Kom ihåg, TRUNK portar är var alla VLAN kom och gå samtidigt. ACCESS port var datorer är kopplat och tagged rammar gå.


<img width="630" height="588" alt="Screenshot From 2026-09-08 14-59-45" src="https://github.com/user-attachments/assets/bc55705f-6885-43cf-9d7b-5199fd2aab2b" />


På switch 0, hostname är bytat och båda gigabit port G0/1 och G0/2 är trunk portar. 
Men! Vi har två datorer kopplat till switch 0 och de behöver en access-port till varje dator. 


<img width="630" height="490" alt="Screenshot From 2026-09-08 15-14-21" src="https://github.com/user-attachments/assets/705abb06-b0d5-4d11-8749-547375905299" />


Switch 01 är helt klart nu, byta konsol kabel till switch 02 och börja med konfiguration. Byta hostname, bestämmer vlan's och Gigabit Ethernet port måste konfigurera till TRUNK port.


<img width="447" height="522" alt="Screenshot From 2026-09-08 15-26-53" src="https://github.com/user-attachments/assets/ba05624a-d36e-44f6-ba2e-ee8fd5d017e6" />


Nu bara kvar att bestämmer alla access portar till varje dator. Kom ihåg, om du bestämmer en port till en vlan, t.ex: Kontor, datoren ska få en ip address automatisk från kontors vlan dhcp server.


