# Imports
import datetime

# Header
print('----------------------------\n      Guess the number\n----------------------------\n')


def get_birthday_from_user():
    print('When were you born ?')
    year = input('Year? (YYYY) ')
    month = input('Month? (MM) ')
    day = input('Day? (DD) ')
    birthday = datetime.date(int(year), int(month), int(day))

    # check = input('Is this correct ? {} (Y/N) : '.format(birthday))
    # if check == "Y":
    #     print('So you are born on {}/{}/{}...'.format(day, month, year))
    #     return birthday


def days_between_two_dates(birthday, today):
    this_year = datetime.date(today.year, birthday.month, birthday.day)
    dt = this_year - today
    age = today.year - birthday.year
    if dt.days > -1:
        age -= 1
    print('You are {} years old'.format(age))
    return dt.days


def print_bday_infos(days):
    if days > 1:
        print("{} days left before your birthday !".format(days))
        return
    elif days == 1:
        print("It's your birthday tomorrow !")
        return
    elif days == 0:
        print("Happy birthday !")
        return
    else:
        print("Your birthday was {} days ago".format(-days))
        return


def main():
    bday = get_birthday_from_user()
    now = datetime.date.today()
    num_of_days = days_between_two_dates(bday, now)
    print_bday_infos(num_of_days)

    return


main()