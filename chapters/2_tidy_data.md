# Tidy data

Data komt zelden in een format waarin je het direct kan gebruiken voor analyse. Er gaan vaak veel stappen aan vooraf en 
er wordt ook wel gezegd dat 80% van de analysetijd gaat zitten in het opschonen en transformeren van de data. Een goede
manier om data te organiseren voor analyse is door gebruik te maken van het *tidy* format: tidy data 
[^Tidy]<sup>,</sup>[^Tidyr]. Zolang de data past in een spreadsheet (2D) vorm, heeft dit format (meestal) de voorkeur. 
Het principe van tidy data is simpel: 

1. Elke variabele krijgt een kolom
1. Elke observatie is een rij
1. Elke waarde heeft zijn eigen cell

De eerste rij van een tabel is de header. Iedere kolom is een variabele, dus iedere kolom heeft een eigen unieke header. 
De header naam bevat geen speciale karakters, geen spaties, en begint niet met een getal. Hieronder staat een voorbeeld
van tidy en messy data [^DSR]:

:::{panels}
:header: bg-success

**Tidy**
^^^
| country     |   year |   population |
|:------------|-------:|-------------:|
| Afghanistan |   1999 |     19987071 |
| Afghanistan |   2000 |     20595360 |
| Brazil      |   1999 |    172006362 |
| Brazil      |   2000 |    174504898 |
| China       |   1999 |   1272915272 |
| China       |   2000 |   1280428583 |
---
:header: bg-error

**Non-tidy**
^^^
| country     |       1999 |       2000 |
|:------------|-----------:|-----------:|
| Afghanistan |   19987071 |   20595360 |
| Brazil      |  172006362 |  174504898 |
| China       | 1272915272 | 1280428583 |
:::

In het bovenstaande voorbeeld bevat de rechter tabel non-tidy of messy data. Dat komt omdat variabelen zowel in rijen als
in kolommen staan. Op het eerste gezicht zullen de meeste mensen, misschien een voorkeur hebben voor de rechter tabel, 
maar het verwerken van deze data wordt al snel vervelend wanneer men berekeningen wil uitvoeren op de tabel. Men moet dan
goed oppassen met indexeren op basis van de kolomnamen. In het linkervoorbeeld is het bijvoorbeeld veel makkelijker om de
populatie door een andere variabele te delen of vermenigvuldigen. 

```{epigraph}
Tidy datasets are all alike, but every messy dataset is messy in its own way.

-- Hadley Wickham [^Tidy]
```

## Messy data

Het concept van tidy data klinkt simpel en bestaat al een hele tijd. Toch zijn het overgrote deel van de datasets in "het
wild" niet tidy. Een aantal veelvoorkomende problemen (naast de eerdergenoemde in de good practices) met data zijn:

- **Column headers zijn waarden:** dit is ook het geval in de bovenstaande tabel. Hier is de variable 'jaar' verspreid
over verschillende kolommen en staat de waarde in de header.
<br><br>

- **Meerdere variabelen in één kolom:** een voorbeeld hiervan is bijvoorbeeld de waarde m24 om een man van 24 aan te 
duiden in de data. In zo'n geval moet men dus de kolom splitsen naar één kolom voor sekse en één kolom voor leeftijd.
<br><br>

- **Variabelen in rijen en kolommen:** dit gebeurt als een deel van de data tidy is en een ander deel van de data niet.
Een goed voorbeeld hiervan staat [hier](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html).
<br><br>

- **Meerdere types in zelfde tabel:** als er veel beschrijvende data in een dataset zit is er bij tidy data veel herhaling
in de data. Bijvoorbeeld als men eenmalig bepaalde eigenschappen meet van iemand en vervolgens elke dag een vervolgmeting 
op een andere variabele doet. In zo'n geval kan het handig zijn om de data op te splitsen naar meerdere tabellen (één met
de proefpersooneigenschappen en één met iedere individuele meting) en die aan elkaar te linken.
<br><br>

- **Zelfde waarde in meerdere tabellen:** dit is een veelvoorkomend probleem als men meerdere metingen doet. Hierdoor kan
het voorkomen dat informatie op meerdere plekken tegelijk staat. Dit kan verwarrend werken en kan ervoor zorgen dat men op
meerdere plekken iets moet aanpassen. In zo'n geval moet men de tabellen combineren naar één hoofdbestand. Het project
[goodtables.io](https://goodtables.io/) van Frictionless Data kan een dataset checken op 'tidyness'.
  
Andere problemen met messy data komen vaak voor doordat men werkt in spreadsheet software. Daar gaan we in het volgende
stuk op in!

[^Tidy]: Wickham H. Tidy data. Journal of statistical software. 2014 Sep 12;59(1):1-23. http://www.jstatsoft.org/v59/i10/paper
[^Tidyr]: https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html
[^DSR]: https://github.com/garrettgman/DSR