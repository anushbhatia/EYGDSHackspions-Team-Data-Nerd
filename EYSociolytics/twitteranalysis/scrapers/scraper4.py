import twint
from datetime import datetime
current_time=datetime.today()
import os
from pathlib import Path
path=os.path.join(Path(__file__).resolve().parent.parent,"generated")

day=current_time.day
month=current_time.month
year=current_time.year
hour=current_time.hour
minute=current_time.minute
second=current_time.second


def csv_creator_four(username):
    c = twint.Config()
    c.Username = username
    c.Limit = 150
    c.Store_csv = True
    c.Output = f"output_{day}_{month}_{year}_{hour}_{minute}_{second}.csv"
    
    twint.run.Profile(c)
