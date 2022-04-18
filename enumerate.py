import datetime
import random
count = 5000000

data = {}
for d_id in range(count):
    data[str(d_id)] = random.randint(0, 1000)


t0 = datetime.datetime.now()
for i in range(len(data)):
    print(data[str(i)])

t1 = datetime.datetime.now()
dt_range_loop = (t1 - t0).total_seconds()

t00 = datetime.datetime.now()
for i, v in enumerate(data):
    print(v)
    #print(f'value: {v}')
t11 = datetime.datetime.now()

dt_enumerate = (t11 - t00).total_seconds()
print("Range loop: {} sec".format(dt_range_loop))
print("Enumerate loop: {} sec".format(dt_enumerate))
