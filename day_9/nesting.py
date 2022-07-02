# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijion"],
    "Germany": ["Berlin", "Hamburg", "Strttgart"],   
}

# Nesting a dictionary in a dictionary
travel_log["France"] = {"cities_visited": ["Paris", "Lille", "Dijion"], "total_visits": 12}
travel_log["Germany"] = {"cities_visited": ["Berlin", "Hamburg", "Strttgart"],"total_visits": 5} 


# Nesting dictionaries in list
travel_log = [{"country": "France",
               "cities_visited": ["Paris", "Lille", "Dijion"], 
               "total_visits": 12
               }, 
              {"country": "Germany", 
               "cities_visited":["Berlin", "Hamburg", "Strttgart"],
               "total_visits": 5}
            ]
print(travel_log)