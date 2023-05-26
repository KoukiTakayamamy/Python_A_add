import sys

distance = int(sys.argv[1])

fare = 0

if distance <= 1500:
    fare = 630
    print(fare, end="")

if distance > 1500:
    fare = 728 + ((distance - 1500) // 344) * 98
    print(fare, end="")