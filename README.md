# RailNL

## Doel
De opdracht van dit project is om een heuristiek binnen python te creëren die een voeringssysteem voor intercitytreinen genereert met als doel de algehele kwaliteit van de lijnvoering te optimaliseren. Dit kan worden gedaan door de doelfunctie die in de oefening wordt gegeven, te maximaliseren. De doelfunctie kan als volgt worden omschreven: K = p * 10000 - (T * 100 + Min), waarbij K de kwaliteit is van het treinvoeringsysteem, p een fractie is van het aantal gebruikte verbindingen, T het aantal gebruikte paden en Min is de totale tijd in minuten van alle gebruikte paden. Er zijn twee voorwaarden waaraan moet worden voldaan bij het maken van een treinlijnsysteem. De eerste is dat een traject een maximale tijdslengte heeft en de tweede voorwaarde is dat een treinlijnsysteem een maximaal aantal paden heeft.

## Vereisten
Om deze code te gebruiken zijn er voorafgaand packages nodig om deze code werkend te krijgen. Deze zijn te installeren via de command:
<pre> pip install -r requirements.txt </pre>

## Hoe te werk?
Gebruik de volgende instructie om de code uit te voeren: <pre> python main.py </pre>Het programma zal u eerst vragen welk deel van Nederland u wilt gebruiken. Het programma zal u dan vragen welk algoritme u wilt gebruiken. Er zijn vier opties: Random, Greedy, Greedy Lookahead en Hill Climber. Elk algoritme produceert een afbeelding van de gekozen paden en de score

<img src = "https://github.com/MadmanDaniel/RailNL/blob/main/doc/command.png">

## Extensies
- networkx
- matplotlib
- random
- csv
- pandas

## Structuur 

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: Alle code voor dit project
  - **/code/algorithm**: De code voor de algoritmes 
  - **/code/classes**: De classes voor deze case
  - **/code/visualisation**: De code voor de visualisaties
- **/data**: De databestanden die nodig zijn om de graaf te vullen en te visualiseren

## Auteurs
Team naam: **Team Rocket**
* Daniel Djuly
* Hatim Hashi
* Elvin Li
