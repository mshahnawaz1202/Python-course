import random
def game():
    print("You are playing a game..")
    you=random.randint(1,50)
    with open("file_handling/practice_set/02_high_score.txt") as f:
        highScore=f.read()
        if(highScore!=""):
            highScore=int(highScore)
        else:
            highScore=0
        print(f"Your score : {you}")
        if(you>highScore):
            with open("file_handling/practice_set/02_high_score.txt","w") as f:
                f.write(str(you))

    return you

score=game()
# print(score)
