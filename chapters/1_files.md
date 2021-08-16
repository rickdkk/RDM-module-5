# Files organiseren

De naam van een file is belangrijk voor het identificeren van een file, maar ook voor het werken met de file. Geef 
daarom files een logische naam met waar nodig een deel van de metadata in de naam. Afhankelijk van de situatie 
(en persoonlijke voorkeur) kunnen er verschillende keuzes worden gemaakt, maar drie principes blijven leidend[^Bryan]:

1. het moet makkelijk te lezen zijn voor de computer
1. het moet makkelijk te lezen zijn voor de gebruiker
1. het moet goed te sorteren zijn

## Good practices

- **Check of er al een systeem is** bij de andere onderzoekers van de onderzoeksgroep of in de documentatie van het lab.
Als er al een systeem is dan is het vaak beter om hier gebruik van te maken. Leg het systeem vast in het DMP en de 
README.
<br><br>

- **Gebruik geen speciale karakters** zoals `~ ! @ # $ % ^ & * ( ) [ ] { } ; : " ' < > / \ | ?`. In het beste geval moet je er
omheen werken in je eigen scripts en in het slechtste geval kunnen deze botsen met het besturingssysteem of andere
software.
<br><br>
Bijvoorbeeld: Windows staat geen ASCII control karakters toe in filenamen `\/:*?"<>|`. Op Linux en OS-X kan dit wel, 
maar dan kan je collega de bestanden dus niet openen.
<br><br>

::::::{margin}
:::{figure-md} iso-fig
<img src="https://imgs.xkcd.com/comics/iso_8601_2x.png" alt="xkcd" class="bg-primary mb-1">

xkcd.com over het schrijven van data
:::
::::::

- **Gebruik voor een datum altijd ISO-8601** (YYYY-MM-DD), alleen dan kan je makkelijk chronologisch sorteren. 
<br><br>
Bijvoorbeeld: manuscript_2020-12-01.docx of manuscript_2020-12-02.docx
<br><br>
  
- **Houdt ruimte voor hogere getallen** door nullen toe te voegen aan het begin van een getal, dit wordt ook wel zero-padding
genoemd.
<br><br>
Bijvoorbeeld: BloodImage_1.xml wordt opgevolgd door BloodImage_11.xml en niet BloodImage_2.xml. Zorg er daarom voor dat 
je begint met BloodImage_01.xml en op die manier doorgaat met nummeren. 
<br><br>

- **Gebruik geen spaties**, want deze worden gebruikt om commando's te scheiden in de command-line. Gebruik een `-` of 
PascalCase om woorden te scheiden (afhankelijk van voorkeur). 
<br><br>
Bijvoorbeeld: 2020-12-01_BloodImage_001.xml of 2020-12-01_blood-image_001.xml
<br><br>

- **Gebruik een underscore voor verschillende elementen** van een bestandsnaam. 
<br><br>
Bijvoorbeeld: In het bovenstaande voorbeeld is het erg makkelijk om de datum, naam, en metingnummer uit de bestandsnaam 
te halen door de naam te splitsen op de underscore. De volgorde van de elementen bepaalt hoe de bestanden standaard 
gesorteerd worden.
<br><br>  

- **Beschrijf de inhoud van een bestand** en geef het niet alleen een getal. Een file zoals figuur_3.png zorgt meteen 
voor verwarring wanneer er een figuur wordt toegevoegd of verwijderd in het manuscript. Beschrijf daarom ook altijd de 
inhoud van een file met de naam.
<br><br>
Bijvoorbeeld: beurskoers_gme.png of BloodImage_001.png
  
### Quiz

`````{panels}
Welke van deze voorbeelden is geschikt:
^^^
```{dropdown} Abstract for ISB 2020-08-16.docx
:title: + p-2
:body: + p-2 bg-warning
**Fout:** de filenaam bevat spaties, dat kan het automatiseren van analyses verhinderen.
```
```{dropdown} 2021-08-16_abstract-for-isb.docx
:title: + p-2
:body: + p-2 bg-success
**Correct:** de datum is in YYYY-MM-DD, het is duidelijk wat de inhoud van de file is, en de file 
bevat geen speciale karakters.
```
```{dropdown} abstract-for-isb_16-08-2021.docx
:title: + p-2
:body: + p-2 bg-warning
**Fout:** de datum is niet op een sorteerbare volgorde gegeven, gebruik altijd YYYY-MM-DD.
```
---
Welke van deze voorbeelden is geschikt:
^^^
```{dropdown} fig01_regplot-speed-vs-power.png
:title: + p-2
:body: + p-2 bg-success
**Correct:** er is zero-padding toegepast en het is direct duidelijk om welk figuur het gaat.
```
```{dropdown} Figure_01.png
:title: + p-2
:body: + p-2 bg-warning
**Fout:** er is zero-padding gebruikt, maar het is niet direct duidelijk wat de inhoud van de file is.
```
```{dropdown} figure_1_2020-08-16.png
:title: + p-2
:body: + p-2 bg-warning
**Fout:** er is een versienummer toegevoegd op basis van de datum, maar het is niet duidelijk wat de inhoud van de file is.
```
``````

## Een systeem: voorbeeld

Hieronder volgt een voorbeeld uit een onderzoek naar rolstoelpropulsie op een ergometer. Aan het begin van het project 
was duidelijk dat het zou gaan om ongeveer 1000 files, dus er was een strategie voor het benoemen van files afgesproken, 
zodat de studenten die hielpen met de dataverzameling direct alles in het juiste format konden opslaan. Er is gekozen 
voor een strategie die de 'nesting' van de data reflecteerde: er zijn meerdere proefpersonen, die worden meerdere keren 
gemeten, met meerdere meetinstrumenten. De bestandsnaam kreeg dus de volgende hiërarchische opbouw:

\<**experiment**\>\_\<**proefpersoon**\>\_\<**meting**\>\_\<**meetinstrument**\>.\<**extensie**\>

Bijvoorbeeld: `WL_PP01_T01_ergometer.xls`, ofwel de ergometerdata van het 'WL' experiment van proefpersoon 01 op tijd 01.
Hiermee is alle metadata van een bestand direct beschikbaar in de filenaam en zijn de namen 'machine readable', daardoor 
kunnen we met regular expressions en/of door te ‘globben’ gemakkelijk data selecteren. Met deze structuur kunnen we 
na de data verzameling, bijvoorbeeld, alle data van proefpersoon 1, alle ergometer data, of alle ergometer data van T1 
selecteren:

```{tabbed} Python
![](../figures/glob_ipython.png)
```

```{tabbed} R
![](../figures/glob_radian.png)
```

```{tabbed} Julia
![](../figures/glob_julia.png)
```

```{tabbed} Shell
![](../figures/glob_find.png)
```

```{tabbed} Explorer
![](../figures/glob_explorer.png)
```

Het is hierbij dus erg belangrijk dat de bestandsnamen consistent en voorspelbaar zijn. Een typo kan ertoe leiden dat
er bestanden worden overgeslagen. Leg dus ook goed vast wat de conventie is m.b.t. het zero-padden van nummers en het 
gebruik van hoofdletters. De voordelen zijn echter gigantisch: het handmatig selecteren van 100 of 200 files is onbegonnen
werk. Als dan later blijkt dat er toch een nét een iets andere selectie nodig was is dat ook geen probleem.


[^Bryan]: Bryan J. Naming things. 2015 May 04. Retrieved from: https://speakerdeck.com/jennybc/how-to-name-files
