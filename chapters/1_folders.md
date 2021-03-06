# Mappen organiseren

Een duidelijke projectstructuur kan bijdragen aan de reproduceerbaarheid en efficiëntie van het onderzoek. Het 
bepalen van een systeem voor het bewaren van bestanden is dan ook een van de eerste stappen binnen een nieuw project. 
Op deze pagina gaan we in op de mapstructuur van een onderzoeksproject en op de volgende pagina gaan we verder in op de
inhoud: de bestanden. 

De meeste mensen zijn het er over eens dat ieder project in een eigen map moet, maar daarna zijn er veel verschillende 
systemen te bedenken. Hieronder benoemen we eerst een aantal good practices die altijd gelden en daarna presenteren we 
een minimalistische mapstructuur die geschikt is voor onderzoek. Bij elk project hoort een README, dus die wordt ook
behandeld in dit stuk.

## Good practices
::::::{margin}
:::{figure-md} old-files-fig
<img src="../figures/xkcd_old_files.png" alt="xkcd">

xkcd.com over oude files/data
:::
::::::
- **Check wat de standaard is in jouw onderzoeksgroep** zodat het project aansluit bij bestaande en andere lopende 
projecten. Bedenk niet zelf een systeem als dat niet strikt noodzakelijk is.
<br><br>

- **Kies een systeem en leg dit vast in het DMP en de README**. Door het vast te leggen is het direct voor iedereen 
duidelijk welke structuur gebruikt gaat worden. Zo kunnen collega's en studenten meteen de juiste structuur aanhouden. 
Iets wat tijdens het automatiseren en archiveren veel tijd gaat schelen.
<br><br>

- **Kies betekenisvolle namen** voor de mappen zodat men niet de inhoud hoeft te controleren om te kijken wat er in zit.
Hiermee documenteert het project (deels) zichzelf en zorg je ervoor dat men snel eigen kan worden met het project.
<br><br>

- **Kies handige namen**: In Research Drive beginnen standaard alle namen van mappen met een afkorting van het project. 
Daarnaast is het goed om geen spaties of speciale tekens te gebruiken (zie ook [files](1_files.md)).
<br><br>

- **Maak een beperkt aantal mappen in de hoofdmap (root)** en maak specifiekere mappen in sub-mappen of sub-sub-mappen. 
Zorg er wel voor dat de structuur niet onnodig complex wordt, dan is het beter om de context van de bestanden in een 
los bestand op te slaan (metadata) of om te werken met een database systeem.
<br><br>

- **Splits data en gegenereerde content van handbewerkte content**. Hierdoor zorg je ervoor dat automatisch 
gegenereerde data of read-only data niet worden aangepast en dat files die wel met de hand worden aangepast niet worden 
overschreven.
<br><br>

- **Zet een README in de hoofdmap** van het project zodat iedereen direct weet waar men moet beginnen. Met een README
zorg je er voor dat jij en je collega's over een paar maanden nog steeds weten waar alles staat en hoe je het project moet
gebruiken (zie ook: {ref}`readme-label`).
<br><br>

- **Zorg ervoor dat alles aanwezig is om de analyse te herhalen**. In het geval van projecten waar handmatig met data is
gewerkt moet er een uitgebreide handleiding aanwezig zijn en voor geautomatiseerde stappen moeten er scripts zijn die
vanuit de gegeven mapstructuur werken met de aanwezige configuratiefiles.
<br><br>

(example-label)=
## Een systeem: voorbeeld

