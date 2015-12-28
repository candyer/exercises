Modify the valid_month() function to verify whether the data a user enters is a valid month.
If the passed in parameter 'month' is not a valid month, return None. 
If 'month' is a valid month, then return the name of the month with the first letter capitalized.

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

# solution 1
def valid_month(month):
    cap_month = month.capitalize()
    if cap_month in months:
        return cap_month
        
        
# solution 2
def valid_month(month):
    if month:
        cap_month =  month.capitalize()
        if cap_month in months:
            return cap_month

print valid_month("january")  # January   
print valid_month("aPril")  # April
print valid_month("foo") # None
print valid_month("") # None
print valid_month("maY") # May


# solution 3
def valid_month(month):
    month_abbvs = dict((m[:3].lower(),m) for m in months)
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
        
print valid_month('decdfghjk')  # December
print valid_month('feb')  # February
print valid_month('') # None




Modify the valid_day() function to verify whether the string a user enters is a valid day. The valid_day() function takes as 
input a String, and returns either a valid Int or None. If the passed in String is not a valid day, return None. 
If it is a valid day, then return the day as an Int, not a String. Don't worry about months of different length. 
Assume a day is valid if it is a number between 1 and 31.Be careful, the input can be any string 
at all, you don't have any guarantees that the user will input a sensible day.

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if 0 < day <= 31:
            return day

print valid_day('3') # 3
print valid_day('foo') # None


