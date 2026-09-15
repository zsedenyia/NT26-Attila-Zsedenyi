# Terminalkommandon – Nätverksteknik

*Fullständig sammanställning av alla terminalkommandon i boken, kapitel för kapitel. Cisco IOS (switch/router) accepterar en förkortning så länge den är entydig — boken visar själv `conf t`, `sh run` och `int gi0/1` som exempel; övriga förkortningar nedan följer samma standard.*

---

## Kapitel 1 — Sladden, prompten och lådorna

*Grundläggande navigering i Cisco IOS: lägen, spara konfiguration, felsökning.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `enable` | `en` | Går från användarläge (`>`) till privilegierat läge (`#`). |
| `configure terminal` | `conf t` | Går till konfigurationsläget (`(config)#`), där ändringar görs. |
| `end` | `en` (i konfig-läge) | Går tillbaka hela vägen till privilegierat läge (`#`). |
| `exit` | `ex` | Går ett steg tillbaka, eller loggar ut från toppläget. |
| `hostname <namn>` | `host <namn>` | Namnger enheten. Prompten byter namn direkt. |
| `interface GigabitEthernet0/1` | `int gi0/1` | Går in i en enskild ports konfigurationsläge (`(config-if)#`). |
| `no shutdown` | `no shut` | Slår på en avstängd port. |
| `show version` | `sh ver` | Visar modell, IOS-version, uptime, serienummer, konfigurationsregister. |
| `copy running-config startup-config` | `copy run start` (eller `wr`) | Sparar aktiv konfiguration så den överlever en omstart. |
| `show running-config` | `sh run` | Visar den konfiguration som gäller just nu. |
| `show running-config \| include hostname` | `sh run \| i hostname` | Filtrerar fram bara raden med hostname. |
| `show startup-config` | `sh start` | Visar konfigurationen som laddas vid nästa omstart. |
| `show startup-config \| include hostname` | `sh start \| i hostname` | Kontrollerar att namnet verkligen sparats. |
| `show interfaces status` | `sh int status` | Översikt över alla portars status, VLAN, duplex, hastighet. |
| `show running-config interface <port>` | `sh run int <port>` | Konfigurationen för en enskild port, t.ex. för att se `shutdown`. |

---

## Kapitel 2 — Ramar och MAC-adresser

*Switchens MAC-tabell, felräknare på portar.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `show mac address-table` | `sh mac address-table` | Visar switchens MAC-tabell: adress, VLAN och port. |
| `show mac address-table address <mac>` | `sh mac address-table address <mac>` | Slår upp en specifik MAC-adress direkt. |
| `show interfaces` | `sh int` | Detaljerad statistik per port, bl.a. CRC, runts, late collisions. |
| `clear counters` | `clear coun` | Nollställer felräknarna på en port. |

**Windows / Linux**

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `arp -a` | `arp -a` (redan kort) | (Windows) Visar datorns ARP-tabell. |
| `ipconfig /all` | ingen kortform | (Windows) Detaljerad info: MAC-adress, IP, nätmask, gateway. |
| `ping 192.168.1.1` | `ping <adress>` (redan kort) | Skickar testpaket, tvingar fram trafik switchen kan lära sig av. |

---

## Kapitel 3 — IP-adresser och subnätning

*Sätta adresser på router-interface, DHCP och DNS.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `interface GigabitEthernet0/0` | `int gi0/0` | Går in i interfacets konfigurationsläge. |
| `ip address 192.168.1.1 255.255.255.192` | `ip add <adress> <mask>` | Sätter IP-adress och nätmask på interfacet. |
| `no shutdown` | `no shut` | Slår på interfacet. |
| `show ip interface brief` | `sh ip int br` | Snabb översikt: IP-adress samt lager 1/2-status per interface. |
| `ip dhcp excluded-address 192.168.1.1 192.168.1.19` | `ip dhcp excl <start> <slut>` | Undantar ett intervall från DHCP (för statiska adresser). |
| `ip domain lookup` | `ip dom look` | Slår på routerns egen namnuppslagning. |
| `ip name-server 9.9.9.9` | (redan kort) | Anger vilken DNS-server routern själv frågar. |
| `ip dns server` | (redan kort) | Gör routern till DNS-server åt klienterna. |
| `ip dhcp pool KONTOR` | (redan kort) | Skapar/öppnar en DHCP-pool. |
| `network 192.168.1.0 255.255.255.192` | `net <nät> <mask>` | Anger vilket nät poolen delar ut adresser ur. |
| `default-router 192.168.1.1` | (redan kort) | Gateway-adress klienterna får via DHCP. |
| `dns-server 192.168.1.1` | (redan kort) | DNS-server klienterna får via DHCP. |
| `show ip dhcp binding` | `sh ip dhcp bin` | Visar utdelade adresser och till vilken klient. |

