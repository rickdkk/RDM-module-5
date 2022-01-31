# Good practices

Er zijn veel verschillende soorten data formats en iedereen werkt met verschillende analysetools. Toch zijn er een aantal 
praktische aanbevelingen die we kunnen doen om data zo te organiseren dat het geschikt is voor analyse en archivering.

::::::{margin}
:::{figure-md} extensions-fig
<img src="../figures/xkcd_file_extensions.png" alt="xkcd">

xkcd.com over file extensies
:::
::::::

- **Gebruik open formats** voor de opslag van data. Dit werd al kort behandeld bij {doc}`./1_good_practices`. Het kan ook
van invloed zijn op de inhoud van de data. Het kan betekenen dat data getransformeerd moet worden en/of dat metadata ergens
anders komt te staan.
<br><br>

- **Hou mutaties bij** en werk in een kopie van de data, pas nooit de ruwe data aan. Hou transformaties bij in een los 
document (CHANGELOG), een script, met [OpenRefine](https://openrefine.org/), of door bijv. de SPSS syntax op te slaan.
<br><br>

- **Gebruik consistente waarden** door bijvoorbeeld een [data dictionary](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary)
of taxonomie/ontologie te gebruiken en/of door data validatie toe te passen op de data als deze handmatig wordt ingevuld.
<br><br>

- **Let op missings** en leg een systeem vast om met missing data om te gaan. Vroeger gebruikte men daarvoor vaak de 
waarde 999, maar tegenwoordig kan de meeste software gewoon omgaan met missings. Gebruik je toch speciale waarden? Leg
dit dan vast in het DMP/README/dictionary en zorg dat iedereen hiervan op de hoogte is.
<br><br>

- **Gebruik descriptieve headers** en/of variabele namen. Probeer ervoor te zorgen dat mensen zo min mogelijk hoeven te
zoeken wat een variabele betekent. Met descriptieve headers is de data al voor een heel deel zelf-documenterend.
<br><br>

- **Gebruik versienummers** of version control (bijv. Git LFS of DVC). Hou versies bij als de data wordt aangevuld of 
aangepast en spreek met je collega's af welke versiestrategie je gebruikt.
<br><br>

- **Gebruik .csv in plaats van .xlsx** of in ieder geval .ods voor spreadsheet data. In praktijk wordt (te) veel data in
spreadsheets bewaard. Door gebruik te maken van .csv (comma separated values) bestanden kunnen we ervoor zorgen dat de 
data makkelijk te verwerken is met andere tools en dat het bestand niet beschadigd raakt. Een bijkomend voordeel van 
.csv is dat men niet verleid kan raken om formatting als data te gebruiken of om data en analyse te mixen.
<br><br>

- **Gebruik geen spreadsheet programma** voor analyses of plotten. Het voornaamste probleem is dat het moeilijk is om 
te zien wat de flow van data is in een spreadsheet. Er zijn gespecialiseerde programma's die dit werk op een 
reproduceerbaardere manier kunnen verrichten. Spreadsheets zijn wel geschikt voor data entry, dat onderwerp wordt behandeld
in {doc}`2_spreadsheets`
<br><br>

- **Gebruik een tidy format**: {doc}`2_tidy_data`
