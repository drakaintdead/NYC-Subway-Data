**NYC Subway Data**

This program gets data from the MTA/NYCT (Metropolitan Transport Authority/New York City Transit)'s GTFS subway data, and texts it to me via email-to-SMS.

---

**How it works**
> I'm using the library `nyct-gtfs`, that gets data from the MTA's GTFS feed and translates it into python.  
I set it up to get the data for only Q trains that are going to stop at Atlantic Av-Barclays Ctr (`D24N` is the stop ID).  
It gets all of the info from the `StopTimeUpdate` objects stored in the list `trains[0]`.
The code searches through the `trains[0]` list until it can find the correct stop id, to make sure that it always displays the correct stations.
It then puts all of the info together into a string, and uses the `smtplib` library to send the email.

**How to use it**
1. First, you need to create an account for the MTA. You need this to get your API key. [Link](https://api.mta.info/#/signup)
2. Log in and grab your API key.
3. put in your login info into a .env file, with the correct naming.
  > **Important Note: You must allow less secure apps if using gmail, and if not using gmail, make sure to change the smtp server.**  
4. Download and install these two python libraries: [pytz](https://pypi.org/project/pytz/) and [nyct-gtfs](https://pypi.org/project/nyct-gtfs/). All the other libraries come with python by default.  
5. Change the following things to make the code how you want it:
> Line 20: Change `"Q"` to whatever line you want to get data from *Note: If you write Q, it will get the data for NQRW trains. If you select 1, it will get the data for 123 trains. It gets the data for the entire line set (If not sure what the sets are check the API portal)  
Line 21: Change `line_id` and `headed_for_stop_id` to the lines (ex. "B") and stops (ex. "D24N") that you want. You can put multiple values. Stop id's can be found [here](https://github.com/Andrew-Dickinson/nyct-gtfs/blob/master/nyct_gtfs/gtfs_static/stops.txt).  
Line 27 & 28: Change the stop id's to the 2 stations that you wish to get the data for. `atlantic` is the station you want the main data for (most commonly the stop that you put in `headed_for_stop_id`) and `fiftyseventh` is the other station.  
Line 80: You can change how the message is formatted however you want. A few things to note about it however: Make sure to remove any indents. If there are then it will result in the formatting messing up. Also if you want to use colons in the message, you must have a subject. Otherwise the message will be blank.  
6. Run the code!

---

If you have any issues with the code, please submit it [here](https://github.com/drakaintdead/NYC-Subway-Data/issues/new). Make sure to include adequate info as to what exactly the problem is and how to replicate it.
