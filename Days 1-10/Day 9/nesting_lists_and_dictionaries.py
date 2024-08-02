# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_logs = {
    "France": { "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
}

# if "France" in travel_logs:
#     for city in travel_logs["France"]["cities_visited"]:
#         print(city)
#     print(travel_logs["France"]["total_visits"])

# Nesting a dictionary in a list
new_logs = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
]

for country in new_logs:
    for city in country["cities_visited"]:
        print(city)
