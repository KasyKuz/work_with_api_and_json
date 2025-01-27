import requests as req
import json
import matplotlib.pyplot as plt
API_BASE = 'https://ruz.spbstu.ru/api/v1/ruz/'
#ctrl+shift+f10

lessons = [0 for i in range(6)]
def weekdays(num):
    match num:
        case 1:
            print("Понедельник", end =" ")
        case 2:
            print("Вторник", end =" ")
        case 3:
            print("Среда", end =" ")
        case 4:
            print("Четверг", end =" ")
        case 5:
            print("Пятница", end =" ")
        case 6:
            print("Суббота", end =" ")


#38653
def schedule(transf_json_data, data):
    flag=0
    for i in transf_json_data['groups']:
        if i['name'] == gr:
            print(i['id'])
            flag = 1
            json_data = req.get(API_BASE + 'scheduler/' +str(i['id']) + '?date=' + data[6]+data[7]+data[8]+data[9]+'-'+data[3]+data[4]+'-'+data[0]+data[1]).text
            transf_json_data = json.loads(json_data)
            #       print(transf_json_data)
            if transf_json_data["week"]["is_odd"] == True:
                print("                  ---------------------------неделя четная---------------------------")
            else:
                print("                  ---------------------------неделя четная---------------------------")
            for j in transf_json_data["days"]:
                a = j['weekday']
                weekdays(a)
                print(j['date'])
               # print(f"Date: {j['date']}")
                num_of_pairs = 0
                for k in j["lessons"]:
                    num_of_pairs += 1
                    print('      ', k['subject']+': ',k['time_start'],'-',k['time_end'],' ',k['auditories'][0]['building']['name'],' ',k['auditories'][0]['name'])

                    if k['teachers'] != None:
                        print("                        ( Преподаватель: ", k['teachers'][0]['full_name'],')')
                    else:
                        print("                        ( Преподаватель не указан )")
                lessons[a-1] = num_of_pairs
            break
    return flag
def diagramma():
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    plt.bar(week_days, lessons, label='Количество пар')
    plt.xlabel('День недели')
    plt.ylabel('Число пар')
    plt.title('Количество пар')
    plt.legend()
    plt.show()

flag=0
print("Enter group number")
gr = input()
print("Enter date of monday of week, which schedule you want to see")
date = input()
json_data = req.get(API_BASE+'/faculties').text
transf_json_data = json.loads(json_data)
for j in transf_json_data['faculties']:
    id = str(j['id'])
    API_F = API_BASE + '/faculties' + '/' + id +'/groups'
    json_data1 = req.get(API_F).text
    transf_json_data1 = json.loads(json_data1)
    if schedule(transf_json_data1, date) == 1:
        flag = 1
        break


if flag == 0:
    print('Group did not found')
    exit()
diagramma()