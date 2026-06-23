import time

lyrics = """
Jisko jo bhi milta ha
besabab ni milta 
mujhse bole man mera
sabko sab ni milta
"""

lines = lyrics.strip().split("\n")

for line in lines:
    for word in line.split():
        print(word, end=" ", flush=True)
        time.sleep(0.5)
    print()
    time.sleep(0.5)
