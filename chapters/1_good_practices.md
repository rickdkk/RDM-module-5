# Good (enough) practices

Een groot deel van de aanbevelingen op deze pagina zijn gebaseerd op 1) de constatering dat data opslag ongelofelijk
goedkoop is en tijd erg duur en 2) data geschikt moet zijn voor analyse (d.w.z. tidy) en archivering. Op het moment van
schrijven is de prijs van een harde schijf ongeveer 2 cent per GB. De prijs van het kwijtraken of beschadigen van data
is echter velen malen groter en kan een project zo maar een jaar vertragen. Zonder een heel verhaal over FAIR op te
hangen zijn er een aantal belangrijke tips and tricks die men kan gebruiken voor het goed genoeg beheren van data:

:::{figure-md} markdown-fig
<img src="https://imgs.xkcd.com/comics/digital_resource_lifespan.png" alt="xkcd" class="bg-primary mb-1">

xkcd.com on the lifespan on digital resources
:::

## Sla je ruwe data op

::::::{margin}
:::{tip}
Zet de map met de ruwe data op read-only. Dat kan op Windows, Mac, en Linux gewoon via de file explorer!
:::
::::::

Zorg dat de ruwe data altijd los is opgeslagen. Het kan zijn dat een meetinstrument een rapport uitdraait of dat je direct
aan de slag wil met de data. Vooral bij programma's die data opslag en verwerking/visualisatie combineren (bijv. Excel)
is dit erg verleidelijk. Maar zonder toegang tot de ruwe data is de enige manier waarop je weer toegang tot de
originele informatie kan krijgen door een meting te herhalen. De ruwe data hoort daarom thuis in een losse map die
ofwel read-only is of een extra back-up heeft, en het liefst beide. Je kan dan een 'werkkopie' maken waarmee je aan
de slag kan.

## Zorg voor een back-up

Een back-up is essentieel! Harddrives gaan kapot, laptops worden gestolen, en files kunnen worden overschreven. De enige
manier om er zeker van te zijn dat je data veilig is, is met een back-up. Werk dus niet alleen met de data op je lokale
computer, maar zorg er ook voor dat het project in [Fontys Research Drive](https://fontys.data.surfsara.nl/index.php/login)
staat.

## Verwerk de data

We kennen allemaal de oude Windows-98 computer achterin het lab waar de software opstaat van die ene dure sensor. Die
computer die tevens de enige computer is met de software om de ruwe data om te kunnen zetten naar een verwerkbaar format. Om
ervoor te zorgen dat we niet afhankelijk zijn van deze computer moeten we de data zo snel mogelijk omzetten naar een
houdbaar format.

Kies dus een format dat lang mee kan gaan en waar geen specifieke software voor nodig is om het te openen. Een goed
format is future-proof en simpel. In praktijk zijn dit veelal text files zoals .csv voor 'spreadsheet' data of .txt
voor tekst. Voor een overzicht van geschikte formats kan men kijken bij [DANS](https://dans.knaw.nl/en/about/services/easy/information-about-depositing-data/before-depositing/file-formats)
en [4TU](https://data.4tu.nl/info//fileadmin/user_upload/Documenten/preffered_file_formats.pdf).
Hieronder een aantal voorbeelden:

```{tabbed} Duurzaam
- Markup: XML, HTML
- Data: CSV, JSON, ODS
- Documenten: PDF, ODT, TXT
- Afbeeldingen: JPEG, PNG, SVG
- Video: MXF, MKV
```

```{tabbed} Niet-duurzaam
- Markup: SGML
- Data: SPSS (SAV), MDB, XLSX
- Documenten: DOC, DOCX, RTF
- Afbeeldingen: AI, EPS, WMF
- Video: MPEG-4, AVI, MOV
```

Er bestaat bij het converteren van bestanden altijd een risico dat informatie verloren gaat, bewaar daarom ook de
originele file totdat je het project hebt afgerond. Soms is het (nog) niet mogelijk om data in een open format op te
slaan. Als er een ander format beschikbaar is dat een 'industrie standaard' is dan kan dat format worden gebruikt, maar
op de lange termijn zou alles in een open format opgeslagen moeten worden.

## Beschrijf de data

De data moet beschreven worden zodat jij en anderen weten wat voor een data het precies betreft. Er zijn verschillende
niveaus van metadata. Allereerst moet de dataset zelf beschreven worden, dat is bijvoorbeeld nodig om de data terug te
kunnen vinden in DataverseNL. Dan moet de inhoud van de dataset zelf nog beschreven worden, hiervoor is een goede
[README](https://nl.wikipedia.org/wiki/README) de meest waardevolle toevoeging. Op de volgende pagina gaan we hier verder
op in, maar in het kort: een README is een bestand (meestal in plain text) die informatie geeft die gebruikers eerst moeten
lezen.

## Archiveer de data

Onderzoeksdata moet minimaal 10 jaar bewaard blijven (15/20 jaar voor medische data). Het archiveren van data is dus een
belangrijke stap in het onderzoeksproces. Bij voorkeur wordt de data openbaar gemaakt, maar als dat niet kan dan kan het
ook gesloten gearchiveerd worden. Fontys beschikt over DataverseNL. Hier kunnen de data zowel open als gesloten
gearchiveerd worden. Door al het voorwerk dat is gedaan in de voorgaande secties is het archiveren van data zo gebeurd.
De organisatie is al op orde, evenals de documentatie, en de data staat al in een houdbaar format.

<a href="https://dataverse.nl/dataverse/fontys/">
    <img src=https://dataverse.nl/assets/logos/DataverseNL-logo.png alt="DataverseNL logo" width="200px">
</a>


## Gebruik een systeem

Tot nu toe is er nog niets gezegd over hóe de data moet worden opgeslagen. Welke mappenstructuur is handig voor
onderzoek en hoe moet ik de files noemen? Daar gaan we in het volgende stuk op in!
