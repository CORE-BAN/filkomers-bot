from bs4 import BeautifulSoup
import requests
import os
import json

URL = "https://filkom.ub.ac.id/berita/"

proxies = {
    'http': '104.37.101.73:8181',
    'http': '186.97.182.5:999',
    'http': '188.133.173.21:8080',
    'http': '66.29.156.100:80',
    'http': '122.102.118.82:8080',
    'http': '43.255.113.232:8083',
}


def get_latest_berita() -> bool:
    # TODO: scraping berita https://filkom.ub.ac.id/berita/
    print("berita terkini")


def get_all_berita() -> list:
    # print("[GET] all berita..")
    try:
        response = requests.get(URL, proxies=proxies).text
    except:
        response = requests.get(URL).text

    soup = BeautifulSoup(response, 'html.parser')
    beritas = soup.find_all('div', class_='post')

    beritas_text = [berita.text.strip().replace("\n", " - ")
                    for berita in beritas]

    return beritas_text


if __name__ == '__main__':
    get_all_berita()
