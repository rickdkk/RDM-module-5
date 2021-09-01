# Spreadsheets

Spreadsheet software kan heel veel en het is daarom verleidelijk om alles te doen in een spreadsheet. Toch kleven er veel
nadelen aan het misbruiken van deze software voor ieder probleem. Over het algemeen is het advies dus om geen data te 
manipuleren, analyseren, of plotten in een spreadsheet. Maar waar zijn ze dan wel handig voor? Het voordeel is dat je
de data goed kan bekijken en dat, met data validatie, het op zich een aardige tool is om data in te voeren. Toch zijn
er mensen die spreadsheets overal voor gebruiken en dat is op zich prima. Ik heb collega's gehad die hele Monte Carlo
analyses in spreadsheets deden. De beste tool is vaak gewoon de tool waar jij het beste mee overweg kan. Er zijn dan wel
een aantal dingen waar je op kunt letten, daar gaan we in dit stuk op in. Voor een uitgebreidere introductie kan je
[hier](https://datacarpentry.org/spreadsheets-socialsci/) kijken.

:::{figure-md} spreadsheets-fig
<img src="../figures/xkcd_spreadsheets.png" alt="xkcd">

xkcd.com over spreadsheets
:::

## Eén spreadsheet één tabel

Het is verleidelijk om meerdere tabellen in één spreadsheet te plakken, dan staat alle info op één plek. Dit maakt het echter
heel lastig om de data later nog te verwerken of te exporteren naar een houdbaar format. Zorg er daarom voor dat er 
één tabel per spreadsheet wordt gebruikt.

## Formatting issues

::::::{margin}
:::{tip}
Gebruik een open source programmeertaal zoals Python, R, of Julia om je data te analyseren en/of transformeren. Gebruik
OpenRefine als je niet wilt scripten.
:::
::::::

Gebruik geen cell highlighting of andere kleurtjes om iets aan te geven in de data, deze waarden kunnen niet ingelezen
worden met andere programma's en als het wel kan kost het vaak veel extra moeite. Als highlighting gebruikt wordt om een
waarde aan te geven, dan moet daar een extra kolom voor komen. Hetzelfde geldt voor het gebruiken van comments, deze 
horen ook thuis in een eigen kolom.

## Gebruik validatie

Wanneer men een online formulier invult wordt er vaak gecontroleerd of de waarde die je invult mogelijk is. Hetzelfde zou
je eigenlijk willen als men data invult in een spreadsheet. Gelukkig hebben Excel en Libreoffice Calc allebei de optie
om data validation te gebruiken. Met data validation kan je aangeven welk soort waarden er in een veld mogen, daardoor
kan je niet per ongeluk een ongeldige waarde invullen. Het is handig om dit te doen voordat je de data gaat invullen,
want als de data er al instaat krijg je wel een indicatie waar de data niet klopt, maar je moet dan wel alle data langs.
Zie [hier](https://datacarpentry.org/spreadsheets-socialsci/04-quality-assurance/index.html) een uitleg over data validatie.

## Werken met datums

Datums in spreadsheets zijn erg tricky. Er zit verschil tussen spreadsheet programma's, tussen regio notaties, en tussen
versies (zie Excel op de Mac vs die op Windows). Sommige waarden worden niet herkend als een datum, bijvoorbeeld als ze 
van voor 1900 zijn en anderen worden soms onterecht herkend als een datum, wat voor veel fouten kan zorgen [^Ziemann]. 
De beste manier om data te formatten in een spreadsheet is door de datum op te splitsen in een jaar, maand, en een dag 
en die in losse kolommen op te slaan. Hiervoor kan men ook de ingebouwde functies `YEAR()`, `MONTH()`, `DAY()` gebruiken.

## Missings

Het is belangrijk om consistent te zijn met missing values. Er zijn hierbij twee dingen belangrijk. Als je een waarde
wel gemeten hebt maar deze is 0, vul dan een 0 in. Het tweede ding is dat men moet kiezen voor consistente waardes
in het geval van missing data. Over het algemeen heeft het de voorkeur om dan geen waarde in te vullen. De meeste programma's
en programmeertalen herkennen dit automatisch als een missing value. Vroeger werd -999 wel eens gebruikt, maar dat is al
lang niet meer nodig voor de computer en kan in een berekening terecht komen met alle gevolgen van dien.

## Good practices

De eerdergenoemde good practices met betrekking tot versiebeheer, het kiezen van kolomnamen, en het aanhouden van een tidy
format gelden uiteraard ook voor spreadsheets!

---

:::{eval-rst}
.. link-button:: ../assignments/2_data_organisatie_opdracht
    :type: ref
    :text: Klaar voor een opdracht!
    :classes: btn-outline-primary btn-block
:::


[^Ziemann]: Ziemann M, Eren Y, El-Osta A. Gene name errors are widespread in the scientific literature. Genome biology. 
2016 Dec;17(1):1-3.