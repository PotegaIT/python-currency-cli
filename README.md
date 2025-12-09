## 🇬🇧 English version
# Python Currency CLI

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
