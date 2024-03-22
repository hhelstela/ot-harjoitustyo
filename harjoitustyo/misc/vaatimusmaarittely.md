# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus toimia kalenterina, johon kirjataan pääsääntöisesti tapahtumien sijaan tehtäviä, jotka pitäisi sen päivän aikana tehdä. Tehtävät voi luokitella sen mukaan, miten tärkeitä ne ovat. Sovelluksen on tarkoitus auttaa käyttäjää ajanhallinnassa ja aikaansaamisessa.

## Käyttäjät

Sovelluksessa tulee olemaan kaksi käyttäjäroolia: _normaali käyttäjä_ ja _ylläpitäjä_. _Normaali käyttäjä_ pystyy hallinnoimaan omaa kalenteriaan, kun taas _ylläpitäjä_ voi hallinnoida kaikkien käyttäjien kalentereita ja poistaa käyttäjiä.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri näkymästä
Kirjautumisnäkymä
![](./images/login_screen.jpeg)
Päänäkymä
![](./images/main_view.jpeg)
Yksityiskohtien ponnahdusikkuna
![](./images/detail_popup.jpeg)

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirtyä uuden käyttäjän luomisnäkymään tai onnistuneen kirjautumisen yhteydessä kirjaantuneen käyttäjän päänäkymään. Jos haluaa tarkastella yksityiskohtia, aukeaa ponnahdusikkuna, jossa näkyy tehtävän nimi ja yksityiskohdat.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen, johon liittyy myös salasana
    - Käyttäjätunnuksen täytyy olla uniikki
- Käyttäjä voi kirjautua järjestelmään
    - Kirjautuminen onnistuu jos käyttäjätunnus ja salasana ovat kirjattu järjestelmään
    - Kirjautuminen ei onnistu, jos käyttäjätunnusta ei ole rekisteröity


### Kirjautumisen jälkeen

- Käyttäjä näkee oman kalenterinsa ja siihen tallennetut tehtävät
- Käyttäjä voi luoda uuden tehtävän
  - Luotu tehtävä näkyy ainoastaan sen luoneelle käyttäjälle
  - Tehtävä voi jäädä ikkunaan sovelluksessa, jossa on kaikki tehtävät, joita ei ole vielä lisätty millekään päivälle
  - Tehtävän voi siirtää suoraan kalenteriin
- Käyttäjä voi merkitä tehtävän tehdyksi
- Käyttäjä voi luokitella tehtävät tärkeyden mukaan
- Käyttäjä voi merkitä tehtävään lisätietoja
- Käyttäjä voi poistaa tehtävän
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Tehdyksi merkittyjen tehtävien tarkastelu
- Jos tehtävä ei tule tehdyksi päivän aikana, se siirtyy seuraavalle päivälle automaattisesti
- Tehdyksi merkittyjen tehtävien merkkaaminen tekemättömiksi, jolloin ne palautetaan ikkunaan, jossa on sijoittamattomat tehtävät
- Käyttäjä pääsee tarkastelemaan tehtyjä tehtäviä
- Tehtävien tietojen editointi
- Mahdollisuus useampaan erilliseen kalenteriin, samalla käyttäjällä
- Käyttäjätunnuksen poisto