major_rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
    "mississippi": "united states",
    "ganges": "india"
}
for river, country in major_rivers.items():
    print(f"{river.title()} runs through {country.title()}")