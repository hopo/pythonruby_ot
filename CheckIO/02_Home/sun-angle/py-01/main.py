
def sun_angle(time):
    hr = int(time[0:2])
    mn = int(time[3:])
    
    if hr >= 6 and hr <= 17:
        return ((hr-6)*15) + (mn*0.25)
    return "I don't see the sun!"

if __name__ == '__main__':
    ex1 = sun_angle("07:00") # 15
    print(ex1)
    ex2 = sun_angle("12:15") # 93.75
    print(ex2)
    ex3 =  sun_angle("01:23") # "I don't see the sun!"
    print(ex3)
    ex4 =  sun_angle("18:01") # "I don't see the sun!"
    print(ex4)


