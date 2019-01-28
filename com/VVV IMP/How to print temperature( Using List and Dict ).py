# list
# daily_temp = [34,56.7,34,87.3,84,34,23]
# day = input("enter 'sun', 'mon', 'tus', 'wed', 'thu', 'fri', 'sat':")
# if day == 'sun':
#     temp = daily_temp[0]
#     print('temperature is on friday', temp)
# elif day == 'mon':
#     temp = daily_temp[1]
#     print('temperature is on friday', temp)
# elif day == 'tus':
#     temp = daily_temp[2]
#     print('temperature is on friday', temp)
# elif day == 'wed':
#     temp = daily_temp[3]
#     print('temperature is on friday', temp)
# elif day == 'thu':
#     temp = daily_temp[4]
#     print('temperature is on friday', temp)
# elif day == 'fri':
#     temp = daily_temp[5]
#     print('temperature is on friday', temp)
# elif day == 'sat':
#     temp = daily_temp[6]
#     print('temperature is on friday', temp)
# else:
#     print("wrong")

# dictionary

dict_temp = {'sun':34,'mon':56, 'tus':46, 'wed':23, 'thu':54, 'fri':64, 'sat':74}
dayname = {'sun':'sunday', 'mon':'monday', 'tus':'tusrday', 'wed':'wednesday', 'thu':'thursday', 'fri':'friday',
           'sat':'saturday'}
day = input("enter 'sun', 'mon', 'tus', 'wed', 'thus', 'fri', 'sat':")
print("the temperature is on ", dayname[day] , " was ",dict_temp[day], " degrees")