from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ----------------
def connect_db():
    conn = sqlite3.connect("database.db")
    return conn


# ---------------- HOME PAGE ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- REGISTER STUDENT ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        matric = request.form["matric"]
        dept = request.form["dept"]
        fid = request.form["fingerprint_id"]

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                matric TEXT,
                dept TEXT,
                fingerprint_id TEXT
            )
        """)

        cursor.execute("""
            INSERT INTO students (name, matric, dept, fingerprint_id)
            VALUES (?, ?, ?, ?)
        """, (name, matric, dept, fid))

        conn.commit()
        conn.close()

        return redirect("/register")

    return render_template("register.html")


# ---------------- ATTENDANCE PAGE ----------------
@app.route("/attendance")
def attendance():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date TEXT,
            time TEXT
        )
    """)

    cursor.execute("SELECT * FROM attendance")
    data = cursor.fetchall()

    conn.close()

    return render_template("attendance.html", records=data)


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, render_template, request, redirect
    import sqlite3

    app = Flask(__name__)


    def connect():
        return sqlite3.connect("database.db")


    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            name = request.form["name"]
            matric = request.form["matric"]
            dept = request.form["dept"]

            conn = connect()
            cur = conn.cursor()

            cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                matric TEXT,
                dept TEXT
            )
            """)

            cur.execute("INSERT INTO students (name, matric, dept) VALUES (?, ?, ?)",
                        (name, matric, dept))

            conn.commit()
            conn.close()

            return redirect("/register")

        return render_template("register.html")


    if __name__ == "__main__":
        app.run(debug=True)
    from flask import Flask, render_template, request, redirect
    import sqlite3

    app = Flask(__name__)


    def connect():
        return sqlite3.connect("database.db")


    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            name = request.form["name"]
            matric = request.form["matric"]
            dept = request.form["dept"]

            conn = connect()
            cur = conn.cursor()

            cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                matric TEXT,
                dept TEXT
            )
            """)

            cur.execute("INSERT INTO students (name, matric, dept) VALUES (?, ?, ?)",
                        (name, matric, dept))

            conn.commit()
            conn.close()

            return redirect("/register")

        return render_template("register.html")


    if __name__ == "__main__":
        app.run(debug=True)