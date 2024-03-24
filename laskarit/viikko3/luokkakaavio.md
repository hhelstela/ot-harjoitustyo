```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Ruututoiminto "*" -- "1" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Ruutu "1" -- "6" SattumaJaYhteismaa
    Kortti "*" -- "1" SattumaJaYhteismaa
    Korttitoiminto "1" -- "1" Kortti
    Ruutu "1" -- "6" AsematJaLaitokset
    Ruutu "1" -- "22" Kadut
    Talot "0..4" -- "1" Kadut
    Hotellit "1" -- "1" Kadut
    Kadut "1" -- "1" Pelaaja
    Raha "*" -- "2..8" Pelaaja
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
```