import requests
from tabulate import tabulate

# Słownik dostępnych walut:
# Dictionary of available currencies:
AVAILABLE_CURRENCIES = {
    "USD": "Dolar amerykański", # US Dollar
    "EUR": "Euro", # Euro
    "GBP": "Funt szterling", # Pound sterling
    "CHF": "Frank szwajcarski", # Swiss franc
    "NOK": "Korona norweska", # Norwegian krone
    "DKK": "Korona duńska", # Danish krone
    "CAD": "Dolar kanadyjski", # Canadian dollar
    "SEK": "Korona szwedzka" # Swedish krona
}
# Funkcja pobiera aktualne kursy wszystkich walut
# Function fetches the current exchange rates for all currencies
def fetch_rates(currencies):
    try:
        # Tworzymy ciąg znaków z kodami walut
        # Create a string of currency codes
        symbols = ",".join(currencies.keys())

        # Wysyłamy zapytanie do API
        # Send a request to the API
        response = requests.get(f"https://api.frankfurter.app/latest?base=PLN&symbols={symbols}")

        # Sprawdzamy, czy odpowiedź API nie zawiera błędu
        # Check if the API response contains an error
        response.raise_for_status()

        # Konwertujemy odpowiedź JSON na słownik
        # Convert the JSON response to a dictionary
        data = response.json()

        # Zwracamy kursy walut oraz datę
        # Return the exchange rates and the date
        return data["rates"], data.get("date", "N/A")

    except requests.RequestException:
        # Wyświetlamy komunikat w przypadku błędu API
        # Display a message in case of an API error
        print("Błąd: nie udało się połączyć z API.")
        return None, None

# Główna pętla programu
# Main program loop
while True:
    try:
        print("\n" + "="*50)

        # Pobieramy od użytkownika kwotę w PLN
        # Get the amount in PLN from the user
        amount_pln = float(input("Podaj kwotę w PLN: "))

        # Sprawdzamy, czy liczba nie jest ujemna
        # Check if the number is not negative
        if amount_pln < 0:
            print("Błąd: kwota nie może być ujemna!")
            continue

    except ValueError:
        # Obsługa sytuacji, gdy użytkownik wpisze tekst zamiast liczby
        # Handle the case where the user enters text instead of a number
        print("Błąd: wpisz poprawną liczbę!")
        continue
    
    # Pobieramy kursy z API
    # Fetch rates from the API
    rates, rate_date = fetch_rates(AVAILABLE_CURRENCIES)
    
    if rates:
        # Informujemy użytkownika o konwersji
        # Inform the user about the conversion
        print(f"\nPrzeliczenie {amount_pln} PLN na wszystkie waluty:")
        print(f"Data kursu: {rate_date}")
        
        # Lista wierszy danych, które później wyświetlimy w tabeli
        # List of data rows that will be displayed in the table later
        table_data = []

        # Iterujemy przez wszystkie waluty zapisane w słowniku
        # Iterate through all currencies stored in the dictionary
        for code, name in AVAILABLE_CURRENCIES.items():

            # Pobieramy kurs dla konkretnej waluty
            # Get the rate for the specific currency
            rate = rates.get(code)

            # Jeśli API zwróciło kurs
            # If the API returned a rate
            if rate:
                # Przeliczamy wynik PLN * kurs waluty
                # Calculate the result PLN * currency rate
                result = amount_pln * rate

                # Dodajemy wiersz do tabeli:
                # Add a row to the table:
                table_data.append([code, name, f"{result:.2f}", f"{rate:.4f}"])
        
        # Wyświetlamy tabelę z użyciem 'tabulate'
        # Display the table using 'tabulate'
        print(tabulate(table_data, headers=["Kod", "Waluta", "Kwota", "Kurs"], tablefmt="grid"))

    else:
        # Jeśli API nie zwróciło kursu
        # If the API did not return rates
        print("Błąd: nie udało się pobrać kursów.")
    
    # Pytanie, czy użytkownik chce wykonać kolejną konwersję
    # Question whether the user wants to perform another conversion
    while True:
        continue_choice = input("\nChcesz przeliczyć kolejną kwotę? (tak/nie): ").strip().lower()

        if continue_choice == "tak":
            break

        elif continue_choice == "nie":
            print("Do widzenia!")
            exit(0)

        else:
            print("Niepoprawny wybór - spróbuj ponownie (wpisz 'tak' lub 'nie').")
