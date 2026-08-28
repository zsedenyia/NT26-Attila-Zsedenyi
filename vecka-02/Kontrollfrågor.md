# 1 Vad står först i en ram, ansändares eller mottagarens Address?
    Mottagarens address.
    
# 2 Hur många tecken har en MAC-address, och vad betyder den första halvan?
    12 tecken och första halva är för identifera tilverkare egen kod. t.ex: Intel, realtek.

# 3 Var får switchen sina anteckningar ifrån? Vem fyller tabellen?
    Switchen lära själv. När en dator skicka packet till en annan i ram finns motaggare mac address och avsändare mac-address.
    Switchen spara avsändare mac-address och fyller i mac-address tabell. 
   
# 4 Vad gör switchen med en ram vars mottagare den inte känner igen?
    Om motaggare mac address finns inte i tabellem, switchen floda data ram till alla portar förutom var ligger avsändare och vänta för svar.
    När mottagare få ramen, svarar "Hej, denna packet är till mig" switchen lära mottagarens mac address, samtidigt alla andra enhet slänng ramen.

# 5 Hur länge sitter en anteckning kvar i MAC-tabellen, och varför försvinner den?
    Det sitter 5 minuter om det finns inte dataflöde till enheten. Efter försvinner. 

# 6 Vilken address används vid Broadcast, och vad betyder den.
    Address är FF-FF-FF-FF-FF-FF. Och det betyder att skicka till alla enheter, vilken är kopplad till switchen.

# 7 Varför går en ARP-fråga till alla, medan svaret går till alla.
    När en Arp-fråga är skickats ut, det är en Broadcast begräran. Skickar ut att lära Mac address från en enhetn på netvärk.
    När matchar enhet med mac-addressen, enhet skickar tillbaka en unicast svar. "Hej, här är jag". Alla andra enheter slänga ramen.

# 8 Din dator vill nå en server i ett annat land. Vilken MAC-address frågar den efter?
    Min dator ska fråga efter min egen default-gateway (Router) MAC-address.

# 9 Vad betyder DYNAMIC respektive STATIC i kolumnen Type?
    DYNAMIC betyder att switchen har lärt mac-address och STATIC betyder att en person har skrivit fix "static-address".

#10 Nämn två saker som gör att en port visar NOT CONNECT.
    Ingen fysik kabel kopplat till porten eller kabel är trasig. 
    Eller porten är avstängd eller enheten NIC är avstängd också.

#11 Några veckor senare ringer Anna igen. Här är ett utdrag ur MAC-tabellen. Hon har adressen a4c3.f011.3ab7 och når ingen alls, trots att
    hennes port är uppe. Vad är fel, och vilken kolumn avslöjar det?
    Kolumnen är Vlan och hennes dator sitter i Vlan 99. Det är problemet.

#12 Här är ett utdrag ur show interfaces status. Tre portar har trafik. En av dem kommer att fungera sämre än de andra. Vilken, och vad skulle du kontrollera härnäst?
    Problemet är duplex mode. Enhet kopplat till Gi0/2 är på half-duplex.

#13 Skriv fem meningar till en kollega som aldrig hört talas om en switch, där du förklarar varför switchen skickar en ram till alla portar första gången. Använd inga engelska termer utom switch.
    Föreställ dig en switch som en smart brevbärare i ett hus där alla rum har varsin dörr. 
    När brevbäraren får ett brev till någon som bor i huset, måste den veta exakt vilket rum personen befinner sig i. 
    Första gången ett brev ska levereras har brevbäraren ännu inte lärt sig vem som bor var. 
    Därför knackar den på alla dörrar samtidigt och ropar ut namnet för att se vem som svarar.
    När rätt person väl ger sig till känna kommer brevbäraren ihåg vilket rum det var och skickar alla framtida brev direkt dit.
