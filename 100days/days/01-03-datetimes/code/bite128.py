from datetime import datetime
from datetime import date

THIS_YEAR = '2018'
date = "8 Aug, 2015"
print(int(THIS_YEAR) - int(datetime.strptime(date, "%d %b, %Y").year))

eu_date = "11/03/2002"
convdate = datetime.strptime(eu_date, "%d/%m/%Y")
am_date = convdate.strftime("%m/%d/%Y")
