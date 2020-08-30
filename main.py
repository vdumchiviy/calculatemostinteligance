import requests
TOKEN = "2619421814940190"


def get_intelligence_by_name(name_of_hero):
    result = -100000
    print(f"Request intelligance for {name_of_hero}")
    url = "https://www.superheroapi.com/api.php/" + TOKEN + "/search/" + name_of_hero
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error {response.status_code} during request {name_of_hero}")
        return
    data = response.json()

    result = int(data["results"][0]["powerstats"]["intelligence"])
    print(f"--{name_of_hero} has result {result}")
    return result


def main():

    Thanos = get_intelligence_by_name("Thanos")
    Hulk = get_intelligence_by_name("Hulk")
    CaptainAmerica = get_intelligence_by_name("Captain America")

    if Hulk <= Thanos >= CaptainAmerica:
        print(f"The most intelligance is Thanos with level {Thanos}")
    elif Thanos <= Hulk >= CaptainAmerica:
        print(f"The most intelligance is Hulk with leve {Hulk}")
    else:
        print(
            f"The most intelligance is Captain America with leve {CaptainAmerica}")


main()
