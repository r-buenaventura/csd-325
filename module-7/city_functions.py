# Roxanne Buenaventura
# CSD325
# Assignment 7_2
# 10 July 2026

def get_city_country(city, country, language=None, population=None):
    """Generate a neatly formatted city-country string with language and population."""
    city_country = f"{city}, {country}"
    result = f"{city.title()}, {country.title()}"
    if language:
        result += f", language: {language.title()}"
    if population:
        result += f" - Population: {population}"
    return result


# call the function 3 times
if __name__ == "__main__":
    print(get_city_country("Santiago", "Chile", "Spanish", 5000000))
    print(get_city_country("paris", "France", "French", 2148000))
    print(get_city_country("tokyo", "Japan", "Japanese", 13929286))