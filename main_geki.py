import hashlib
import os
import time
import traceback

import requests

req_url = "https://ongeki.sega.jp/assets/json/music/music.json"
img_baseurl = "https://ongeki-net.com/ongeki-mobile/img/music/"

jacketpath = "./"

data = requests.get(req_url).json()

choiced = []
for music in data:
    if music["lev_mas"] != "" or music["lev_lnt"] != "":
        choiced.append(music)

os.makedirs(jacketpath + "jackets_geki", exist_ok=True)

for music in choiced:
    try:
        url = img_baseurl + music["image_url"]
        title = music["title"]
        artist = music["artist"]
        rawfilename = title + artist
        filepath = jacketpath + "jackets_geki/" + f"{hashlib.md5(rawfilename.encode('utf-8')).hexdigest()}.png"
        if not os.path.isfile(filepath):
            print(f"「{title}」を{url}からダウンロードしています")
            imageblob = requests.get(url)
            if imageblob.status_code == 200:
                with open(filepath, "wb") as i:
                    i.write(imageblob.content)
            time.sleep(1)
        else:
            print(f"「{title}」は既に存在しています")
    except:
        traceback.print_exc()
        time.sleep(1)
