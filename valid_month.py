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