::::::{margin}
:::{tip}
Deze mapstructuur is [hier](https://gitlab.com/Rickdkk/good-enough-project) ook beschikbaar als cookiecutter: `cookiecutter gl:rickdkk/good-enough-project`.
Een uitgebreidere versie gericht op data science is [hier](https://github.com/drivendata/cookiecutter-data-science) te vinden.
:::
::::::

Er is niet één mappenstructuur die werkt voor al het onderzoek, daarom volgt hier een voorstel voor een minimalistische
structuur waarin de voorgaande basisprincipes terugkomen. Deze structuur is gebaseerd op de 'good enough project' van 
Barbara Vreede [^BVreede]. Het betreft een sjabloon met een aantal bestanden en mappen die aanwezig zouden moeten zijn
in ieder project. Er wordt onderscheid gemaakt tussen de volgende bestandstypes:

- read-only (RO): worden niet aangepast door code of de onderzoeker.
- human-writeable (HW): worden alleen aangepast door de onderzoeker.
- project-generated (PG): folders die worden gegeneerd door het runnen van de code, deze worden elke keer opnieuw
gegenereerd als alle code wordt gerunned.

```
.
├── .gitignore         <- Files die niet in version control zitten
├── CITATION.cff       <- Hoe het project te citeren
├── LICENSE            <- Copyright informatie
├── README.md
├── requirements.txt   <- Vereisten voor het reproduceren van de analyse (PG)
├── bin/               <- Gecompileerde code, genegeerd door git (PG)
│   └── external/      <- Externe code, genegeerd door git (RO)
├── data/              <- Alle projectdata, genegeerd door git
│   ├── processed/     <- De definitieve dataset voor modellering (PG)
│   ├── raw/           <- De originele, read-only data (RO)
│   └── temp/          <- Getransformeerde data (PG)
├── docs/              <- Documenten voor gebruikers (HW)
│   ├── manuscript/    <- Manuscript data, e.g., LaTeX, Markdown, etc. (HW)
│   └── reports/       <- Andere rapportages of notebooks (e.g. Jupyter, .Rmd) (HW)
├── results/
│   ├── figures/       <- Figures voor het manuscript of andere rapportages (PG)
│   └── output/        <- Andere output voor het manuscript etc. (PG)
└── src/               <- Source code voor dit project (HW)

```

De `CITATION`, `LICENSE`, en `README` files zijn allemaal nodig om het project te kunnen gebruiken. Hiermee kunnen mensen
erachter komen hoe ze, respectievelijk, het project kunnen citeren, wat ermee kan en mag, en zich snel oriënteren 
op de inhoud van het project. De `.gitingore` zorgt ervoor dat Git weet welke files niet onder version control horen. 
De mappen zelf maken een logische scheiding op inhoud en type van de files.

(readme-label)=
## De README

::::::{margin}
:::{tip}
READMEs worden vaak in markdown gemaakt (net als deze pagina!). Zie [hier](https://www.markdownguide.org/basic-syntax/) 
een overzicht van de syntax. Fontys Research Drive beschikt over een markdown editor!
:::
::::::

In ieder project hoort in de hoofdmap een README en waar nodig in sub-mappen een specifiekere README. Deze README
beschrijft de inhoud van het project en hoe men aan de slag kan met die inhoud.
Veelvoorkomende formats zijn `.txt`, `.md` (Markdown), en `.rst` (reStructuredText), dat zijn allemaal platte text formats, 
maar de laatste twee hebben een aantal extra opties om documenten op te maken. Iedereen met een text editor (bijv. Kladblok)
kan een README bestand dus openen. De README is waarschijnlijk een van de eerste dingen die iemand zal lezen als die het 
project te zien krijgt. Het is daarmee ook wel het visitekaartje van het project. Zie 
[hier](https://connect.fontys.nl/fontysbreed/opo/ResearchDataManagement/Gedeelde%20%20documenten/README%20file%20-%20format.docx)
het Fontys format.

Op GitHub/GitLab worden READMEs in een repository ook omgezet in een pagina. Een voorbeeld is 
[deze](https://github.com/willmcgugan/rich#readme) pagina die gemaakt is op basis van 
[deze](https://raw.githubusercontent.com/willmcgugan/rich/master/README.md) README in .md format. Zoals je kan zien in 
het voorbeeld kan er heel veel in een README, maar voor onderzoek moeten een paar dingen altijd aanwezig zijn:

- Een titel
- Een beschrijving/abstract
- De indeling/organisatie van het project
- Wat er allemaal nodig is om aan de slag te kunnen
- Informatie over de licentie
- Informatie over citeren

Daarnaast kan men nog extra informatie verstrekken over de auteurs, methodologie, etc. Hier heb je in principe veel 
vrijheid, maar probeer wel aan te sluiten bij de standaarden die er zijn in jouw vakgebied of onderzoeksgroep. De 
metadata formulieren die bij de repository horen zijn voor het automatisch indexeren (door computers) bedoeld, maar dit 
stukje metadata is echt bedoeld voor mensen. Schrijf het dus ook voor mensen en probeer ze enthousiast te maken over
jouw project!

[^BVreede]: https://github.com/bvreede/good-enough-project
