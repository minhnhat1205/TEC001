import requests


def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])  # print only the joke text
    else:
        print("Failed to fetch joke.")


# Run the function
get_chuck_norris_joke()