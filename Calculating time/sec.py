hours = 3600
minutes = 60
seconds = 1

time = 33333

hours = time / hours
time2 = time % 3600
print ("how many hours that have passed:", hours)

minutes = time2 / minutes
time3 = time2 % 60
print ("how many minutes that have passed:", minutes)

seconds = time3 / minutes
print ("how many seconds that have passed:", seconds)