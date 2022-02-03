from nyct_gtfs import NYCTFeed
import datetime
import pytz
import os
import smtplib, ssl
import math

api_key = os.environ['mta_api_key']
password = os.environ['gmailpassword']
email = os.environ['email']
phone = os.environ['phone_email']

port = 587
smtp_server = "smtp.gmail.com"
sender_email = email
receiver_email = phone
password = password

feed = NYCTFeed("Q", api_key=api_key)
trains = feed.filter_trips(line_id=["Q"], headed_for_stop_id=["D24N"], underway=True)
feed.refresh()

est = pytz.timezone("America/New_York")

lists = trains[0].stop_time_updates
atlantic = "D24N"
fiftyseventh = "R14N"

score1, score2 = -1, -1

for StopTimeUpdate in lists:
  score1 += 1
  station = trains[0].stop_time_updates[score1]
  if atlantic in station.stop_id:
    break

for StopTimeUpdate in lists:
  score2 += 1
  station = trains[0].stop_time_updates[score2]
  if fiftyseventh in station.stop_id:
    break

arrivalTime = trains[0].stop_time_updates[score1].arrival
timeNow = datetime.datetime.now()
timedelta = arrivalTime - timeNow
secsRemaining = timedelta.total_seconds()
reeeeee = math.floor(secsRemaining/60)
eeeeeer = round(secsRemaining%60)
timeuntil = f"{reeeeee}:{eeeeeer}"

if reeeeee > 1:
  mins = f"{reeeeee} mins {eeeeeer} secs away"
elif reeeeee == 1:
  mins = f"{reeeeee} min {eeeeeer} secs away"
elif reeeeee == 0:
  mins = "Arriving"
else:
  mins = f"{reeeeee} mins {eeeeeer} secs away"

atlantic = trains[0].stop_time_updates[score1]
atlanticName = "Atlantic-Barclays"
atlanticArrival = atlantic.arrival
atlanticArrivalEst = atlanticArrival.astimezone(est)
atlanticArrivalFormat = atlanticArrivalEst.strftime("%-I:%M %p")

fiftyseventh = trains[0].stop_time_updates[score2]
fiftyseventhName = fiftyseventh.stop_name
fiftyseventhArrival = fiftyseventh.arrival
fiftyseventhArrivalEst = fiftyseventhArrival.astimezone(est)
fiftyseventhArrivalFormat = fiftyseventhArrivalEst.strftime("%-I:%M %p")

currentStop = trains[0].stop_time_updates[0]
currentStopName = currentStop.stop_name

lastUpdate = trains[0].last_position_update
lastUpdateEst = lastUpdate.astimezone(est)
lastUpdateFormat = lastUpdateEst.strftime("%-I:%M:%S %p %Z")

message = f"""\
Subject: NYC Subway info as of {lastUpdateFormat}

:
Next Q at {atlanticName}: {atlanticArrivalFormat}
-----------
This train is {mins} from {atlanticName} and will arrive at {fiftyseventhName} at {fiftyseventhArrivalFormat}. The current location of the train is: {currentStopName}"""
print(message)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()