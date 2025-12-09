## 🇵🇱 Wersja polska
# Python Currency CLI

---

Prosta aplikacja konsolowa w Pythonie do przeliczania PLN na najpopularniejsze waluty (USD, EUR, GBP, CHF, NOK, DKK, CAD, SEK). Pobiera aktualne kursy z API Frankfurter i wyświetla wyniki w czytelnej tabeli. Łatwa w użyciu, interaktywna i idealna do szybkich konwersji walut.

## Funkcje

- 💱 Przeliczanie PLN na wiele walut jednocześnie
- ⏱️ Aktualne kursy walut w czasie rzeczywistym dzięki API Frankfurter
- 🖥️ Interaktywny interfejs konsolowy
- ⚠️ Walidacja danych wejściowych (liczby ujemne, niepoprawne wartości)
- 📊 Wyświetlanie wyników w sformatowanej tabeli z użyciem `tabulate`

## Instalacja

Sklonuj repozytorium:

```bash
git clone https://github.com/<twoje-konto>/python-currency-cli.git
cd python-currency-cli
```

Zainstaluj zależności:

```bash
pip install requests tabulate
```

## Uruchomienie

Uruchom główny skrypt:

```bash
python main.py
```

Po wyświetleniu komunikatu:

- Wpisz kwotę w PLN (np. `100`, `250`)
- Lub wpisz `nie` po konwersji, aby zakończyć program.

## Przykładowy wynik

```yaml
Podaj kwotę w PLN: 100
============================================
Przeliczenie 100 PLN na wszystkie waluty:
Data kursu: 2025-12-09
+------+----------------+--------+---------+
| Kod  | Waluta         | Kwota  | Kurs    |
+------+----------------+--------+---------+
| USD  | Dolar ameryk.  | 25.34  | 0.2534  |
| EUR  | Euro           | 22.78  | 0.2278  |
| ...  | ...            | ...    | ...     |
+------+----------------+--------+---------+
```

## Licencja

Projekt udostępniony na licencji MIT.
Szczegóły w pliku `LICENSE`.

## Podziękowania za API

Kursy walut: [Frankfurter API](https://frankfurter.dev/)

# Autor

* Stworzone przez Greg — PotegaIT
* YouTube: [@PotegaIT](https://www.youtube.com/@PotegaIT)

---


## 🇬🇧 English version
# Python Currency CLI

---

A simple Python CLI app to convert PLN to major currencies (USD, EUR, GBP, CHF, NOK, DKK, CAD, SEK). Fetches real-time rates from Frankfurter API and displays results in a clear table. Easy to use, interactive, and perfect for quick currency conversions.

## Features

- 💱 Convert PLN to multiple currencies at once
- ⏱️ Real-time exchange rates via Frankfurter API
- 🖥️ Interactive console interface
- ⚠️ Input validation for negative numbers and non-numeric entries
- 📊 Display results in a formatted table using `tabulate`

## Installation

Clone the repository:

```bash
git clone https://github.com/<twoje-konto>/python-currency-cli.git
cd python-currency-cli
```

Install dependencies:

```bash
pip install requests tabulate
```

## Usage

Run the main script:

```bash
python main.py
```

When prompted:

- Enter the amount in PLN (e.g., `100`, `250`)
- Or type `nie` after a conversion to close the program.


## Example Output

```yaml
Podaj kwotę w PLN: 100
============================================
Przeliczenie 100 PLN na wszystkie waluty:
Data kursu: 2025-12-09
+------+----------------+--------+---------+
| Kod  | Waluta         | Kwota  | Kurs    |
+------+----------------+--------+---------+
| USD  | Dolar ameryk.  | 25.34  | 0.2534  |
| EUR  | Euro           | 22.78  | 0.2278  |
| ...  | ...            | ...    | ...     |
+------+----------------+--------+---------+
```

## License

This project is licensed under the MIT License.
See the `LICENSE` file for details.

## API Credits

- Currency rates: [Frankfurter API](https://frankfurter.dev/)

## Author

Created by Greg — PotegaIT
YouTube: [@PotegaIT](https://www.youtube.com/@PotegaIT)
