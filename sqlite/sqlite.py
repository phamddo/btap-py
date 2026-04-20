import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    major TEXT,
    gpa FLOAT
)
""")

conn.commit()

# Dữ liệu sinh viên thêm
students_data = [
    ("An", "Công nghệ thông tin", 3.5),
    ("Bình", "Kế toán", 2.8),
    ("Chi", "Marketing", 3.2),
    ("Dũng", "Kỹ thuật phần mềm", 1.9),
    ("Hà", "Trí tuệ nhân tạo", 3.8)
]

# Thêm dữ liệu ghi vào dưới
cursor.executemany(
    "INSERT INTO students (name, major, gpa) VALUES (?, ?, ?)",
    students_data
)

conn.commit()

# Lấy tất cả sinh viên
print("Danh sách tất cả sinh viên:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Lấy sinh viên GPA > 3.0
print("\nSinh viên GPA > 3.0:")
cursor.execute("SELECT * FROM students WHERE gpa > 3.0")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Cập nhật GPA
cursor.execute(
    "UPDATE students SET gpa = ? WHERE name = ?",
    (3.3, "An")
)

conn.commit()

print("\nSau khi cập nhật GPA của An:")
cursor.execute("SELECT * FROM students WHERE name = ?", ("An",))
print(cursor.fetchone())

# Xóa sinh viên GPA < 2.0
cursor.execute("DELETE FROM students WHERE gpa < 2.0")
conn.commit()

print("\nDanh sách sau khi xóa:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
