Plan är här, att skapa en infrastruktur med /26 subnet och 4 VLAN trunk melllan en router och två olika switch.


<img width="1585" height="871" alt="Screenshot From 2026-09-09 14-28-59" src="https://github.com/user-attachments/assets/8d1c9914-6975-45e3-ba8f-6fc77ce310a9" />


Gör en plan med alla vlan namn och varje nätverk ska ha rederverad 10 statisk addresser


<img width="753" height="628" alt="Screenshot From 2026-09-09 14-30-53" src="https://github.com/user-attachments/assets/2b36b443-3159-4e7d-9b17-59f691a115ee" />


Koppla till router med en konsol-kabel och byta hostnam på routern och Port G0/0/0 är administratively up.


<img width="753" height="265" alt="Screenshot From 2026-09-09 14-34-28" src="https://github.com/user-attachments/assets/537df2d2-b418-45f8-9480-81b9fb7ad835" />


Börja konfigurera vlan 10-20-30-99 på samma port med encapsulation "TRUNK".


<img width="942" height="637" alt="Screenshot From 2026-09-09 15-04-08" src="https://github.com/user-attachments/assets/c62accdc-89aa-4184-8cfb-f8a032401a31" />


Nu vi ska fixa alla statik addresser på alla nätverk.


<img width="750" height="108" alt="Screenshot From 2026-09-09 15-08-28" src="https://github.com/user-attachments/assets/34ff4610-2fc2-4504-bc36-59d567ecdb9c" />


Och sist på router, vi ska bestämmer alla avdelning Namn, pool och default-router (gateway) address.










<img width="750" height="421" alt="Screenshot From 2026-09-09 15-16-36" src="https://github.com/user-attachments/assets/7841e24d-4cc8-4b83-b4fc-4ea8f9c8d291" />



Nu vi ska avkoppla från routern och vi ska koppla till Switch 0 (enligt mappen).

Börja konfigurera Switch 0 med byta hostnam och trunk portarna från routern och till andra switchen.


<img width="633" height="130" alt="Screenshot From 2026-09-10 05-12-54" src="https://github.com/user-attachments/assets/082c6353-1711-4138-8358-77d0614b0d28" />


Efter hostnam bytat, vi konfigurera alla vlan och vlan namn.


<img width="633" height="247" alt="Screenshot From 2026-09-10 05-15-39" src="https://github.com/user-attachments/assets/dd179e53-6fdd-4052-ad0c-61ba7a2a5af6" />


Definiera trunk portarna (wilken inkommer från router och gå ut till andra switchen)

Först, Gigabit port vilken inkommer från Routern.


<img width="906" height="205" alt="Screenshot From 2026-09-10 05-18-38" src="https://github.com/user-attachments/assets/22726378-ba82-43b0-ba91-a949ccb06cab" />


Efter, andra Gigabit port, vilken gå till andra switchen.


<img width="906" height="283" alt="Screenshot From 2026-09-10 05-20-30" src="https://github.com/user-attachments/assets/6894bb5a-a16c-496b-841a-401ceefa854c" />


Nu alla TRUNK port är set. 
Men vi har en avdelning kopplat till switch ett, vilken är VLAN 99 - DRIFT. 
Vi gör två access till DRIFT datoren till VLAN 99

<img width="648" height="445" alt="Screenshot From 2026-09-10 05-27-26" src="https://github.com/user-attachments/assets/7686bf7d-d014-4e39-a8d9-46b2bc5f88d3" />


Nu, switch 01 är helt klart. Vi kan gå till sista enhet, Switch 02.

På switch 02 byta hostnamn och konfigurera VLAN och inkommer TRUNK port från switch 01.


<img width="672" height="513" alt="Screenshot From 2026-09-10 05-37-02" src="https://github.com/user-attachments/assets/a5dc0096-13e2-4f5e-a5ef-d77f34501437" />


Efter vi bestämt vlan's och trunk port, vi kan fixa alla trunk access portarna och alla avdelning.

Jag börjar med VLAN 10 - Kontor


<img width="522" height="142" alt="Screenshot From 2026-09-10 05-44-53" src="https://github.com/user-attachments/assets/0956c263-4895-4698-b31f-d2e68067334b" />


Nästa är VLAN 20 - EKONOMI och sista är VLAN 30 - GAST


<img width="522" height="423" alt="Screenshot From 2026-09-10 05-53-58" src="https://github.com/user-attachments/assets/bc243003-b9cb-411c-bdf4-27afb8d2c964" />


Jag har kontrolerat att alla datorer få ip address från respektiv dhcp server automatisk.


Kolla på Switch-01 om vlan's och TRUNK portarna är ok.


<img width="795" height="711" alt="Screenshot From 2026-09-10 06-04-29" src="https://github.com/user-attachments/assets/7b111a0b-f435-42ae-adc0-1e24b325d711" />


kolla på Switch-02 on vlan's och TRUNK portarna är ok.


<img width="795" height="634" alt="Screenshot From 2026-09-10 06-07-41" src="https://github.com/user-attachments/assets/c3070695-72ca-4835-8760-73f6f99d3a09" />


