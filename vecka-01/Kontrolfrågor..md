# 1 Varför går det att komma in på en switch över konsolen även när netverket är nere?
    KOnsol port är "bakdörr" till enhet. Om nätverket är nere och kan inte koppla till IOS via ethernet port, konsol port fortfarande funkar och denna är en direkt port att konfigurera enhent.

# 2 Vilka tre lägen finns och hur se du i prompten vilket du är i?
    switch> Det är "user mode" du kan få information men kan inte ändra ingenting. 
    switch# Det är "priviledged mode". Du kan göra ändringar. Komando användat: enable
    swict#(config) det är "configuration mode". När du gör andring med enheten. Komando: "Configure Terminal".

# 3 Vilket komando tar dig från användare läget till privilegiat läge?
    Enable

# 4 Vad är skilnaden mellan running-config ochstartup-config?
    Running-config är till example när enhet är på och vi göra ändring. Det sparas i running config.
    Startup-Config är när vi starta upp enhet och det bootar från NVRAM. NVRAM är var vi kan spara running-config som startup-config.
   
# 5 Vad händer med en osparad ändring vid en strömavbrott.
    Om vi inte spara running-config till startup-config och enheten stängs av eller strömavbrot händer, running- config ska borta med alla ändringar.

# 6 Räkna upp denna sju OSI-lager.

    7. Application    A  Away
    6. Presentation   P  Pizza
    5. Session        S  Sausage
    4. Transport      T  Throw
    3. Network        N  Not
    2. Data-Link      D  Do
    1. Physical       P  Please
    Easy to remember...

# 7 Vilket lager arbetar en switch på? Vilken lager en router?
    Switch arbetar på lager 2 (Data lager) och kom ihåg på fysikal MAC-address. 
    Router arbetar på lager 3 (network lager) och kom ihäg logical Ip-address.

# 8 Vad gör en brandvägg som en router ingen gör?
    Brandvägg filtrera traffik enligt hur det var konfigurerat. Router är routa data mellan 2 olika lan.

# 9 Nämn två saker "show version" berättar om en okänd enhet.
    Det visas enhet IOS version och running config också.

# 10 Vilken hastighet ska den serial port ha, och vad se du om den är fel?
    Hastighet är 9600.

# 11 svar är: port Gi 0/3 - Disabled. Porten är stängd av. 
    configure Terminal -> interface Gigabitethernet0/3  -> no shut down -> end -> write'

# 12 En KKurskamrat visa dig det här och säger att switchen "inte ta emot kommandon".Vad här hant och vad säger du åt att göra?
    Först måste byta till "priviledged mode". Switchen är i "user mode" enligt bilden.

# 13 Fem meningar att förklara skillanden mellan running-config och startup-config.
    1. Running-config sparas i ram minne. Startup-config sparas i nvram, det är en special minne var switchen bootar när det omstarta 
    2. Switcharna funkar på layer-2, vilken menar de spara enhetrnas Mac addresser, inte IP-addresser, vilken är layer-3 och routrar gör det.
    3. Switchar komihåg av enheternas mac-addresser.och när a dataram kommer från en dator till en adra på samma netvärk switch lära först sendare mac-address. 
       
    
    
