# Voorbereiding & casus
RDM module 5 gaat over project- en dataorganisatie. Maar hoe organiseer jij eigenlijk je data? Het is een thema waarmee 
je waarschijnlijk bewust of onbewust wel mee bezig bent. In deze opdracht willen we je uitdagen om de organisatie van 
een eigen onderzoeksproject expliciet te maken. Je doet dit voor jezelf en hoeft het resultaat niet te delen.

## Stap 1 kies: 
Kies het onderzoeksproject dat je wilt beschrijven. Geen eigen onderzoeksproject? Gebruik dan [dit](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/wheelchair_sprints3.zip)
voorbeeld.

## Stap 2 beschrijf:
Documenteer de organisatie van het onderzoeksproject. Hiervoor zijn twee opties, kies degene die het meest bij jou past:

### Optie 1 (low-tech optie):
Navigeer met je file explorer (bijv. Verkenner) naar de projectmap van jouw onderzoek en bekijk de inhoud. Beschrijf 
(globaal, ~5 minuten) voor jezelf de organisatiestrategie, maak eventueel één of meerdere screenshot(s),
en beantwoord de richtvragen uit Stap 3.

### Optie 2 (enige technische voorkennis vereist):
::::::{margin}
:::{tip}
Als er te veel bestanden zijn kan je ook `/f` weglaten op Windows of `-d` toevoegen op Mac/Linux. Tree op Linux heeft 
nog extra opties (zie --help).
:::
::::::

```{tabbed} Windows
- Stap 2.1: Ga naar de hoofdmap van het project in Verkenner (File Explorer)
- Stap 2.2: Klik op de adresbalk van Verkenner, maak deze leeg, en typ `cmd`, druk op enter
- Stap 2.3: Typ `tree /f`, druk op enter, en maak een screenshot van het resultaat of typ `tree /f /a > tree.txt` om het op 
te slaan in een .txt bestand, typ `exit`, enter
- Stap 2.4: Open het bestand in een tekstverwerker (bijv. Kladblok)
```

```{tabbed} MacOS
- Stap 2.1: Open een [terminal](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac), 
installeer [Homebrew](https://brew.sh/), en installeer tree met `brew install tree`
- Stap 2.2: Navigeer naar de hoofdmap van het project met `cd /pad/naar/map`
- Stap 2.3: Typ `tree > tree.txt`, druk op enter, om het resultaat op te slaan in een .txt bestand
- Stap 2.4: Open het bestand in een tekstverwerker (bijv. TextEdit)
```

```{tabbed} Linux
- Stap 2.1: Run `tree --help`, installeer tree met je package manager als deze ontbreekt
- Stap 2.2: Navigeer naar de hoofdmap van het project met `cd /pad/naar/map`
- Stap 2.3: Run `tree > tree.txt` om het resultaat op te slaan in een .txt bestand
- Stap 2.4: Open het bestand in een tekstverwerker (bijv. Gedit of Kate)
```

## Stap 3 contempleer:
Beantwoord de volgende vragen (~10 minuten):
- Kan je een collega snel uitleggen waar een bepaald document staat?
- Als iemand begint in dit project, kan die persoon dan snel aan de slag?
- Is het project organisch ontstaan of is het op basis van een bepaalde standaard? Welke?
- Is alles aanwezig om je analyse te kunnen reproduceren?
- Zijn de map- en bestandsnamen consistent? Kan je (alfabetisch) sorteren?
- Welke strategie gebruik je voor versienummering?
- Zijn er dingen die je -in retrospect- anders zou doen?

<br>

---

<br>

(casus)=
# Introductie casus <i class="fab fa-accessible-icon"></i>

In de volgende opdrachten gaan we aan de slag met een dataset afkomstig van mijn collega Nick de Vlerk. Hij staat er om
bekend dat hij vaak rommelig omgaat met zijn onderzoeksprojecten waardoor het moeilijk is om alles terug te vinden. In
de komende drie opdrachten gaan we aan de slag met de data en zorgen we dat het project weer overzichtelijk is en dat 
de data netjes en veilig is opgeslagen.

Het betreft een eenvoudige interventie studie naar het effect van een krachttrainingsprotocol op de rolstoelsprint 
prestaties. Deelnemers worden één keer voor de training gemeten (T1/pre) en één keer na de training (T2/post). Voor 
het gemak laten we even de data van de controlegroep buiten beschouwing. Bij een meting doet een proefpersoon een 
100m sprint in een sportrolstoel. De tijd, geregistreerd met een stopwatch, wordt gebruikt als uitkomst van de meting 
(lager is beter). Verder wordt het gewicht van de proefpersoon en de sekse geregistreerd. De voornaam van de proefpersoon
en het e-mail adres werden geregistreerd om contact op te nemen voor de retentiemeting (T3).

De data voor de eerste opdracht kan [hier](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/wheelchair_sprints0.zip) 
vandaan worden gedownload (.zip). Het figuur hieronder geeft een korte indruk van de data die is verzameld:

:::{figure-md} sprint-fig
<img src="../figures/xkcd_plot.svg" alt="wheelchair-sprints">

Rolstoel sprint (100m) data tijdens de voor- en nameting (n=20).
:::
