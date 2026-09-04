
import datetime      
import time
now = datetime.datetime.now()   #this is used for current date and time 
print(now)


timestamp = time.time()      #we use timestamp to record a event which accour at an time for example if we want to save login histroy of user we use timestamp
print(timestamp)
current_time =time.ctime(timestamp)
print(current_time)

#to calculate how much time has passed 
start =time.time()
end = time.time()
print("time taken :",end -start,"seconds")

#strftime = string+ format + time

print(now.strftime("%d,%B,%Y"))
print(now.strftime("%d,%m,%Y,%H:%M:%S"))
