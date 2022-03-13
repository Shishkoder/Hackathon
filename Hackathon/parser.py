"""Данный скрипт обеспечивает парсинг расписания с сайта "https://kai.ru/raspisanie".
И отбирает информацию об аудитории(какая группа, во сколько пара и пр.), если она занята.
Иначе говорит, что свободна.

:requests.get, post: Для запроса с сервера с GET- и POST-запросами соответственно.
:json.dump, load, loads: Для сохранения в JSON-файл.
:bs4.BeautifulSoup: Для парсинга сайта.

"""
from json import dump, load, loads

from requests import get, post
from bs4 import BeautifulSoup


# Константы
FIRST_URL = "https://kai.ru/raspisanie?p_p_id=" \
            "pubStudentSchedule_WAR_publicStudentSchedule10&p_p_lifecycle=" \
            "2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getGroupsURL&p_p_cacheability=" \
            "cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&query="
SECOND_URL = "https://kai.ru/raspisanie?p_p_id=" \
             "pubStudentSchedule_WAR_publicStudentSchedule10&p_p_lifecycle=" \
             "2&p_p_state=normal&p_p_mode=view&p_p_resource_id=schedule&p_p_cacheability=" \
             "cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1"

# Для обхода DDoS-защиты
HEADERS_DICT = {'Accept': '*/*',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) '
                              'Gecko/20100101 Firefox/98.0'}


def parse_schedule():
    """ВНИМАНИЕ!!!
    ЗАДЕЙСТОВАТЬ ЭТУ ФУНКЦИЮ В РУЧНУЮ ТОЛЬКО В ТОМ СЛУЧАЕ,
    ЕСЛИ БОТ ПО КАКИМ-ЛИБО ПРИЧИНАМ НУЖНО ПЕРЕЗАПУСТИТЬ И СФОРМИРОВАТЬ ФАЙЛ СО ВСЕМИ ГРУППАМИ!!!
    ВНИМАНИЕ!!!

    """
    # Достаём ID всех групп
    get_all_groups = get(FIRST_URL, headers=HEADERS_DICT)
    soup = BeautifulSoup(get_all_groups.text, "lxml")
    all_groups_raw = soup.find("body").text
    all_groups_list = loads(all_groups_raw)

    classroom_dict = {
        "1": {},
        "2": {},
        "3": {},
        "4": {},
        "5": {},
        "6": {}
    }

    for group in all_groups_list:
        get_group_id = post(SECOND_URL, data={"groupId": group["id"]})
        soup_group = BeautifulSoup(get_group_id.text, 'lxml')
        group_dict = loads(soup_group.text)



        for key, value in group_dict.items():
            for value_list in value:
                if group["group"] not in classroom_dict[key].keys():
                    classroom_dict[key].update({group["group"]: {
                        "id": group["id"],
                        "classroom": []  # Если не работает, ставим [{}]
                    }})
                classroom_dict[key][group["group"]]['classroom'].append({
                    value_list['audNum'].strip(): {
                        'time': value_list['dayTime'].strip(),
                        'prepodName': value_list['prepodName'].strip(),
                        'discipline': value_list['disciplName'],
                        'buildNum': value_list['buildNum'].strip(),
                        'thread': value_list['potok'],
                        'dayDate': value_list['dayDate'].strip()
                    }
                })
    with open("result/dern/data.json", 'w', encoding='utf-8') as group_json:
        dump(classroom_dict, group_json, indent=4, ensure_ascii=False)

    print(classroom_dict)
    # Тестовое получение запроса для группы № 4112
    # get_group_id = get(FIRST_URL + "4112")
    # soup = BeautifulSoup(get_group_id.text, "lxml")
    #
    # content_raw = soup.find("body").text
    # content = content_raw.replace('[', '').replace(']', '')
    # json_data = json.loads(content)
    #
    # get_rasp = post(SECOND_URL, data={'groupId': json_data['id']})
    # css = BeautifulSoup(get_rasp.text, 'lxml')
    # test = dict(json.loads(css.text))
    # for i, j in test.items():
    #     print(i, j)
    # if css.text != '{}':
    #     # with open("result/tt.txt", mode='w', encoding='utf-8') as file:
    #     #     file.write(css.text)
    #     pass


def get_classroom(week_number, build_number, classroom="КСК КАИ ОЛИМП"):
    classroom_dict = {}
    result = ""
    with open("result/dern/data.json", 'r', encoding='utf-8') as reader:
        json_objects = load(reader)
        try:
            for key_group, value_classroom in json_objects[week_number].items():
                for value_classes in value_classroom['classroom']:
                    try:
                        if classroom in value_classes.keys():
                            classroom_dict[key_group].append(value_classes)
                    except KeyError:
                        classroom_dict.update({key_group: [value_classes]})
                        continue
        except KeyError:
            result = "Да не мороси!"

    if classroom_dict:
        result = ""
        for key, value_list in classroom_dict.items():
            for value in value_list:
                for par, data in value.items():
                    try:
                        if data['dayDate'] == '':
                            data['dayDate'] = "чет/неч"
                        # else:
                        #     data = value[classroom]['dayDate']
                        if data['buildNum'] == build_number:
                            result += f"Занята группой: {key}, дисциплина: {data['discipline']}, дата: {data['dayDate']}," \
                                      f" время: {data['time']}, преподаватель: {data['prepodName']}\n\n"
                    except KeyError:
                        continue

        if not result:
            return "Свободно!"
        else:
            return result
    elif result == "Да не мороси!":
        return result
    else:
        return "Свободно!"


# Test -----------------------
# print(get_classroom('2', '3', '406'), end='')
# print(get_classroom('3', '2', '309'), end='')
# print(get_classroom('3', '6', '930'), end='')
