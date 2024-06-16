import datetime


def date_in_future(days: int) -> datetime.datetime:
    now = datetime.datetime.now()
    format: str = '%d-%m-%Y %H:%M:%S'

    if not isinstance(days, int):
        return now.strftime(format)
    days = datetime.timedelta(days=days)
    return (now + days).strftime(format)


if __name__ == '__main__':
    print(date_in_future([]))
    print(date_in_future(2))
