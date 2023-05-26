# 파이썬의 namelist를 조작해, 인덱스가 기수인 요소만을 출력
namelist = ["Kurita", "Tanaka", "Kaneda", 
            "Noda", "Koyama", "Adachi", 
            "Kuriyama", "Ohyama", "Kishida"]
    
resultlist = []

# 1부터 리스트 길이 중에서 2씩 뛰어넘어 출력 (1,3,5,7)
for i in range(1, len(namelist), 2):
    resultlist.append(namelist[i])

print(resultlist, end="")