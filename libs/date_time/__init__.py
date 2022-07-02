from datetime import datetime, timedelta, timezone


def current_datetime():
    return datetime.now()


def current_datetime_with_tz():
    return datetime.now().astimezone()


def current_datetime_with_utc_tz():
    return datetime.now().astimezone(timezone.utc)


def current_date_utc():
    return datetime.now() - timedelta(hours=7)


def get_datetime_from_timestamp(timestamp):
    date = datetime.fromtimestamp(timestamp / 1e3)
    return date - timedelta(hours=7)


def get_string_datetime_from_timestamp(timestamp, format):
    date = get_datetime_from_timestamp(timestamp)
    return date.strftime(format)


def get_string_datetime(date, format):
    return date.strftime(format)


def get_datetime_from_string(date, format):
    return datetime.strptime(date, format)


def get_datetime_delta_now(no_of_day):
    now = current_date_utc()
    return now - timedelta(days=no_of_day)


def get_datetime_delta_date(date, delta):
    return date + timedelta(days=delta)


def convert_to_another_timezone(date, delta):
    converted = date + timedelta(hours=delta)
    return converted.astimezone()


def get_start_of_date(date, set_tz=False):
    if set_tz:
        return datetime(year=date.year, month=date.month, day=date.day, hour=0, second=0).astimezone()
    return datetime(year=date.year, month=date.month, day=date.day, hour=0, second=0)


def set_current_timezone(date):
    # tz = timezone(timedelta(hours=7))
    # return date.astimezone(tz)
    return date.astimezone()


def get_datetime_delta_second(date, delta):
    return date + timedelta(seconds=delta)


def get_start_of_hour(date, set_tz=False):
    if set_tz:
        return datetime(year=date.year, month=date.month, day=date.day, hour=date.hour, second=0).astimezone()
    return datetime(year=date.year, month=date.month, day=date.day, hour=date.hour, second=0)
