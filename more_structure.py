import datetime # we can import useful built in libraries
# using 'in' and print formatting

test_results_tuple = (True, True, False, True, True, True)

if False in test_results_tuple:
    print('At least one test failed')
else:
    print('All good')

temperature_list = [-3, 2, -6, 12, 18, 3, 53, -2] # some arbitrary temperature values

# we can check that the temperature has remained within bounds
for temp in temperature_list:
    if temp < -4 or temp > 42: # we can also use 'and'
        print('too cold or too hot')
    else:
        print('temerature remained within limits')

# we can choose to format our printed output
min = -6
max = 42
precise = 12.345765573 # a precise number!!!
today = datetime.datetime.now() # gives todays date and time
# to format a string, use f'' then inject values uing {}
print(f'Today is {today} min:{min} max {max} (difference is {max-min}), {precise:0.2f}')
# sometimes strings are formatted like this (you may come across this)
print('Today is {0} max:{2}, min:{1}, delta:{3}, roughly {4:0.2f}'.format(today, min, max, max-min, precise))
