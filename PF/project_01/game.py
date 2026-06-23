import random

while True:
    computer = random.choice([0, 1, 2])
    print("""Enter
    ==============
    | s for snake |
    | w for water |
    | g for gun   |
    | e to exit   |
    ==============
    """)
    you = input("Enter your choice : ").lower()

    if you == 'e':
        print("Game exited.")
        print("==========================================")
        break

    gamedic = {'s': 0, 'w': 1, 'g': 2}
    reverseDic = {0: "Snake", 1: "Water", 2: "Gun"}

    if you not in gamedic:
        print("Invalid input! Try again.\n")
        continue

    you_val = gamedic[you]

    print("-----------------------------------------------------------------------------")
    print(f"You chose     : {reverseDic[you_val]}")
    print(f"Computer chose: {reverseDic[computer]}")
    print("-----------------------------------------------------------------------------")

    # Game logic
    if you_val == computer:
        print("Result: It's a draw!\n")
    elif (you_val == 0 and computer == 1) or \
         (you_val == 1 and computer == 2) or \
         (you_val == 2 and computer == 0):
        print("                         Result: You win!\n")
        print("=====================================================================================")
    else:
        print("                         Result: Computer wins!\n")
        print("======================================================================================")


# import tkinter as tk
# import random

# # Game logic
# def play(choice):
#     choices = {"Snake": 0, "Water": 1, "Gun": 2}
#     reverse = {0: "Snake", 1: "Water", 2: "Gun"}
    
#     user = choices[choice]
#     computer = random.randint(0, 2)

#     result_text = f"You chose: {choice}\nComputer chose: {reverse[computer]}\n\n"

#     if user == computer:
#         result_text += "Result: It's a draw!"
#     elif (user == 0 and computer == 1) or \
#          (user == 1 and computer == 2) or \
#          (user == 2 and computer == 0):
#         result_text += "Result: You win!"
#     else:
#         result_text += "Result: Computer wins!"

#     result_label.config(text=result_text)

# # GUI Setup
# window = tk.Tk()
# window.title("Snake-Water-Gun Game")
# window.geometry("400x300")
# window.configure(bg="black")

# title = tk.Label(window, text="Snake 🐍  Water 💧  Gun 🔫", font=("Arial", 18, "bold"), bg="black", fg="white")
# title.pack(pady=10)

# frame = tk.Frame(window, bg="black")
# frame.pack(pady=10)

# btn_snake = tk.Button(frame, text="Snake", font=("Arial", 14), width=10, bg="brown", fg="white", command=lambda: play("Snake"))
# btn_snake.grid(row=0, column=0, padx=10)

# btn_water = tk.Button(frame, text="Water", font=("Arial", 14), width=10, bg="blue", fg="white", command=lambda: play("Water"))
# btn_water.grid(row=0, column=1, padx=10)

# btn_gun = tk.Button(frame, text="Gun", font=("Arial", 14), width=10, bg="gray", fg="white", command=lambda: play("Gun"))
# btn_gun.grid(row=0, column=2, padx=10)

# result_label = tk.Label(window, text="", font=("Arial", 12), bg="black", fg="white", justify="center")
# result_label.pack(pady=20)

# exit_btn = tk.Button(window, text="Exit", font=("Arial", 12), bg="red", fg="white", command=window.destroy)
# exit_btn.pack()

# window.mainloop()

