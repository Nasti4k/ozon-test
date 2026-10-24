import requests

def get_tallest_hero(gender_input, work_input):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    data = response.json()

    info_hero = []
    candidates = []

    for hero in data:
        appearance = hero["appearance"]
        gender = appearance["gender"]
        hight = appearance["height"][1]
        work = hero["work"]["occupation"]

        bool_work = None
        if work == '-':
            bool_work = False
        else:
            bool_work = True

        info_hero.append((hero["name"], gender, hight, bool_work))

    for hero in info_hero:
        name = hero[0]
        gender = hero[1]
        height_str = hero[2]
        bool_work = hero[3]

        if gender == gender_input and bool_work == work_input:
            if height_str == "-" or height_str == "":
                continue

            if "cm" in height_str:
                height_cm = int(height_str.replace("cm", "").strip())
                candidates.append((name, height_cm))

            elif "meters" in height_str:
                height_m = float(height_str.replace("meters", "").strip())
                candidates.append((name, height_m * 100))

    if len(candidates) == 0:
        return None

    tallest = max(candidates, key=lambda x: x[1])
    return tallest[0]

print(get_tallest_hero("Male", True))
print(get_tallest_hero("Female", False))

