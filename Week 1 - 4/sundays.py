start = [1, 1, 1900]
months = {
1: 31,
2: 28,
3: 31,
4: 30,
5: 31,
6: 30,
7: 31,
8: 31,
9: 30,
10: 31,
11: 30,
12: 31
}

days = [0, 1, 2, 3, 4, 5, 6]
# sun, mon, tue, wed, thur, fri, sat
cur_day = 2
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if year % 4 == 0:
            end_day = 29
        else: 
            end_day = months[month]
        for day in range(1, end_day + 1):
            if day == 1 and days[cur_day % 7] == 0:
                count += 1
            #print "%i / %i / %i - %i" %(month, day, year, days[cur_day % 7])                
            cur_day += 1

print count                

