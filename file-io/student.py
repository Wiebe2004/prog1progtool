def count_lines_in_file(path):
    """
    Telt het aantal lijnen in een bestand.

    Parameters:
    - path (str): Het pad naar het bestand.

    Returns:
    - int: Het aantal lijnen in het bestand.
    """
    aantal = 0  # Initialiseren van de teller voor het aantal lijnen
    with open(path, encoding="utf-8") as file:
        while file.readline():  # Lees elke lijn in het bestand
            aantal += 1  # Tel elke gelezen lijn op
    return aantal  # Geef het totale aantal lijnen terug


def remove_empty_lines(source, destination):
    """
    Verwijdert lege lijnen uit een bronbestand en schrijft het resultaat naar een doelbestand.

    Parameters:
    - source (str): Het pad naar het bronbestand.
    - destination (str): Het pad naar het doelbestand.
    """
    with open(source) as in_file:
        with open(destination, "w", encoding="utf-8") as out_file:
            for line in in_file:  # Loop door elke lijn in het bronbestand
                if line != "\n":  # Controleer of de lijn niet leeg is
                    out_file.write(
                        line
                    )  # Schrijf niet-lege lijnen naar het doelbestand


def remove_duplicate_lines(source, destination):
    """
    Verwijdert opeenvolgende duplicaatlijnen uit een bronbestand en schrijft het resultaat naar een doelbestand.

    Parameters:
    - source (str): Het pad naar het bronbestand.
    - destination (str): Het pad naar het doelbestand.
    """
    with open(source) as in_file:
        with open(destination, "w", encoding="utf-8") as out_file:
            last_line = None  # Initialiseren van de variabele voor de vorige lijn
            for line in in_file:  # Loop door elke lijn in het bronbestand
                if (
                    line != last_line
                ):  # Controleer of de huidige lijn verschilt van de vorige lijn
                    out_file.write(
                        line
                    )  # Schrijf niet-duplicaatlijnen naar het doelbestand
                    last_line = line  # Update de vorige lijn voor de volgende iteratie
