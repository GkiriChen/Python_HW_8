from datetime import datetime, timedelta

def get_birthdays_per_week(users=None):
    #print(users)
    if users == None:
        print('Дні народження на наступний тиждень відсутні')
    else:

        date_now = datetime.now()
        delta = timedelta(days=(6 - datetime.isoweekday(date_now))) 
        next_mon = (date_now + delta).date() #наступний понеділок
        delta7 = timedelta(days=(12 - datetime.isoweekday(date_now))) 
        next_sun = (date_now + delta7).date() #наступна неділя
        # print('ближчий понеділок', (date_now + delta).date() )
        # print('наступна неділя ', (date_now + delta7).date() )
        ddd = {}

        for user in users:     

            for key in user.keys():
                date_b = datetime.strptime(user[key], '%Y-%m-%d') #дата дня народження                       

                if date_b.strftime("%m") == date_now.strftime("%m"): #якщо місяць дня народженя співпадає з поточним місяцем
                    
                    if date_b.strftime("%d") >= next_mon.strftime("%d") and date_b.strftime("%d") <= next_sun.strftime("%d"): #якщо день у проміжу наступного тижня                 
                        day = datetime(int(date_now.strftime("%Y")), int(date_b.strftime("%m")), int(date_b.strftime("%d") ))                    
                        #print(day.strftime("%A"), ':', key )
                        day_week = day.strftime("%A")
                        #print(key, day_week)
                        if day_week in ('Saturday', 'Sunday'): #якщо день народження припадає на вихідні
                            day_week = 'Monday'
                        
                        #print(ddd.get(day_week))
                        if ddd.get(day_week) == None: #запомнюємо словник 
                            ddd.update({day_week: key})
                        else:
                            if type(ddd.get(day_week)) != list:                            
                                name = [ddd.get(day_week),]
                                name.append(key)
                                ddd.update({day_week: name})
                            else:
                                name = ddd.get(day_week)
                                name.append(key)
                                ddd.update({day_week: name})
                        #     print(name)
        print(ddd)
        for n in ddd:        
            if type(ddd[n]) != list:
                print(f"{n}: {ddd[n]}")
            else:            
                print(f"{n}:",', '.join(ddd[n]))
                
use = [{'Sveta': '2000-05-14'}, {'Gena': '2000-05-19'}, {'Mama': '2000-05-13'}, 
       {'Oleg': '2000-05-14'}, {'Lena': '2000-05-22'}, {'Dima': '2000-05-18'}, {'Egor': '2000-05-14'}, {'Antom': '2000-05-15'}]
get_birthdays_per_week(use)