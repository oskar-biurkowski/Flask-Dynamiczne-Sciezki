# Flask – Dynamiczne ścieżki i parametry

Projekt zawiera realizację zadań z zakresu obsługi dynamicznych tras, konwerterów typów, query string oraz przekierowań we Flasku.

## Lista tras (Endpoints)

| Trasa | Opis | Przykład użycia |
| :--- | :--- | :--- |
| `/czesc/<imie>` | Powitanie użytkownika | `http://localhost:5000/czesc/Jan` |
| `/czesc/<imie>/<int:wiek>` | Powitanie z podaniem wieku | `http://localhost:5000/czesc/Jan/20` |
| `/dodaj/<int:a>/<int:b>` | Dodawanie dwóch liczb | `http://localhost:5000/dodaj/10/5` |
| `/odejmij/<int:a>/<int:b>` | Odejmowanie dwóch liczb | `http://localhost:5000/odejmij/10/5` |
| `/pomnoz/<int:a>/<int:b>` | Mnożenie dwóch liczb | `http://localhost:5000/pomnoz/4/3` |
| `/podziel/<int:a>/<int:b>` | Dzielenie (z obsługą błędu dzielenia przez 0) | `http://localhost:5000/podziel/10/2` |
| `/potega/<int:a>/<int:b>` | Potęgowanie | `http://localhost:5000/potega/2/3` |
| `/tabliczka/<int:n>` | Tabliczka mnożenia dla $n$ z zakresu 1–20 | `http://localhost:5000/tabliczka/5` |
| `/produkty` | Obsługa filtrów `kat` i `sort` via Query String | `http://localhost:5000/produkty?kat=elektronika&sort=cena` |
| `/elementy` | Lista wszystkich elementów z bazy | `http://localhost:5000/elementy` |
| `/element/<int:id>` | Szczegóły elementu (lub 404 w przypadku braku) | `http://localhost:5000/element/1` |
| `/start` | Przekierowanie (302) na stronę główną `/` | `http://localhost:5000/start` |