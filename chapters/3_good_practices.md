# Good practices

Bij de vorige twee hoofdstukken waren de good practices voornamelijk aanbevelingen om ervoor te zorgen dat je jezelf
tijd en moeite kan besparen. Als het gaat om het anonimiseren en pseudonimiseren van data gaat het meestal niet meer om
aanbevelingen, maar om het voldoen aan de regels.

- **Ga voor anonieme data**. Probeer het onderzoek altijd zo op te zetten dat er geen identificeerbare data verwerkt
hoeft te worden.
<br><br>
- **Plan vroeg in het onderzoek** en schrijf het op in je DMP. Door vroeg te plannen kom je niet voor verassingen te staan
en door het vast te leggen weet iedereen hoe die moet omgaan met de data.
<br><br>
- **Leg de manipulaties vast** zodat je weet wat er is gebeurd met de data. Dit kan door de manipulaties automatisch te 
doen en het script te bewaren of door een logboek bij te houden.
<br><br>
- **Gebruik betekenisvolle vervangingen** in kwalitatieve data. Vervang in getranscribeerde interviews de tekst met 
\[haakjes\] of gebruik \<Auteur\>XML tags\<\/Auteur\>.
<br><br>
- **Print geen documenten met persoonsgegevens**. Het is erg moeilijk om papieren documenten te beveiligen en te
bewaren. Het beste is om zoveel mogelijk met digitale bestanden te werken.
<br><br>
- **Bewaar niet langer dan nodig**. Als je identificeerbare gegevens opslaat en deze niet langer nodig hebt, verwijder
ze dan direct.

## De 'Five Safes'

Een framework wat kan helpen bij het beschrijven en ontwerpen van onderzoek is het "Five Saves" framework [^Desai]. In
dit framework is aandacht voor de data, maar ook voor de organisatie rondom de data:

- Veilige projecten: is het gebruik van de data gepast (nodig, ethisch, wettelijk, redelijk, etc.)?
- Veilige mensen: kunnen de gebruikers van de data vertrouwd (kennis, vaardigheden, motieven) worden?
- Veilige data: zitten er veiligheidsrisico's in de data zelf?
- Veilige settings: wie heeft toegang tot de data?
- Veilige output: zijn de statistische resultaten niet onthullend?

## Voorbeeld: (medische) biomechanica

In de biomechanica wordt gebruik gemaakt van veel verschillende meetinstrumenten. Denk bijvoorbeeld aan apparatuur om de
zuurstofopname te registreren, de hartslag, 3D positie in de ruimte, en weegcellen. Deze sensors zijn vaak bedoeld voor
de medische markt en de software die bij de instrumenten hoort is vaak bedoeld voor artsen. Dat betekent dat de software
een mooi rapportje uit kan draaien met de belangrijkste uitkomsten. Hiervoor vraagt de software altijd van alles over de
proefpersoon: naam, geboortedatum, lengte, gewicht, etc. Leuk voor een arts, maar erg onhandig voor een onderzoeker die
zich aan de AVG wil houden.

Een student vult, zonder nadrukkelijke instructie, deze gegevens meestal gewoon in. Het apparaat vraagt immers zelf om de 
gegevens. Maar daardoor zijn al deze gegevens opgeslagen in ieder apparaat en ieder document. Door hier van tevoren al 
rekening mee te houden in het meetprotocol kunnen we ervoor zorgen dat deze data niet overal komt te staan. Soms vergt
dit wat extra testen om te kijken hoe het apparaat omgaat met dummy data, maar eigenlijk gaat het altijd wel goed. Dit 
verlaagt het risico op het verlies van deze data aanzienlijk en scheelt veel werk bij het archiveren van de data.


[^Desai]: Desai T, Ritchie F, Welpton R. Five Safes: designing data access for research. https://core.ac.uk/download/pdf/323894811.pdf