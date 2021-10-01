# Anonimiseren

Door data te anonimiseren is deze niet meer te herleiden tot een specifiek persoon. Anonimiseren is
*destructief*. Dat wil zeggen dat data onomkeerbaar aangepast worden en dat er vaak wat informatie verloren
gaat. Vaak is de data die je publiceert in het artikel al anoniem doordat de data samengevoegd zijn, maar als je de
dataset zelf wil publiceren moet je ook zorgen dat in die grotere dataset geen herleidbare gegevens zitten.
::::::{margin}
:::{caution}
Pseudonimiseren staat dus niet gelijk aan anonimiseren. Het versleutelen van informatie staat ook niet gelijk aan 
anonimiseren.
:::
::::::
Het kan nog best een uitdaging zijn om de data goed te anonimiseren omdat volgend de AVG het *onmogelijk* moet zijn om
de participant te kunnen identificeren. Het voordeel is echter dat wanneer de data volledig geanonimiseerd is deze niet 
meer onder de AVG valt. Er is daarna dus een stuk meer mogelijk met de data, bijvoorbeeld wanneer men deze wilt delen
of hergebruiken bij vervolgonderzoek.

## Aanpak

Eerst is het goed om te kijken naar de onderzoekspopulatie zelf. Als je een willekeurige sample studenten hebt gebruikt
voor een studie is de kans op heridentificatie een stuk kleiner dan wanneer men met data van een hele populatie werkt 
zoals met microdata of een grote clinical trial. Daarna is de volgende stap uiteraard om te controleren dat alle directe 
identifiers uit de data zijn verwijderd. Het verwijderen van indirecte identifiers kan echter een stuk lastiger zijn. 
Zo kan het zijn er maar één proefpersoon is met een bepaalde eigenschap (bijv. iemand die 2.15m lang is) of dat er maar
één persoon is met een bepaalde combinatie van indirecte gegevens. Er zijn verschillende transformaties die we kunnen 
doen op de data om ervoor te zorgen dat deze indirecte gegevens geen probleem veroorzaken:

1. **Sampling:** het publiceren van een sample van de data en niet de complete dataset. Dit is met name relevant als de data
een hele populatie beschrijft, bijv. bij microdata of ziekenhuisdata.
1. **Aggregation:** door resultaten te aggregeren (bijv. door het gemiddelde te nemen)
1. **Surpression:** door bepaalde waarden niet te laten zien als die bijv. uniek zijn voor die persoon of die persoon uniek
in de dataset maakt. Voor outliers kan men ook de waarden aftoppen of de outlier helemaal niet meenemen.
1. **Masking:** door een deel van de informatie te verstoppen. Een goed voorbeeld hier zijn postcodes, door de laatste cijfers
en letters te verbergen wordt de geografische locatie steeds minder specifiek.
1. **Categorizeren:** door 'bins' te maken waarin een proefpersoon valt kan men het detail vervagen. Dit werkt goed voor gewicht
of lengte, maar bijvoorbeeld ook bij inkomen.
1. **Generaliseren:** door gegevens op een hoger abstractieniveau weer te geven. Denk hier bijvoorbeeld aan ziektes 
adhv een hoger niveau op de [classification of diseases](https://www.who.int/standards/classifications/classification-of-diseases) 
of beroepen op een hoger niveau in de [International Standard Classification of Occupations](http://www.ilo.org/public/english/bureau/stat/isco/isco08/index.htm).
1. **Disruption/swapping:** door gegevens te verwisselen, dit kan met name bij kwalitatief onderzoek handig zijn als het
detailniveau in een transcript niet heel belangrijk is. Bijvoorbeeld door \[broer\] te vervangen met \[zus\] bij een 
transcript kan je het risico op heridentificatie verlagen.
<br><br>

```{figure} ../figures/prasser_transformation_methods.webp
---
name: anonimization-fig
width: 75%
---
Transformatie methoden voor anonimisering CC-BY-NC [^Prasser].
```

## Tools

::::::{margin}
:::{note}
Bij kleinschalig onderzoek is dit vaak niet nodig/praktisch.
:::
::::::

Het is erg lastig om alle verschillende combinaties van indirecte identifiers na te gaan om te kijken of iemand 
geheridentificeerd kan worden. Gelukkig zijn er verschillende tools die hierbij kunnen helpen, die verschillende
privacy modellen ondersteunen. Die modellen hebben vaak catchy namen zoals 𝛿-Presence, 𝛽-Likeness, k-Anonymity, of t-Closeness. Het
makkelijkste voorbeeld is k-Anonymity: een dataset is k-anoniem als voor elke combinatie van indirecte identifier er op
zijn minst k andere zijn. Een veelgebruikt getal voor k is 5, dan zijn er voor elke combinatie van variabelen op zijn minst
vijf samples met dezelfde combinatie van gegevens. Om dit met de hand te doen is erg lastig (ook om te programmeren overigens)
dus men kan dan het beste een tool als [ARX](https://arx.deidentifier.org/) of [Amnesia](https://amnesia.openaire.eu/) 
gebruiken. Anonimiseren werkt voor iedere dataset anders, overleg daarom bij twijfel met de Privacy Officer en je Data
Supporter.

---
:::{eval-rst}
.. link-button:: ../assignments/3_data_minimalisatie_opdracht
    :type: ref
    :text: Klaar voor een opdracht!
    :classes: btn-outline-primary btn-block
:::

[^Prasser]: Prasser F, Eicher J, Spengler H, Bild R, Kuhn KA. Flexible data anonymization using ARX—Current status and 
challenges ahead. Software: Practice and Experience. 2020 Jul;50(7):1277-304.