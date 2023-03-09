from datetime import datetime

def time10(x):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
    Hours = currentDateAndTime.strftime("%H")
    Minutes = currentDateAndTime.strftime("%M")
    Minutes10 = int(Minutes) + 10

    if Minutes10 >= 60:
        Minutes10 = int(Minutes10)
        Minutes10 -= 60
        Hours = int(Hours)
        Hours += 1
        Hours = str(Hours)
        if int(Minutes10) < 10:
            Minutes10 = "0" + Minutes10

    Minutes10 = str(Minutes10)
    FirstRing = Hours + ":" + Minutes10
    if x == "FirstRing":
        return FirstRing

def time8(x):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
    Hours = currentDateAndTime.strftime("%H")
    Minutes = currentDateAndTime.strftime("%M")
    Minutes8 = int(Minutes) + 8

    if Minutes8 >= 60:
        Minutes8 = int(Minutes8)
        Minutes8 -= 60
        Hours = int(Hours)
        Hours += 1
        Hours = str(Hours)
        if int(Minutes8) < 10:
            Minutes8 = "0" + Minutes8

    Minutes8 = str(Minutes8)
    SecondRing = Hours + ":" + Minutes8
    if x == "SecondRing":
        return SecondRing

def time5(x):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
    Hours = currentDateAndTime.strftime("%H")
    Minutes = currentDateAndTime.strftime("%M")
    Minutes5 = int(Minutes) + 5

    if Minutes5 >= 60:
        Minutes5 = int(Minutes5)
        Minutes5 -= 60
        Hours = int(Hours)
        Hours += 1
        Hours = str(Hours)
        if int(Minutes5) < 5:
            Minutes5 = "0" + Minutes5

    Minutes5 = str(Minutes5)
    ThirdRing = Hours + ":" + Minutes5
    if x == "ThirdRing":
        return ThirdRing

def time2(x):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
    Hours = currentDateAndTime.strftime("%H")
    Minutes = currentDateAndTime.strftime("%M")
    Minutes2 = int(Minutes) + 2

    if Minutes2 >= 60:
        Minutes2 = int(Minutes2)
        Minutes2 -= 60
        Hours = int(Hours)
        Hours += 1
        Hours = str(Hours)
        if int(Minutes2) < 10:
            Minutes2 = "0" + Minutes2

    Minutes2 = str(Minutes2)
    FinalRing = Hours + ":" + Minutes2
    if x == "FinalRing":
        return FinalRing









