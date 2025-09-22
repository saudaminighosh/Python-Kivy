import sqlite3
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker



# ----------------- DATABASE SETUP -----------------
def init_db():
    conn = sqlite3.connect("tinnitus_tracker.db")
    cursor = conn.cursor()

    # User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Logs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            time TEXT,
            duration INTEGER,
            notes TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect("tinnitus_tracker.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def authenticate(username, password):
    conn = sqlite3.connect("tinnitus_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None


def add_log(user_id, date, time, duration, notes=""):
    conn = sqlite3.connect("tinnitus_tracker.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs (user_id, date, time, duration, notes) VALUES (?, ?, ?, ?, ?)",
        (user_id, date, time, duration, notes)
    )
    conn.commit()
    conn.close()


def get_logs(user_id):
    conn = sqlite3.connect("tinnitus_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, time, duration, notes FROM logs WHERE user_id=?", (user_id,))
    logs = cursor.fetchall()
    conn.close()
    return logs


# ----------------- KIVY SCREENS -----------------
class LoginScreen(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.app = app

        self.add_widget(Label(text="Username"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        login_btn = Button(text="Login")
        login_btn.bind(on_press=self.login)
        self.add_widget(login_btn)

        signup_btn = Button(text="Signup")
        signup_btn.bind(on_press=self.signup)
        self.add_widget(signup_btn)

        self.message = Label(text="")
        self.add_widget(self.message)

    def login(self, instance):
        user_id = authenticate(self.username.text, self.password.text)
        if user_id:
            self.app.root.clear_widgets()
            self.app.root.add_widget(MainAppScreen(user_id))
        else:
            self.message.text = "Invalid username or password"

    def signup(self, instance):
        if add_user(self.username.text, self.password.text):
            self.message.text = "User registered successfully"
        else:
            self.message.text = "Username already exists"


class MainAppScreen(BoxLayout):
    def __init__(self, user_id, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.user_id = user_id

        self.add_widget(Label(text=f"Welcome, User {user_id}"))

        # Calendar (Date Picker) button
        self.date_label = Label(text="Select Date")
        self.add_widget(self.date_label)

        date_btn = Button(text="Pick Date")
        date_btn.bind(on_press=self.show_date_picker)
        self.add_widget(date_btn)

        # Other inputs
        self.time = TextInput(hint_text="Time (HH:MM)", multiline=False)
        self.add_widget(self.time)

        self.duration = TextInput(hint_text="Duration (minutes)", multiline=False)
        self.add_widget(self.duration)

        self.notes = TextInput(hint_text="Notes", multiline=False)
        self.add_widget(self.notes)

        log_btn = Button(text="Add Log")
        log_btn.bind(on_press=self.add_log_entry)
        self.add_widget(log_btn)

        show_btn = Button(text="Show Logs")
        show_btn.bind(on_press=self.show_logs)
        self.add_widget(show_btn)

        self.logs_label = Label(text="")
        self.add_widget(self.logs_label)

        self.selected_date = None  # to store calendar result

    def show_date_picker(self, instance):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_save)
        date_dialog.open()

    def on_date_save(self, instance, value, date_range):
        # value is a datetime.date
        self.selected_date = str(value)
        self.date_label.text = f"Date: {self.selected_date}"

    def add_log_entry(self, instance):
        if not self.selected_date:
            self.logs_label.text = "Please pick a date first!"
            return
        add_log(self.user_id, self.selected_date, self.time.text, self.duration.text, self.notes.text)
        self.logs_label.text = "Log added successfully!"

    def show_logs(self, instance):
        logs = get_logs(self.user_id)
        text = "\n".join([f"{d} {t} ({dur} min): {n}" for d, t, dur, n in logs])
        self.logs_label.text = text if text else "No logs yet."


class TinnitusApp(MDApp):
    def build(self):
        init_db()
        root = BoxLayout()
        root.add_widget(LoginScreen(self))
        return root


if __name__ == "__main__":
    TinnitusApp().run()
