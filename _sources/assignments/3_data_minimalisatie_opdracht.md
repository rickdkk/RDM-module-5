# Opdracht 3: Data minimalisatie 

## Voorbereiding

- Lees voor het maken van de opdracht het tweede hoofdstuk: [](../chapters/3_data_minimalisatie.md).
- Maak de eerste opdracht: [](2_data_organisatie_opdracht.md)
- Optioneel: Tweede opdracht niet helemaal afgekregen? Dan kan je ook verder met [deze](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/wheelchair_sprints2.zip) files.

## Opdracht <i class="fab fa-accessible-icon"></i>

In de data zitten nog veel directe en indirecte persoonsgegevens. Een deel hiervan is nodig om contact op te nemen voor
de retentiemeting, maar lang niet alles is nodig. Daarbij staan de gegevens *en plein public* naast de andere data.

1. Identificeer de kolommen die nodig zijn voor het onderzoek.
1. Verwijder de kolommen die niet nodig zijn uit de data.
1. Maak een nieuwe file (`sleutel.ods` o.i.d.) en zet daar de `ID` kolom in samen met de gevoelige informatie.
    - Kan je de data nog linken aan de persoon door de files te combineren?
    - Is de data file schoon van persoonsgegevens?
1. Versleutel de sleutel met VeraCrypt.
    - Optioneel: als er weinig tijd is kan je ook van [dit](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/container) 
      volume gebruik maken (wachtwoord: password123).
1. Sluit VeraCrypt en verplaats het versleutelde volume buiten de projectfolder.
    - Kan iemand zonder het wachtwoord nog bij de persoonsgegevens?
    - Is de data nu anoniem?
   
Een oplossing voor de opdrachten staat [hier](https://gitlab.com/Rickdkk/messy-example-project/-/raw/main/wheelchair_sprints3.zip).
Het wachtwoord op de container is password123. 
Let wel op: in dit voorbeeld staat de sleutel ook in de projectmap, deze mag daar niet blijven. Het wachtwoord is natuurlijk
ook uitzonderlijk slecht.

## #TODO

Het project is nu in een acceptabele vorm. Er zijn echter nog een paar dingen die niet behandeld zijn, maar wel een 
eervolle vermelding verdienen:
- [Version control](https://swcarpentry.github.io/git-novice/)
- [Automatiseren](https://the-turing-way.netlify.app/reproducible-research/make.html)
- [Scripting](https://guide.esciencecenter.nl/#/best_practices/language_guides/languages_overview) + 
  [code quality](https://the-turing-way.netlify.app/reproducible-research/code-quality.html) + 
  [code testing](https://the-turing-way.netlify.app/reproducible-research/testing.html)  
- [Documentatie](https://ddialliance.org/training/getting-started-new-content/create-a-codebook)
- Publiceren op [GitHub + Zenodo](https://guides.github.com/activities/citable-code/)
- •••
