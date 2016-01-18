# Hint:  use Google to find python function

from dateutil import parser
from datetime import date

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

d_start = parser.parse(date_start)
d_stop = parser.parse(date_stop)
diff = d_stop - d_start
days = diff.days
print days


####b) 

 
date_start = '12312013'  
date_stop = '05282015'  

d_start = date(int(date_start[4:]), int(date_start[0:2]), int(date_start[2:4]))
d_stop = date(int(date_stop[4:]), int(date_stop[0:2]), int(date_stop[2:4]))
diff = d_stop - d_start
days = diff.days
print days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

d_start = parser.parse(date_start)
d_stop = parser.parse(date_stop)
diff = d_stop - d_start
days = diff.days
print days
