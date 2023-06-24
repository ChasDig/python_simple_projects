import json

import requests

URL = "https://api.github.com/users/ChasDig/repos"


def write_response_json_in_file(response_json, number):
    with open(f"response_{number}.json", "w") as file:
        json.dump(response_json, file, indent=4)


def get_data_from_github_page():
    page = 1
    while True:
        url = f"https://api.github.com/users/ChasDig/repos?page={page}&per_page=2"
        response_page = requests.get(url=url)
        write_response_json_in_file(response_json=response_page.json(), number=page)
        page += 1
        next_link_url = response_page.links.get("next", None)
        if next_link_url is None:
            print("Finished!")
            break
        print(res)


def get_data_from_github(url):
    response_github = requests.get(url=url)
    write_response_json_in_file(response_json=response_github.json(), number=0)


if __name__ == "__main__":
    # get_data_from_github(url=URL)
    get_data_from_github_page()
