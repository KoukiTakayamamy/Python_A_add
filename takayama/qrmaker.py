import qrcode
import os
import sys

args = sys.argv


file_name = args[1]
path = "../../../files"

with open (file_name, encoding="utf-8") as file:
    i = 1
    for line in file:
#qrコード作成
        img = qrcode.make(f)
#画像保存
        img.save(os.path.join(path, str(i)+".png"))
        i += 1
