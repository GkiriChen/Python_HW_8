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
                        
                        if day_week in ('Saturday', 'Sunday'): #якщо день народження припадає на вихідні
                            day_week = 'Monday'
                        
                        if ddd.get(day_week) == None: #запомнюємо словник 
                            ddd.update({day_week: key})
                        else:
                            
                            name = [ddd.get(day_week),]
                            #print(name, key)
                            name.append(key) 
                            ddd.update({day_week: name})
                    
        #print(ddd)
        for n in ddd:        
            if type(ddd[n]) != list:
                print(f"{n}: {ddd[n]}")
            else:            
                print(f"{n}:",', '.join(ddd[n]))
                
