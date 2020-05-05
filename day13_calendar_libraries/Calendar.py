import calendar


def calendarExamples():
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2020, 4)
    print(st)

    for name in calendar.month_name:
        print(name)


if __name__ == "__main__":
    calendarExamples()
