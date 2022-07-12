def add_time (starttime, duration, day=False):

  starthr = int(starttime.split(":")[0])
  durationhr = int(duration.split(":")[0])
  min_tuple = starttime.partition(" ")[0]
  startmin = int(min_tuple.split(":")[1])
  durationmin = int(duration.split(":")[1])
  clockform = starttime.partition(" ")[2]
  clock_index = {"AM":1, "PM":2}
  clock_form = {1:"AM", 2:"PM"}
  day_index = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
  enddaynum = ["Monday", "Tursday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if clock_index[clockform] == 2 :
    starthr = starthr + 12

  totalmin = startmin + durationmin
  totalhr = starthr + durationhr
  print("totalmin: ", totalmin)
  print("totalhr: ", totalhr)

  if totalmin >= 60:
    endmin = totalmin % 60
    totalhr += 1
  else:
    endmin = totalmin
  print("totalhr: ", totalhr)

  if totalhr >= 24:
    endhr = totalhr % 24
  else:
    endhr = totalhr
    
  if totalhr%24 == 12:
    endclockform = clock_form[2]
  elif totalhr%24 >= 12 :
    endclockform = clock_form[2]
  else:
    endclockform = clock_form[1]

  if endhr >= 13:
    endhr = endhr%12
  else:
    endhr = endhr
  print(str(endhr) + endclockform)

  if endhr == 0:
    endhr = str("12")

  returnTime =  str(endhr) + ":" + str('{:02}'.format(endmin)) + " " + endclockform

  if(day):
    day = day.lower()
    print (day)
    index = int((day_index[day]) + totalhr/24) % 7
    endday = enddaynum[index]
    returnTime += ", " + endday

  if int(totalhr//24) == 1:
    end_laterday = " (next day)"
    returnTime += end_laterday

  if int(totalhr//24) >= 2:
    laterday = int(totalhr/24)
    end_dayday =  " ("+ str(laterday) + " days later)"
    returnTime += end_dayday
  
  return returnTime
