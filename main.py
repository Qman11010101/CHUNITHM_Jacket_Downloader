import os
import time
import traceback

import requests

req_url = "https://chunithm.sega.jp/storage/json/music.json"
img_baseurl = "https://new.chunithm-net.com/chuni-mobile/html/mobile/img/"

jacketpath = "./"

data = requests.get(req_url).json()

choiced = []
for music in data:
    if music["lev_mas"] != "":
        choiced.append(music)

os.makedirs("jackets", exist_ok=True)

for music in choiced:
    try:
        url = img_baseurl + music["image"]
        title = music["title"]
        table = str.maketrans('\\/:*?"<>|#', "__________", "")
        filepath = jacketpath + "jackets/" + f"{title}.png".translate(table)
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
