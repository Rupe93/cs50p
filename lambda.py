# Test run of lambda function: 

animals = [
    {"Genus": "Lion", "Age": 15, "Country": "Africa"},
    {"Genus": "Tiger", "Age": 10, "Country": "Russia"},
    {"Genus": "Puma", "Age": 5, "Country": "North America"}
]

animals.sort(key=lambda Cat:Cat["Age"])
print(animals)