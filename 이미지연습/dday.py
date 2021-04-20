from PIL import *
import datetime
def get_dday_data(year,month,day):

    today=datetime.date(year=year,month=month,day=day)

    td=datetime.timedelta(days=99)
    td1=datetime.timedelta(days=199)
    td2=datetime.timedelta(days=299)
    td3=datetime.date(year=year+1,month=month,day=day)

    td4=datetime.timedelta(days=399)
    td5=datetime.timedelta(days=499)
    td6=datetime.timedelta(days=599)
    td7=datetime.timedelta(days=699)
    td8=datetime.date(year=year+2,month=month,day=day)

    td9=datetime.timedelta(days=799)
    td10=datetime.timedelta(days=899)
    td11=datetime.timedelta(days=999)
    td12=datetime.date(year=year+3,month=month,day=day)

    td13=datetime.timedelta(days=1099)
    td14=datetime.timedelta(days=1199)
    td15=datetime.timedelta(days=1299)
    td16=datetime.timedelta(days=1399)
    td17=datetime.date(year=year+4,month=month,day=day)

    td18=datetime.timedelta(days=1499)
    td19=datetime.timedelta(days=1599)
    td20=datetime.timedelta(days=1699)
    td21=datetime.timedelta(days=1799)
    td22=datetime.date(year=year+5,month=month,day=day)

    td23=datetime.timedelta(days=1899)
    td24=datetime.timedelta(days=1999)
    td25=datetime.timedelta(days=2099)
    td26=datetime.date(year=year+6,month=month,day=day)

    td27=datetime.timedelta(days=2199)
    td28=datetime.timedelta(days=2299)
    td29=datetime.timedelta(days=2399)
    td30=datetime.timedelta(days=2499)
    td31=datetime.date(year=year+7,month=month,day=day)

    td32=datetime.timedelta(days=2599)


    dday = []
    dday.append(today)
    dday.append(today+td)
    dday.append(today+td1)
    dday.append(today+td2)
    dday.append(td3)
    dday.append(today+td4)
    dday.append(today+td5)
    dday.append(today+td6)
    dday.append(today+td7)
    dday.append(td8)
    dday.append(today+td9)
    dday.append(today+td10)
    dday.append(today+td11)
    dday.append(td12)
    dday.append(today+td13)
    dday.append(today+td14)
    dday.append(today+td15)
    dday.append(today+td16)
    dday.append(td17)
    dday.append(today+td18)
    dday.append(today+td19)
    dday.append(today+td20)
    dday.append(today+td21)
    dday.append(td22)
    dday.append(today+td23)
    dday.append(today+td24)
    dday.append(today+td25)
    dday.append(td26)
    dday.append(today+td27)
    dday.append(today+td28)
    dday.append(today+td29)
    dday.append(today+td30)
    dday.append(td31)
    dday.append(today+td32)


    return dday

