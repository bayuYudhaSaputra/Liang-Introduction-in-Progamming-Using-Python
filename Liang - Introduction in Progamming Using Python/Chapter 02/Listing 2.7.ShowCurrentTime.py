import time

currentTime = time.time() # Get current time

# Obtain the total seconds since midnaight Jan 1 1970
totalSeconds = int(currentTime)

# Get current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
curretMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is", currentHour, ":",
        curretMinute, ":", currentSecond, "GMT")