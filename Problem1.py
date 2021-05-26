"""
Input
YourCalendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
YourWorkingHours = ['9:00', '20:00']
YourWorkingHours - YourCalendar
YourCoWorkersCalendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
YourCoWorkersWorkingHours = ['10:00', '18:30'] meetingDuration = 30

Sample Output:
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
"""

from datetime import datetime

def free_time(schedule, working_hours, time):
    new = []
    b_start = datetime.strptime(working_hours[0], "%H:%M")
    b_end = datetime.strptime(working_hours[1], "%H:%M")
    start = datetime.strptime(schedule[0][0], "%H:%M")
    end = datetime.strptime(schedule[len(schedule) - 1][1], "%H:%M")
    min_start = (b_start - start).seconds / 60
    min_end = (b_end - end).seconds / 60
    if min_start >= float(time):
        new.append([working_hours[0], schedule[0][0]])
    for i in range(len(schedule) - 1):
        if ((datetime.strptime(schedule[i + 1][0], "%H:%M") - datetime.strptime(schedule[i][1], "%H:%M")).seconds / 60) >= float(
                time):
            new.append([schedule[i][1], schedule[i + 1][0]])
    if min_end >= float(time):
        new.append([schedule[len(schedule) - 1][1], working_hours[1]])

    return new

def meeting_time(calendar1, calendar2, time):
    pres = []
    final = []
    for i in range(len(calendar1)):
        for j in range(len(calendar2)):
            if datetime.strptime(calendar1[i][1], "%H:%M") <= datetime.strptime(calendar2[j][1], "%H:%M"):
                if datetime.strptime(calendar1[i][0], "%H:%M") >= datetime.strptime(calendar2[j][0], "%H:%M"):
                    if ((datetime.strptime(calendar1[i][1], "%H:%M") - datetime.strptime(calendar1[i][0],
                                                                                         "%H:%M")).seconds / 60) >= float(
                            time):
                        pres.append([calendar1[i][0], calendar1[i][1]])
                else:
                    if ((datetime.strptime(calendar1[i][1], "%H:%M") - datetime.strptime(calendar2[j][0],
                                                                                         "%H:%M")).seconds / 60) >= float(
                            time):
                        pres.append([calendar2[j][0], calendar1[i][1]])
            else:
                if datetime.strptime(calendar1[i][0], "%H:%M") >= datetime.strptime(calendar2[j][0], "%H:%M"):
                    if ((datetime.strptime(calendar2[j][1], "%H:%M") - datetime.strptime(calendar1[i][0],
                                                                                         "%H:%M")).seconds / 60) >= float(
                            time):
                        pres.append([calendar1[i][0], calendar2[j][1]])
    for i in range(len(pres)):
        if datetime.strptime(pres[i][0], "%H:%M") < datetime.strptime(pres[i][1], "%H:%M"):
            final.append([pres[i][0], pres[i][1]])

    return final

person1=[['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
person2=[['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
working_hours_p1=['9:00', '20:00']
working_hours_p2=['10:00', '18:30']
time_def=30

calendar1=free_time(person1,working_hours_p1,time_def)
calendar2=free_time(person2,working_hours_p2,time_def)
meetings=meeting_time(calendar1,calendar2, time_def)

# for i in range(len(meetings)):
#     print('You can have the meeting during : ', meetings[i])
for i in range(len(meetings)):
    print(f'Option {i+1}: You can have the meeting during {meetings[i]}')
