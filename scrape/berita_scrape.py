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
    print("[GET] berita..")
    try:
        response = requests.get(URL, proxies=proxies).text
    except:
        response = requests.get(URL).text

    soup = BeautifulSoup(response, 'html.parser')
    beritas = soup.find_all('div', class_='post')
    judul_baru = beritas[0].text.strip().replace("\n", " - ")

    if not os.path.exists('berita_update.json'):
        print("[GET] latest berita..")
        link = beritas[0].find('a')['href']

        data_berita = {
            "judul": judul_baru.split(" - ")[1],
            "tanggal": judul_baru.split(" - ")[0],
            "link": link
        }

        with open('berita_update.json', 'w') as f:
            json.dump(data_berita, f)

        return True

    else:
        with open('berita_update.json', 'r') as f:
            data_berita = json.loads(f.read())
            judul_lama = data_berita['judul']
            f.close()

        if judul_baru.split(" - ")[1] != judul_lama:
            print("[DEBUG] new berita found.")
            link = beritas[0].find('a')['href']

            data_berita = {
                "judul": judul_baru.split(" - ")[1],
                "tanggal": judul_baru.split(" - ")[0],
                "link": link
            }

            with open('berita_update.json', 'w') as f:
                json.dump(data_berita, f)

            return True

        print("[DEBUG] no new berita found.")
        return False


def get_all_berita() -> list:
    print("[GET] all berita..")
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
    get_latest_berita()
