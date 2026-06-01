import sqlite3 
variable = sqlite3.connect('database.db')
cursor = variable.cursor()

variable.commit()
variable.close()