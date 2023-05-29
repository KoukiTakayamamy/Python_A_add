#モジュール「os」のimport
import os
import qrcode
#os.path.joinを利用して相対パスを生成する

with open("files/url.txt",mode="r",encoding="utf-8") as url_txt:
    file_number = 1 
    # 一行ずつ読み込む
    for line in url_txt:
        #相対パス（"../files/xxxxxx.png"）となる
        img = qrcode.make(line)
        #png ファイルの生成
        path = os.path.join("output", str(file_number) +".png")
        img.save(path)
        file_number += 1