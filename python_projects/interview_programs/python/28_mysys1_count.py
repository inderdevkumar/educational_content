# count of each day 
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

count_days= {}

for item in weekdays:
    if item in count_days.keys():
        count_days[item]= count_days[item]+1
    else:
        count_days[item]= 1

print(count_days)
