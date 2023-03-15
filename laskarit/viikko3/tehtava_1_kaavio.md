# Monopoli luokkakaavio

## Tehtävä 1 & 2
 
```mermaid
  classDiagram
    class Monopoli {
    }
    
    class Pelaaja {
    +Pelinappula pawn
    +int money_balance
    }
    
    class PeliNappula {
      +Ruutu location
    }
    
    class PeliLauta {
    }
    
    class Ruutu {
      +Ruutu next_square
    }
    
    class Noppa {
    }
    
    class AloitusRuutu {
    }
    
    class Vankila {
    }
    
    class SattumaJaYhteismaa {
    }
    
    class AsematJaLaitokset {
    }
    
    class NormaaliKatu {
      +String street_name
    }  
    
    Pelinappula ..> Ruutu
    Pelaaja "2..8" --> "1" Monopoli
    Pelilauta "1" --> "1" Monopoli
    Ruutu "40" --> "1" Pelilauta
    Pelinappula "1" --> "1" Pelaaja
    Noppa "2" --> "1" Monopoli
```
