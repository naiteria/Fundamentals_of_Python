def total_hours(any_list):
    hours = []
    for i in any_list:
        if '(л)' in i:
            hours.append(int(i.replace('(л)', '')))
        elif '(пр)' in i:
            hours.append(int(i.replace('(пр)', '')))
        elif '(лаб)' in i:
            hours.append(int(i.replace('(лаб)', '')))
        else:
            continue
    return sum(hours)


school_subjects = {}

with open('Task5.6.txt', encoding='utf-8') as text:
    my_list = [line.split() for line in text]
    counter = 0
    while counter != len(my_list):
        school_subjects[my_list[counter][0].replace(':', '')] = total_hours(my_list[counter])
        counter += 1
    print(f'Общее количество занятий по предметам: {school_subjects}')
