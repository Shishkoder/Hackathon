# Hackathon

# Что делает программа:
1. Быстрое получение ответа на запрос пользователя о том, свободна ли аудитория. 
2. Если аудитория занята, то выводит данные о том, какой группой она занята, по какой дисциплине у них проходит пара, со скольких и у какого преподавателя. Эти данные чистятся от лишних пробелов, дефисов и других лишних символов.


# Ссылка на GET запрос, где в параметр "query=" передаётся число - номер группы. В нём хранятся данные о номере группы, её форме обучения и ID группы, который необходим для получения расписания группы.
https://kai.ru/raspisanie?p_p_id=pubStudentSchedule_WAR_publicStudentSchedule10&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=getGroupsURL&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&query=
# Ссылка на POST запрос, где передаётся ID группы и вытягивается json с расписанием этой группы.
https://kai.ru/raspisanie?p_p_id=pubStudentSchedule_WAR_publicStudentSchedule10&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=schedule&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1
