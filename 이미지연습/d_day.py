from PIL import *

from datetime import datetime

def get_dayday_data(year,month,day):
    today = datetime.now()
    first_day=datetime(year=year,month=month,day=day)

    dayday = (today - first_day).days + 1
    return dayday

