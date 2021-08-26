# Opdracht 2: Data organisatie 

## Voorbereiding

- Lees voor het maken van de opdracht het tweede hoofdstuk: [](../chapters/2_data_organisatie.md).
- Maak de eerste opdracht: [](1_project_organisatie_opdracht.md)
- Optioneel: Eerste opdracht niet helemaal afgekregen? Dan kan je ook verder met [deze](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/wheelchair_sprints1.zip) files.
- Download de extra data voor deze opdracht [hier](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/new_data.zip).
  
## Opdracht <i class="fab fa-accessible-icon"></i>

::::::{margin}
:::{note}
Deze manier van files aanleveren is niet echt optimaal, maar anders was er geen opdracht 🙃.
:::
::::::

De spreadsheet bestanden in de map zijn nieuwe data verzameld door studenten. Hierin hebben ze de gegevens geregistreerd tijdens 
het onderzoek en ze hebben de files gedropped in hun file drop punt in Fontys Research Drive. Deze moeten nog bijgevoegd 
worden bij de rest van de data. Voor de uiteindelijke analyse is het van belang dat de data allemaal in hetzelfde format 
beschikbaar zijn in één file. 

1. Maak een kopie van de spreadsheet file met alle data (`data.ods`).
1. Voeg data validatie toe:
    - Zorg ervoor dat er een vaste lijst waarden is voor `sex`.
    - Beperk de mogelijke waarden voor `weight`, bijv. 40-120kg.
    - Beperk de mogelijke waarden voor `pre` en `post`, bijv. 10-60s.
1. Vul de data in de file met validatie aan met de drie nieuwe samples.
   - Was alle data goed ingevuld door de studenten?
1. Sla de file op en geef het een nieuw versienummer.
    - Staat de data nu in een tidy format?
    - Wat is het verschil met de .csv file `data_long.csv`?
1. Bonus: leg je stappen vast in een CHANGELOG
