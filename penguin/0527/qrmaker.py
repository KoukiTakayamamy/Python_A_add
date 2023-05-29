import sys
import os
import qrcode

def generate_qr_codes(file_path):
    # ファイルの存在チェック
    if not os.path.exists(file_path):
        print(f"指定されたパスのファイルが存在しません: {file_path}")
        return

    # ファイルの読み込み
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # QRコードの生成と保存
    for i, line in enumerate(lines, 1):
        url = line.strip()  # 改行文字を除去
        if url:
            qr = qrcode.QRCode()
            qr.add_data(url)
            qr.make()
            img = qr.make_image()
            file_name = f"{i}.png"  # 連番を付与
            img.save(file_name)

    print("QRコードが作成されました。")

if __name__ == "__main__":
    file_path = "qrlist.txt"
    generate_qr_codes(file_path)
