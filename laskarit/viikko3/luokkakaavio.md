## Monopoli

```mermaid
classDiagram
      Pelaaja -- Pelaajat
      Pelaaja -- Nopat
      Pelaaja -- Pelilauta
      Pelilauta -- Ruutu
      Ruutu -- Kortti
      Ruutu -- Pelaaja
      Pelaaja -- Kortti
      Ruutu -- Toiminto
      Pelaaja -- Kadut
      Ruutu -- Kadut
      class Pelaajat{
        lista pelaajista(2-8)
      }
      class Pelaaja{
        raha
        omistukset
      }
      class Nopat{
        lista nopista
      }
      class Pelilauta{
        lista ruuduista
      }
      class Ruutu{
        Aloitusruutu
        Vankila
        Sattuma ja yhteismaa
        Asemat ja laitokset
        Normaalit kadut
      }
      class Toiminto{
        toiminnot
      }
      class Kortti{
        toiminnot
      }
      class Kadut{
        nimi
        omistaja
        talot/hotellit
      }
```
