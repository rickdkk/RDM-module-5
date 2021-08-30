# Dataminimalisatie 

Er wordt steeds meer data verzameld en er zijn steeds meer technieken beschikbaar om waarde uit data te halen. Maar er 
zijn ook steeds meer datalekken en de privacy van mensen is over de hele linie in het geding. Als onderzoeker is het je 
plicht om verantwoord om te gaan met de data van je participanten. De data die het makkelijkst is om te beschermen is 
de data die je niet hebt, daarom gaat dit eerste stuk over *dataminimalisatie*. Dit kan men bereiken door gevoelige
informatie helemaal niet te verwerken of door de informatie direct uit de data te halen (anonimiseren). Het 
pseudonimiseren van data kan een middenweg zijn als de data gevoelig doch noodzakelijk is voor het onderzoek. In het 
volgende stuk gaan we in op dataminimalisatie, pseudonimiseren, en anonimiseren bij kleinschalig onderzoek.

:::{figure-md} rewards-fig
<img src="../figures/xkcd_customer_rewards.png" alt="xkcd" width=250px>

xkcd.com over persoonsgegevens
:::

## Minimalisatie

::::::{margin}
:::{note}
Dit hoofdstuk bevat geen uitgebreide uitleg over de AVG. Module 2/3 van het ISP office gaat hier verder op in. De nadruk 
ligt hier op praktische tips voor het werken met data. 
:::
::::::

Als onderzoeker wil je altijd zo veel mogelijk informatie vergaren. Helaas is dat niet altijd mogelijk. Bij het 
onderzoek mag je niet meer (persoons)gegevens verwerken dan strikt noodzakelijk is. Als de persoonsgegevens niet meer 
nodig zijn dan moeten ze ook worden verwijderd. Daarbij moet je van tevoren aangeven waarom je de data verzameld en kan
je deze niet voor iets anders inzetten. Het beste is echter om helemaal geen persoonsgegevens te verzamelen dat scheelt
veel extra moeite tijdens en na het onderzoek.

Als je bijvoorbeeld geen contact meer hoeft op te nemen met de proefpersoon, heb je dus helemaal geen contactinformatie
nodig en kan je die ofwel verwijderen of helemaal niet verzamelen. Zo kan het bijvoorbeeld ook zijn dat je iemand zijn 
leeftijd nodig hebt voor je statistische model. Kijk dan of alleen een leeftijd(range) voldoende is en registreer *niet* 
de geboortedatum. Het kan bijvoorbeeld ook zijn dat je een locatie nodig hebt van de proefpersoon. Kijk dan of alleen 
een plaatsnaam of het eerste deel van een postcode ook voldoende is en registreer *niet* het hele adres. Deze gegevens 
kunnen op zichzelf meestal niet direct tot identificatie leiden, maar indirect wel. Daarom worden dit ook wel indirecte 
persoonsgegevens genoemd. Indirecte persoonsgegevens zijn overigens nog steeds gewoon persoonsgegevens.

Het moet ook duidelijk zijn wat het doel is van het verzamelen van de gegevens, dit komt terug in de onderzoeksaanvraag 
en je DMP, maar ook in de informatiebrief aan de proefpersonen. Je mag alleen gegevens verzamelen die nodig zijn om dit
doel te bereiken en waar de proefpersoon toestemming voor heeft gegeven. De bottom-line is: vraag niet zo maar alles 
uit omdat je *denkt* dat je het *misschien* nodig gaat hebben en kijk altijd of je met minder of anonieme gegevens kan 
werken. Gebruik hierbij je gezonde verstand en vraag bij twijfel het ISP om advies.

:::{panels}
:header: bg-error

**Persoonsgegevens**
^^^
- Naam en/of initialen
- Geboortedatum
- Adresgegevens
- Telefoonnummer/e-mail/IP/etc.
- BSN, IBAN
- Video/audio
- •••
---
:header: bg-warning

**Indirecte persoonsgegevens**
^^^
- Gender
- Geboortejaar/plaats
- Lengte/gewicht
- Sociaal-economische factoren
- Medische gegevens
- Beroep
- •••
:::

## Anonimiseren vs pseudonimiseren

Het heeft dus de voorkeur om überhaupt geen data te verzamelen die tot heridentificatie kan leiden. Soms moet men echter
wel met data werken die niet volledig anoniem is of wordt data niet volledig anoniem aangeleverd. Anonimiseren en 
pseudonimiseren zijn dan twee methoden om toch zo min mogelijk gegevens te verwerken.

De eerste optie is **anonimiseren**, dat kan door het verwijderen van persoonsgegevens en/of het vervagen van indirecte 
persoonsgevens. Na het anonimiseren moet het *onmogelijk* zijn om de data terug te linken aan de originele participant. 
In praktijk kan dit nog best lastig zijn omdat door variabelen te combineren of door het koppelen van datasets er vaak
toch heridentificatie mogelijk is. Zo lieten Rocher en collega's [^Rocher] zien dat incomplete microdata tot 
heridentificatie van bijna alle inwoners van de VS kan leiden.

Als tussenoplossing kan men de data **pseudonimiseren**. Bijvoorbeeld als je nog contact op moet nemen met participanten
voor een vervolgmeting. Bij het pseudonimiseren verwijder je dan de contactgegevens uit de brondata, maar je bewaart 
ze in een losse versleutelde file die op een andere locatie staat. Hiermee verlaag je het privacy risico voor de 
participanten. Door gebruik te maken van deze 'sleutel' is het mogelijk om de gepseudonimiseerde data te koppelen aan 
de persoonsgegevens. Het is dus nog mogelijk om de data terug te linken aan de originele participant: de data is dus 
per definitie niet anoniem.

In de volgende paar stukken gaan we verder in op [good practices](./3_good_practices), [pseudonimiseren](./3_pseudonimiseren),
en [anonimiseren](./3_anonimiseren).


[^Rocher]: Rocher L, Hendrickx JM, De Montjoye YA. Estimating the success of re-identifications in incomplete datasets 
using generative models. Nature communications. 2019 Jul 23;10(1):1-9.