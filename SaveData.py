import sqlite3
import datetime
import json

def dropTable():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("""DROP TABLE historique""")

	conn.commit()

	conn.close()

def addColumn():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("""ALTER TABLE historique ADD COLUMN receivedDate date""")

	conn.commit()

	conn.close()

def createTable():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("""CREATE TABLE historique(
		mac text,
		receivedDate date,
		currentCpuLoad text,
		currentDiskUsage text,
		currentSwapUsage text,
		currentMemLoad text,
		currentConnectedUsers text,
		processCounter text
	)""")

	conn.commit()

	conn.close()

def getTable():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("SELECT * from historique")

	result = c.fetchall()

	conn.commit()

	conn.close()

	return result

def showTable():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("SELECT * from historique")

	print(json.dumps(c.fetchall(), indent=4, sort_keys=True))

	conn.commit()

	conn.close()


def SaveData(JsonIn):

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("""INSERT INTO historique VALUES (
		:mac,
		:receivedDate,
		:currentCpuLoad,
		:currentDiskUsage,
		:currentSwapUsage,
		:currentMemLoad,
		:currentConnectedUsers,
		:processCounter)""", {
			'mac' : JsonIn['mac'],
			'receivedDate' : datetime.datetime.now(),
			'currentCpuLoad' : JsonIn['currentCpuLoad'],
			'currentDiskUsage' : JsonIn['currentDiskUsage'],
			'currentSwapUsage' : JsonIn['currentSwapUsage'],
			'currentMemLoad' : JsonIn['currentMemLoad'],
			'currentConnectedUsers' : JsonIn['currentConnectedUsers'],
			'processCounter' : JsonIn['processCounter']
		})

	conn.commit()

	conn.close()

	# showTable()

# createTable()
# addColumn()
# showTable()
# dropTable()