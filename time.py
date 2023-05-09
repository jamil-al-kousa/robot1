
def hours(time1):
    list1 = mt.modf(time1)
    user_min = float(round(list1[0] * 100))
    user_hour = list1[1]
    current = tm.localtime()
    current_hour = float(current[3])
    current_min = float(current[4])

    if user_hour > current_hour or ( (user_hour == current_hour) and user_min > current_min):
        hour_result = user_hour - current_hour
        min_result = user_min - current_min
        hour_result_in_min = hour_result * 60
        result = hour_result_in_min + min_result
        result = result * 60
        result= int(result)
        print("programmet startar om ", result , " Sec")
        wait(result * 100)
    else: 
        print("The time is less than the current time, pls try again")
        input1 = float(input("What is the time sir?"))
        print(input1)
        hours(input1)

time2 = hours(10.35)
