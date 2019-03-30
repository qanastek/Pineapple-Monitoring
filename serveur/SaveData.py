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

	conn = sqlite3.connect('alerts.db')

	c = conn.cursor()

	c.execute("""ALTER TABLE alerts ADD COLUMN disk int""")

	conn.commit()

	conn.close()

def createTableAlerts():

	conn = sqlite3.connect('alerts.db')

	c = conn.cursor()

	c.execute("""CREATE TABLE alerts(
		mac text,
		receivedDate date,
		currentCpuLoad int,
		currentDiskUsage int,
		currentSwapUsage int,
		currentMemLoad int,
		currentConnectedUsers int,
		processCounter int,
		sysExp text,
		coreCounter int,
		ram int,
		disk int
	)""")

	conn.commit()

	conn.close()

def createTable():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("""CREATE TABLE historique(
		mac text,
		receivedDate date,
		currentCpuLoad int,
		currentDiskUsage int,
		currentSwapUsage int,
		currentMemLoad int,
		currentConnectedUsers int,
		processCounter int,
		sysExp text,
		coreCounter int,
		ram int,
		disk int
	)""")

	conn.commit()

	conn.close()

def getTableAlerts():

	conn = sqlite3.connect('alerts.db')

	c = conn.cursor()

	c.execute("SELECT * from alerts")

	result = c.fetchall()

	conn.commit()

	conn.close()

	return result

def getTable():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("SELECT * from historique")

	result = c.fetchall()

	conn.commit()

	conn.close()

	return result

def getComputers():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	c.execute("""SELECT DISTINCT
					mac,
					sysExp,
					coreCounter,
					treadsCounter,
					cpuModel,
					hostName,
					ram,
					disk
				 from historique
				 order by receivedDate DESC;""")

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

def showTableAlerts():

	conn = sqlite3.connect('alerts.db')

	c = conn.cursor()

	c.execute("SELECT * from alerts")

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
		:processCounter,
		:sysExp,
		:coreCounter,
		:treadsCounter,
		:cpuModel,
		:hostName,
		:ram,
		:disk)""", {
			'mac' : JsonIn['mac'],
			'receivedDate' : datetime.datetime.now(),
			'currentCpuLoad' : JsonIn['currentCpuLoad'],
			'currentDiskUsage' : JsonIn['currentDiskUsage'],
			'currentSwapUsage' : JsonIn['currentSwapUsage'],
			'currentMemLoad' : JsonIn['currentMemLoad'],
			'currentConnectedUsers' : JsonIn['currentConnectedUsers'],
			'processCounter' : JsonIn['processCounter'],
			'sysExp' : JsonIn['sysExp'],
			'coreCounter' : JsonIn['coreCounter'],
			'treadsCounter' : JsonIn['treadsCounter'],
			'cpuModel' : JsonIn['cpuModel'],
			'hostName' : JsonIn['hostName'],
			'ram' : JsonIn['ram'],
			'disk' : JsonIn['disk']
		})

	conn.commit()

	conn.close()

def SaveDataAlerts(JsonIn):

	conn = sqlite3.connect('alerts.db')

	c = conn.cursor()

	c.execute("""INSERT INTO alerts VALUES (
		:mac,
		:receivedDate,
		:currentCpuLoad,
		:currentDiskUsage,
		:currentSwapUsage,
		:currentMemLoad,
		:currentConnectedUsers,
		:processCounter,
		:sysExp,
		:coreCounter,
		:treadsCounter,
		:cpuModel,
		:hostName,
		:ram,
		:disk)""", {
			'mac' : JsonIn['mac'],
			'receivedDate' : datetime.datetime.now(),
			'currentCpuLoad' : JsonIn['currentCpuLoad'],
			'currentDiskUsage' : JsonIn['currentDiskUsage'],
			'currentSwapUsage' : JsonIn['currentSwapUsage'],
			'currentMemLoad' : JsonIn['currentMemLoad'],
			'currentConnectedUsers' : JsonIn['currentConnectedUsers'],
			'processCounter' : JsonIn['processCounter'],
			'sysExp' : JsonIn['sysExp'],
			'coreCounter' : JsonIn['coreCounter'],
			'treadsCounter' : JsonIn['treadsCounter'],
			'cpuModel' : JsonIn['cpuModel'],
			'hostName' : JsonIn['hostName'],
			'ram' : JsonIn['ram'],
			'disk' : JsonIn['disk']
		})

	conn.commit()

	conn.close()

	# showTable()

# createTable()
# addColumn()
# showTable()
# dropTable()
# createTableAlerts()