**Windows / Linux**

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `ipconfig` | (redan kort) | (Windows) Aktuell IP-adress, nätmask, gateway. |
| `ip a` | (redan kortform av `ip address show`) | (Linux) Motsvarigheten till `ipconfig`. |

---

## Kapitel 4 — VLAN och trunkar

*Skapa VLAN, access-portar, trunkar, spanning tree.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `vlan 10` | (redan kort) | Skapar VLAN 10 och går in i dess konfigurationsläge. |
| `name KONTOR` | (redan kort) | Ger VLAN:et ett namn (bara för din egen skull). |
| `switchport mode access` | `sw mo access` | Gör porten till en access-port (ett enda VLAN). |
| `switchport access vlan 10` | `sw acc vlan 10` | Lägger porten i VLAN 10. |
| `show vlan brief` | `sh vlan br` | Listar alla VLAN och vilka portar som hör till varje. |
| `interface range GigabitEthernet0/5 - 6` | `int range gi0/5 - 6` | Går in i flera portars konfigurationsläge samtidigt. |
| `description Trunk mot SW-Nordvik-2` | `desc <text>` | Sätter en textbeskrivning på porten (påverkar ingen trafik, bara dokumentation). |
| `switchport trunk encapsulation dot1q` | `sw trunk encap dot1q` | Anger taggningsstandard (behövs på äldre switchmodeller). |
| `switchport mode trunk` | `sw mo trunk` | Gör porten till en trunk (bär flera VLAN). |
| `switchport trunk allowed vlan 10,20,30,99` | `sw trunk allowed vlan <lista>` | Sätter vilka VLAN som får gå över trunken (skriver över, lägger inte till). |
| `switchport trunk allowed vlan add 40` | `sw trunk allowed vlan add 40` | Lägger till ytterligare ett VLAN till en redan satt allowed-lista. |
| `show interfaces trunk` | `sh int trunk` | Visar vilka portar som är trunkar och vilka VLAN de bär. |
| `switchport trunk native vlan 999` | `sw trunk native vlan 999` | Sätter native VLAN (det otaggade VLAN:et) på trunken. |
| `switchport nonegotiate` | `sw nonegotiate` | Stänger av automatisk förhandling av trunk/access-läge (DTP). |
| `spanning-tree portfast` | `sp-tree portfast` | Hoppar över STP:s väntetid på en access-port (aldrig på en trunk). |
| `spanning-tree vlan 10 root primary` | `sp-tree vlan 10 root primary` | Gör den här switchen till root bridge för VLAN 10. |
| `spanning-tree vlan 10 root secondary` | `sp-tree vlan 10 root secondary` | Gör switchen till reserv-root för VLAN 10. |
| `show spanning-tree vlan 10` | `sh sp-tree vlan 10` | Visar vem som är root bridge och varje ports roll/status (FWD/BLK). |

---

## Kapitel 5 — Routing

*Läsa routingtabellen, sub-interface (router-on-a-stick), statiska rutter.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `show ip route` | `sh ip route` | Visar hela routingtabellen: kända nät och vägen dit. |
| `ip route 0.0.0.0 0.0.0.0 203.0.113.1` | `ip route 0.0.0.0 0.0.0.0 <nästa hopp>` | Sätter en defaultrutt ("sista utvägen") för allt okänt. |
| `show ip route static` | `sh ip route static` | Visar bara de statiska rutterna i tabellen. |
| `interface GigabitEthernet0/0.10` | `int gi0/0.10` | Skapar/går in i ett sub-interface för VLAN 10 på en trunk-port. |
| `encapsulation dot1Q 10` | `encap dot1q 10` | Anger vilket VLAN sub-interfacet hör till (måste stå före adressen). |
| `ip address 192.168.1.1 255.255.255.192` | `ip add <adress> <mask>` | Sätter gatewayadressen på sub-interfacet. |
| `ip route 192.168.2.0 255.255.255.0 10.0.0.2` | `ip route <nät> <mask> <nästa hopp>` | Statisk rutt till ett specifikt fjärrnät via ett nästa-hopp. |
| `traceroute 192.168.2.10` | `trace <adress>` | Visar varje router (hopp) på vägen till målet. |
| `show ip route connected` | `sh ip route connected` | Visar bara de anslutna rutterna (nät routern själv sitter i). |
| `show ip route 192.168.1.70` | `sh ip route <adress>` | Visar vilken rad i tabellen routern skulle välja för en specifik adress. |

---

## Kapitel 6 — NAT och säker inloggning

