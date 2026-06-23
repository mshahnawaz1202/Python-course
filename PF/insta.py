import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

# ------------------ Data Classes ------------------

class User:
    def __init__(self, name, password, city, sec_q, sec_a):
        self.name = name
        self.password = password
        self.city = city
        self.sec_q = sec_q
        self.sec_a = sec_a
        self.posts = []
        self.messages = []
        self.followers = []
        self.following = []

# ------------------ App Class ------------------

class MiniInstagramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Instagram")
        self.root.geometry("800x600")
        self.root.config(bg="#000000")  # Black background

        self.users = {}
        self.current_user = None

        self.build_main_ui()

    def build_main_ui(self):
        self.clear_window()

        tk.Label(self.root, text="📸 Mini Instagram", font=("Helvetica", 26, "bold"),
                 fg="#E1306C", bg="#000000").pack(pady=40)

        self.create_button("Sign Up", "#A0522D", self.signup_ui)
        self.create_button("Login", "#333333", self.login_ui)

    def create_button(self, text, bg_color, command):
        tk.Button(self.root, text=text, font=("Arial", 14),
                  width=20, bg=bg_color, fg="white", command=command).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def signup_ui(self):
        self.clear_window()

        tk.Label(self.root, text="Create Account", font=("Helvetica", 20),
                 bg="#000000", fg="white").pack(pady=20)

        entries = {}
        for field in ["Name", "Password", "City", "Security Question", "Security Answer"]:
            tk.Label(self.root, text=field, bg="#000000", fg="white").pack()
            entry = tk.Entry(self.root, show="*" if field == "Password" else None)
            entry.pack()
            entries[field] = entry

        tk.Button(self.root, text="Register", bg="#A0522D", fg="white", command=lambda: self.register(entries)).pack(pady=10)
        tk.Button(self.root, text="Back", bg="#444", fg="white", command=self.build_main_ui).pack()

    def register(self, entries):
        name = entries["Name"].get()
        if name in self.users:
            messagebox.showerror("Error", "User already exists!")
            return
        self.users[name] = User(
            name,
            entries["Password"].get(),
            entries["City"].get(),
            entries["Security Question"].get(),
            entries["Security Answer"].get()
        )
        messagebox.showinfo("Success", "Account created successfully!")
        self.build_main_ui()

    def login_ui(self):
        self.clear_window()

        tk.Label(self.root, text="Login", font=("Helvetica", 20),
                 bg="#000000", fg="white").pack(pady=20)

        tk.Label(self.root, text="Username", bg="#000000", fg="white").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Password", bg="#000000", fg="white").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        tk.Button(self.root, text="Login", bg="#333333", fg="white",
                  command=lambda: self.login(name_entry, password_entry)).pack(pady=10)
        tk.Button(self.root, text="Back", bg="#444", fg="white", command=self.build_main_ui).pack()

    def login(self, name_entry, password_entry):
        name = name_entry.get()
        password = password_entry.get()
        user = self.users.get(name)
        if user and user.password == password:
            self.current_user = user
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def dashboard(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {self.current_user.name}", font=("Helvetica", 18),
                 bg="#000000", fg="#E1306C").pack(pady=20)

        self.create_button("Create Post", "#A0522D", self.create_post)
        self.create_button("View My Posts", "#444", self.view_posts)
        self.create_button("Send Message", "#663399", self.send_message)
        self.create_button("View Messages", "#800000", self.view_messages)
        self.create_button("Follow User", "#4B0082", self.follow_user)
        self.create_button("Followers & Following", "#8B0000", self.view_followers_following)
        self.create_button("Logout", "#333333", self.logout)

    def create_post(self):
        content = simpledialog.askstring("New Post", "What's on your mind?")
        if content:
            self.current_user.posts.append((content, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            messagebox.showinfo("Posted", "Post created!")

    def view_posts(self):
        self.clear_window()
        tk.Label(self.root, text="Your Posts", font=("Helvetica", 18),
                 bg="#000000", fg="white").pack(pady=10)
        for content, timestamp in self.current_user.posts:
            tk.Label(self.root, text=f"{content}\n🕒 {timestamp}", wraplength=700,
                     bg="#000000", fg="white", justify="left").pack(pady=5)
        tk.Button(self.root, text="Back", bg="#444", fg="white", command=self.dashboard).pack(pady=10)

    def send_message(self):
        recipient = simpledialog.askstring("Send Message", "Enter recipient username:")
        if recipient not in self.users:
            messagebox.showerror("Error", "User not found.")
            return
        msg = simpledialog.askstring("Send Message", "Enter your message:")
        if msg:
            self.users[recipient].messages.append((self.current_user.name, msg))
            messagebox.showinfo("Sent", "Message sent.")

    def view_messages(self):
        self.clear_window()
        tk.Label(self.root, text="Messages", font=("Helvetica", 18),
                 bg="#000000", fg="white").pack(pady=10)
        for sender, msg in self.current_user.messages:
            tk.Label(self.root, text=f"From {sender}: {msg}", wraplength=700,
                     bg="#000000", fg="white", justify="left").pack(pady=5)
        tk.Button(self.root, text="Back", bg="#444", fg="white", command=self.dashboard).pack(pady=10)

    def follow_user(self):
        username = simpledialog.askstring("Follow", "Enter username to follow:")
        if username not in self.users or username == self.current_user.name:
            messagebox.showerror("Error", "Invalid user.")
            return
        if username not in self.current_user.following:
            self.current_user.following.append(username)
            self.users[username].followers.append(self.current_user.name)
            messagebox.showinfo("Followed", f"You followed {username}.")
        else:
            messagebox.showinfo("Already Following", f"You're already following {username}.")

    def view_followers_following(self):
        self.clear_window()
        tk.Label(self.root, text="Followers", font=("Helvetica", 14),
                 bg="#000000", fg="white").pack()
        for f in self.current_user.followers:
            tk.Label(self.root, text=f, bg="#000000", fg="white").pack()
        tk.Label(self.root, text="Following", font=("Helvetica", 14),
                 bg="#000000", fg="white").pack()
        for f in self.current_user.following:
            tk.Label(self.root, text=f, bg="#000000", fg="white").pack()
        tk.Button(self.root, text="Back", bg="#444", fg="white", command=self.dashboard).pack(pady=10)

    def logout(self):
        self.current_user = None
        self.build_main_ui()

# ------------------ Run App ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniInstagramApp(root)
    root.mainloop()
