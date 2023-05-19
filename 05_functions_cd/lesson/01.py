# Calendar
def show_month(name, days):
    print(name)
    print()

    for day in days:
        if day < 10:
            day = f'0{day}'

        if (int(day)+1) % 7 == 0:
            print(day)
        else:
            print(day, end=" ")

    print()


def main():
    data = [
        ('January', range(31)),
        ('February', range(28)),
        ('March', range(31)),
        ('April', range(30)),
        ('May', range(31)),
        ('June', range(30)),
        ('July', range(31)),
        ('August', range(31)),
        ('September', range(30)),
        ('October', range(31)),
        ('November', range(30)),
        ('December', range(31)),
    ]

    # for row in data
    for (month_name, month_days) in data:
        # a, b = row
        show_month(month_name, month_days)
        print()

main()