import psutil

print psutil.cpu_percent(interval=1)

print psutil.cpu_count()

print psutil.cpu_count(logical=False)