*NAT/PAT, SSH-konfiguration, säkerhetskopiering och sanering.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `ip nat inside` | (redan kort) | Märker interfacet som "insidan" (det egna nätet). |
| `ip nat outside` | (redan kort) | Märker interfacet som "utsidan" (mot internet). |
| `ip nat inside source static 192.168.1.10 203.0.113.11` | `ip nat inside source static <intern> <extern>` | Statisk NAT: en intern adress motsvarar alltid en bestämd extern adress. |
| `show ip nat translations` | `sh ip nat tra` | Visar pågående NAT-översättningar. |
| `show ip nat statistics` | `sh ip nat stat` | Visar vilka interface som är inside/outside och sammanfattande statistik. |
| `access-list 1 permit 192.168.1.0 0.0.0.255` | `acc-list 1 permit <nät> <wildcard>` | Standardlista som pekar ut vilka adresser som får översättas. |
| `ip nat inside source list 1 interface GigabitEthernet0/1 overload` | `ip nat inside source list 1 int gi0/1 overload` | Slår på PAT: många enheter delar en offentlig adress (ordet `overload` gör det till PAT). |
| `clear ip nat translation *` | (redan kort) | Rensar hela NAT-översättningstabellen. |
| `ip domain-name nordvik.example` | (redan kort) | Ger enheten ett domännamn (krävs för SSH-nyckeln). |
| `crypto key generate rsa` | (redan kort) | Skapar nyckelparet SSH behöver (svara 2048 på frågan om nyckelstorlek). |
| `username drift privilege 15 secret <lösenord>` | `user drift priv 15 secret <lösenord>` | Skapar ett lokalt användarkonto med lösenord. |
| `ip ssh version 2` | (redan kort) | Tvingar fram SSH version 2 (kräver 2048-bitars nyckel). |
| `line vty 0 4` | (redan kort) | Går in i konfigurationen för de första fem inloggningslinjerna. |
| `transport input ssh` | (redan kort) | Tillåter bara SSH på linjerna (stänger dörren för telnet). |
| `login local` | (redan kort) | Kräver inloggning mot de lokala användarkontona. |
| `line vty 5 15` | (redan kort) | Samma sak för resterande inloggningslinjer (fler än de första fem). |
| `show ip ssh` | (redan kort) | Visar om SSH är igång och vilken version. |
| `reload in 10` | (redan kort) | Ställer in en automatisk omstart om 10 minuter — säkerhetsnät vid fjärrändringar. |
| `reload cancel` | (redan kort) | Avbryter den schemalagda omstarten (körs när ändringen visat sig fungera). |
| `write memory` | `wr` | Sparar konfigurationen (görs sist, efter att ändringen bevisats fungera). |
| `copy running-config flash:backup.cfg` | `copy run flash:backup.cfg` | Tar en säkerhetskopia av konfigurationen till flashminnet. |
| `configure replace flash:backup.cfg` | (redan kort) | Återställer konfigurationen från en sparad säkerhetskopia. |
| `show line` | (redan kort) | Visar hur många inloggningslinjer enheten har totalt. |
| `show access-lists` | `sh acc-list` | Visar alla åtkomstlistor på enheten. |

**Windows / Linux**

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `grep -ri secret configs/` | (redan kort) | Söker rekursivt (`-r`) och skiftlägesokänsligt (`-i`) efter ordet "secret" i konfigurationsfiler, innan de committas. |

---

## Kapitel 7 — Drift och övervakning

*Loggning, tidsstämplar, NTP, filtrering i Wireshark.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `service timestamps log datetime msec` | (redan kort) | Slår på tidsstämplar med datum och millisekunder på loggrader. |
| `logging buffered 16384` | `logging buff 16384` | Sätter storleken på enhetens interna loggminne (i byte). |
| `ntp server 192.168.1.16` | (redan kort) | Anger vilken NTP-server enheten ska synka klockan mot. |
| `show clock` | (redan kort) | Visar enhetens aktuella tid och om den är NTP-synkroniserad (tecken `*`, `.` eller mellanslag). |
| `show logging` | `sh log` | Visar enhetens egen sparade logg. |
| `show logging \| include LINK-3-UPDOWN` | `sh log \| i LINK-3-UPDOWN` | Filtrerar loggen till bara rader om portar som gått upp/ner. |
| `logging host <adress>` | (redan kort) | Skickar loggmeddelanden vidare till en central loggserver. |

**Wireshark-filter** (inte terminalkommandon, men textfilter i verktyget)

