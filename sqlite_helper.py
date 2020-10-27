"""
БОТА СОЗДАЛ "CVC" - t.me/cvc_code
"""
import sqlite3

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()


def add_user(uid):
	result = c.execute("SELECT * FROM adminka_user WHERE uid=?", [uid]).fetchone()
	if not result:
		c.execute("INSERT INTO adminka_user (uid, status) VALUES (?, ?)", [uid, ""])
		conn.commit()
#

def get_all_categories():
	result = c.execute("SELECT * FROM adminka_category").fetchall()
	return result


def get_items(category_id):
	result = c.execute("SELECT * FROM adminka_item WHERE item_category=?", [category_id]).fetchall()
	if len(result) != 0:
		return result
	else:
		return None


def is_category_exists(category_id):
	result = c.execute("SELECT * FROM adminka_category WHERE category_id=?", [category_id]).fetchone()
	if result:
		return result[2]
	else:
		return False


def is_item_exists(item_title):
	result = c.execute("SELECT * FROM adminka_item WHERE item_title=?", [item_title]).fetchone()
	print(result)
	if result:
		return result
	else:
		return None