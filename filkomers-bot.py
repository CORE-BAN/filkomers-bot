import json
import os

from scrape.pengumuman_scrape import get_pengumuman
from scrape.berita_scrape import get_berita


def check_pengumuman():
    status = get_pengumuman()
    if status:
        print("[DEBUG] new pengumuman found.")

        data = json.loads(open('pengumuman_update.json', 'r').read())
        judul = data['judul']
        link = data['link']
        content = data['text'].strip()
        tanggal = data['tanggal']
        print("[DEBUG] new pengumuman title: ", judul[:20])

        if len(content) > 3000:
            print("[DEBUG] content is too long, cutting it..")
            content = content[:3000] + '... [selengkapnya cek sumber]'

        TEXT = f" {judul} \nTanggal: {tanggal} \n\n{content} \n\n\nSumber: {link}"

        WEBHOOK_DISCORD = os.environ['WEBHOOK_DISCORD']

        print("[POST] sending ingfo..")
        # TODO: send message to discord
        # send_message(TEXT, WEBHOOK_DISCORD)
        print("[DEBUG] ingfo sent.")
    else:
        print("[DEBUG] no new pengumuman")
        pass


def check_berita():
    pass


if __name__ == "__main__":
    check_pengumuman()
    check_berita()
