import datetime


def solution1(a, b):
    answer = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0

    for i in range(a - 1):
        result += day[month[i] - 1]
    result += b

    return answer[(result % 7) - 1]


def solution2(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[datetime.date(2016, a, b).weekday()]


a = 5
b = 14

print(solution1(a, b))
print(solution2(a, b))