| Filter | Förklaring |
|---|---|
| `ip.addr == 192.168.1.42` | Visar all trafik till eller från en adress. |
| `tcp.port == 80` | Visar all trafik på en viss port. |
| `arp` | Visar bara ARP-trafik. |
| `stp` | Visar bara spanning tree-trafik. |

---

## Kapitel 8 — Trådlöst

*PoE på switchportar och kontroll av strömbudget.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `power inline auto` | (redan kort) | Slår på automatisk PoE-strömförsörjning på en port. |
| `show power inline` | `sh power inline` | Visar PoE-budget: tillgängligt, använt och kvarvarande, per port. |
| `show power inline GigabitEthernet0/1` | `sh power inline gi0/1` | Samma som ovan, men för en enskild port. |

---

## Kapitel 9 — Säkerhet och brandvägg

*Extended ACL, verifiering och port security.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `ip access-list extended KONTOR-UT` | `ip acc-list ext KONTOR-UT` | Skapar/öppnar en namngiven extended ACL. |
| `deny ip 192.168.1.0 0.0.0.63 192.168.1.64 0.0.0.63` | `deny ip <källa> <wildcard> <mål> <wildcard>` | Nekar trafik mellan två angivna nät (wildcard-mask, nätmask baklänges). |
| `permit ip any any` | (redan kort) | Släpper igenom allt annat — måste stå sist, annars stoppar implicit deny allt. |
| `ip access-group KONTOR-UT in` | `ip acc-group KONTOR-UT in` | Sätter listan på ett interface, i riktningen "in" (från routerns synvinkel). |
| `show ip interface GigabitEthernet0/0.10` | `sh ip int gi0/0.10` | Visar bl.a. vilken ACL som sitter på interfacet och i vilken riktning. |
| `remark Revisorskrav: ej kontor mot ekonomi` | (redan kort) | Lägger en kommentarsrad i ACL:en som förklarar varför regeln finns. |
| `no ip access-list extended KONTOR-UT` | `no ip acc-list ext KONTOR-UT` | Tar bort en hel namngiven ACL (för att skriva om den från grunden). |
| `show access-lists KONTOR-UT` | `sh acc-list KONTOR-UT` | Visar en specifik lista med träffräknare per rad. |
| `clear access-list counters` | `clear acc-list counters` | Nollställer träffräknarna innan ett test. |
| `switchport port-security` | `sw port-security` | Slår på port security på en access-port. |
| `switchport port-security maximum 1` | `sw port-security maximum 1` | Sätter max antal tillåtna MAC-adresser på porten. |
| `switchport port-security mac-address sticky` | `sw port-security mac-address sticky` | Låter switchen själv lära sig och spara den tillåtna adressen. |
| `switchport port-security violation restrict` | `sw port-security violation restrict` | Vid överträdelse: blockera och logga, men håll porten uppe (alternativ: `shutdown`, `protect`). |
| `show port-security interface <port>` | `sh port-security int <port>` | Visar antal tillåtna/sedda adresser på en port. |
| `shutdown` / `no shutdown` | `shut` / `no shut` | Stänger av och slår på en port igen (t.ex. för att återställa en err-disabled port). |

---

## Kapitel 10 — VPN, SD-WAN och lastbalansering

*Site-to-site VPN-tunnel (IPsec): vilken trafik som ska krypteras och verifiering.*

| Kommando | Förkortning | Förklaring |
|---|---|---|
| `ip access-list extended VPN-TRAFIK` | `ip acc-list ext VPN-TRAFIK` | Skapar en ACL som pekar ut vilken trafik som ska in i VPN-tunneln (här betyder `permit` "kryptera", inte "släpp igenom"). |
| `permit ip 192.168.1.0 0.0.0.63 192.168.2.0 0.0.0.63` | `permit ip <källa> <wildcard> <mål> <wildcard>` | Anger vilka två nät som ska skyddas av tunneln (måste spegla motsvarande rad på andra routern). |
| `show crypto isakmp sa` | `sh crypto isakmp sa` | Visar om tunneln är uppe (`QM_IDLE` = uppe och vilar). |
| `show crypto ipsec sa \| include encaps\|decaps` | `sh crypto ipsec sa \| i encaps\|decaps` | Visar antal krypterade/dekrypterade paket — beviset på att trafik faktiskt går igenom tunneln. |
| `ip tcp adjust-mss 1360` | (redan kort) | Justerar maximal segmentstorlek så att paket inte blir för stora när tunnelns extra lager läggs på. |

---

*Förkortningarna för switch/router är standard i Cisco IOS-CLI; endast `conf t`, `sh run` och `int gi0/1` nämns uttryckligen i boken, resten följer samma regel om entydighet. Windows/Linux-kommandonas kortformer är respektive verktygs egna flaggor.*

