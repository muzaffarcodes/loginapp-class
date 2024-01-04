import sys
from PyQt5.QtWidgets import *
import sqlite3

class Window(QWidget):
	def __init__(self):
		super(Window,self).__init__()
		self.db_connect()
		self.ui_start()
	
	def db_connect(self):
		self.kontact = sqlite3.connect("loginpage.db")
		self.cursr = self.kontact.cursor()
		self.cursr.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
		self.kontact.commit()

	def ui_start(self):
		self.username = QLineEdit()
		self.password = QLineEdit()
		self.password.setEchoMode(QLineEdit.Password)
		self.text_body = QLabel("Enter username and password, broo!")
		self.log_in = QPushButton("Log In")
		self.sign_up = QPushButton("Sign Up")
		self.cancel = QPushButton("Cancel")

		v_box = QVBoxLayout()
		v_box.addWidget(self.username)
		v_box.addWidget(self.password)
		v_box.addWidget(self.text_body)
		v_box.addWidget(self.log_in)
		v_box.addWidget(self.sign_up)
		v_box.addStretch()

		h_box = QHBoxLayout()
		h_box.addStretch()
		h_box.addLayout(v_box)
		h_box.addStretch()

		self.setLayout(h_box)

		self.log_in.clicked.connect(self.login)
		self.sign_up.clicked.connect(self.signup)
		self.setWindowTitle("python_Killer.com")
		self.setFixedSize(600,300)
		self.show()

	def login(self):
		name = self.username.text()
		passwd = self.password.text()
		a = "SELECT * FROM users WHERE username = ? AND password = ?"
		self.cursr.execute(a,(name,passwd))
		data = self.cursr.fetchall()
		if(len(data) == 0):
			self.text_body.setText("Password or username is ERROR!")
		else:
			self.text_body.setText("Welcome to Instagram!")

	def signup(self):
		new_user = self.username.text()
		new_pass = self.password.text()
		b = "INSERT INTO users VALUES(?,?)"
		self.cursr.execute(b,(new_user,new_pass))
		self.kontact.commit()
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
