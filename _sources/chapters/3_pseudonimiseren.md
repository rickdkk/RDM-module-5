# Pseudonimiseren

Bij pseudonimiseren worden herleidbare data vervangen door een pseudoniem (ook wel token) die wordt opgeslagen in een 
sleutelbestand. Door het sleutelbestand te gebruiken kan je de data weer reconstrueren. 
Pseudonimiseren kan bijvoorbeeld handig zijn als de naam van de proefpersoon nogmaals gebruikt moet worden
om contact op te nemen voor een vervolgmeting of om resultaten te delen (bijv. in medisch onderzoek). Men kan de 
naam/adresgegevens niet naast de rest van de data bewaren, maar deze kan men wel bewaren in een sleutelbestand die
op een andere plek staat opgeslagen en goed is beveiligd. Pseudonimiseren beschermd de identiteit van de participanten
zolang de data goed genoeg is gepseudonimiseerd, het niet mogelijk is om de data tussen datasets te linken, en het 
pseudoniem niet teruggedraaid kan worden. Zolang de sleutel nog bestaat is de data dus niet anoniem.
En als de sleutel is verwijderd kan het zijn dat er nog aanvullende stappen nodig zijn voordat de data echt anoniem is.

:::{caution}
Gepseudonimiseerde data is nog steeds persoonlijke data en moet als zodanig behandeld worden. Pas als het *onmogelijk* is
om de participant te herleiden spreken we van anonieme data. 
:::

## Sleutelbestand

In het sleutelbestaand staan de persoonsgegevens die beschermd moeten worden naast de tokens die zijn toegeschreven aan
de andere data. Met het sleutelbestand kan men de data weer reconstrueren. Het is daarom belangrijk dat het 
sleutelbestand op een aparte en veilige plaats staat opgeslagen. [Opdracht 3](../assignments/3_data_minimalisatie_opdracht.md)
gaat in op het pseudonimiseren van data. In 2019 heeft LCRDM [^LCRDM] een stappenplan opgesteld om data te pseudonimiseren,
hier volgt een korte samenvatting:

1. Bedenk van tevoren welke data je wilt pseudonimiseren en hoe je dat gaat doen. Leg dit vast in je DMP.
1. Verwijder data die je niet nodig hebt meteen. Vervang data die voor identificatie nodig zijn met een pseudoniem.
1. Gebruik verschillende pseudoniemen voor verschillende datasets zodat data niet gekoppeld kan worden.
1. Bewaar het sleutelbestand op een veilige plek, los van de onderzoeksgegevens.
1. Zorg voor een back-up en goede beveiliging van zowel de data als het sleutelbestand.
1. Beperk de toegang tot het sleutelbestand, maar zorg er wel voor dat er altijd nog iemand is die ook toegang heeft
tot het bestand.

Een aantal punten om op te letten zijn:

- Stuur het sleutelbestand niet mee met de data als je deze deelt.
- Zorg dat het sleutelbestand niet afhankelijk is van de kennis van één persoon.'
- Wanneer het bestand is versleuteld, bewaar dan het wachtwoord goed: geen wachtwoord is geen data.
<br><br>

:::{figure-md} security-fig
<img src="../figures/xkcd_security.png" alt="xkcd">

xkcd.com over data security
:::

## Tokenizen

::::::{margin}
:::{note}
Bij grootschalig onderzoek wordt het pseudonimiseren en sleutelbeheer soms uitbesteed aan een
Trusted Third Party. Bij kleinschalig onderzoek komt dit echter vrijwel nooit voor.
:::
::::::

Het pseudonimiseren van data kan redelijk eenvoudig zijn tot erg moeilijk afhankelijk van de context van het onderzoek.
Zo is het opslaan van een e-mail adres en het koppelen daarvan aan een identifier vrij gemakkelijk. Het meest toegankelijke
voorbeeld is door gebruik te maken van een counter (PP01, PP02, PP03, etc.). Dit zou men in een
spreadsheet kunnen opslaan met bijvoorbeeld een willekeurig getal van www.random.org. Met de random module van de
programmeertaal die jouw voorkeur heeft. Of in een spreadsheet programma.

Het is ook mogelijk om data te tokenizen door een hash algoritme te gebruiken met een pepper. Het voordeel hiervan is 
dat men op die manier automatisch nieuwe data van dezelfde persoon kan pseudonimiseren met hetzelfde pseudoniem. Men
kan ook een pepper en een salt gebruiken voor extra beveiliging. De implementatie hiervan is echter lastig en brengt
daardoor risico's met zich mee.

In kwalitatief onderzoek kan men namen vervangen door vierkante haakjes te gebruiken met een omschrijving: 
`[persoon/buurman/moeder/docent]`. Of men kan bijvoorbeeld de text annoteren met XML-tags. Het wordt echter lastiger
als, bijvoorbeeld, een naam ook context geeft doordat het iets zegt over de culturele achtergrond van een persoon en
dit relevant kan zijn voor het onderzoek. Hierbij moet men wel weer oppassen voor eventuele vooroordelen die in de data
terecht zouden kunnen komen. In zo'n geval is er dus een uitgebreide aanpak nodig om de data te pseudonimiseren die men 
dus goed moet documenteren.

## Tot slot

Zorg dat je het bestand goed bewaard en dat een collega ook toegang heeft tot het bestand. Zo voorkom je eventuele
problemen. 

[^LCRDM]: Omgang met pseudonimisering en sleutelbestanden bij kleinschalig onderzoek. 2019. DOI: 10.581/zenodo.3571046. https://www.lcrdm.nl/files/lcrdm/2019-12/LCRDM%20Pseudonimisering%20en%20sleutelbestanden_NL_online.pdf 