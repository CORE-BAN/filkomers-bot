import json
import os

from scrape.pengumuman_scrape import get_latest_pengumuman
from scrape.berita_scrape import get_latest_berita

from bot.bot_client import send_message

WEBHOOK_DISCORD = os.environ["WEBHOOK_DISCORD"]

def check_pengumuman():

    data = json.loads(open('pengumuman_update.json', 'r').read())
    judul = data['judul']
    link = data['link']
    content = data['text'].strip()

    if "\n\n" in content:
        content = content.replace("\n\n", "\n")

    tanggal = data['tanggal']

    if len(content) > 1500:
        print("[DEBUG] content is too long, cutting it..")
        content = content[:1000] + '... [selengkapnya cek sumber]'

    TEXT = f"[PENGUMUMAN] \n{judul} \nTanggal: {tanggal} \n\n{content} \n\n\nSumber: {link}"

    print("[POST] sending pengumuman..")
    send_message(TEXT, WEBHOOK_DISCORD)
    print("[DEBUG] pengumuman sent.")


def check_berita():
    data = json.loads(open('berita_update.json', 'r').read())
    judul = data['judul']
    tanggal = data['tanggal']
    link = data['link']

    TEXT = f"[BERITA] \n{judul} \nTanggal: {tanggal} \n\nSumber: {link}"

    print("[POST] sending berita..")
    send_message(TEXT, WEBHOOK_DISCORD)
    print("[DEBUG] berita sent.")


if __name__ == "__main__":
    status_pengumuman = get_latest_pengumuman()
    if status_pengumuman:
        check_pengumuman()

    status_berita = get_latest_berita()
    if status_berita:
        check_berita()
