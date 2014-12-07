pyFinder
========

Questo pacchetto vuole essere un piccolo coltellino svizzero per organizzare le sessioni di gioco. 

## Installazione
- Assicuriamoci di aver installato la versione 2.x di Python
- Installiamo pip per risolvere le dipendenze necessarie
- Installiamo git per scaricare l'ultima versione del software
- Cloniamo il pacchetto sulla nostra macchina: git clone https://github.com/flavoi/pyFinder.git
- Installiamo le dipendenze necessarie: cd pyfinder && pip install -r requirements.txt​
​- Il giocattolo è pronto per essere testato :-) 

## Funzionalità incluse

Per invocare lo script desiderato: ```python pyfinder.py <nome_app>```.
- [x] App *dadi*: simula il lancio dei classici dadi da gioco di ruolo, permettendo l'aggiunta di bonus, malus e ripetizioni. 
- [x] App *personaggi*: censisce e riporta le caratteristiche dei giocatori memorizzando i loro progressi.
- [x] App *sfide*: dispensa punti esperienza in maniera equa nel gruppo.
- [x] App *creature*: censisce e riporta le caratteristiche di creature controllate dal game master. 
- [x] App *archetipi*: censisce, gestisce e assegna archetipi ad una creatura.

### Gli attributi di un personaggio

| Generale            |
| ------------------  |
| nome giocatore      |
| nome personaggio    |
| punti esperienza    |


### Gli attributi di una creatura

| Generale | Attacco | Difesa | Speciale | 
| -------- | ------- | ------ | -------- |
| nome | nome | classe armatura | nome |
| tipo | bonus di attacco | punti ferita | descrizione |
| grado sfida | danni | resistenza al danno |
| taglia | 
| allineamento |
| dadi vita |
