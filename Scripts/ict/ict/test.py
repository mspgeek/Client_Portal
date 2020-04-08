from datetime import datetime

start = datetime.utcnow()

date = start.date()
time = start.time()

print(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))



print(date)
print(time)

