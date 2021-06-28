from datetime import datetime

from croniter import croniter_range


def list_timestamps_between(start, end, cron_string):
    """
    Get timestamps between start and end where cron should fire,
    based upon cron_string.
    """
    return croniter_range(start, end, cron_string)


def main():
    """
    Here lies the body of the CLI script.
    """

    # FIXME
    #   * get args from sys.argv
    #   * timezone support?

    start = datetime(2021, 1, 1)
    end = datetime(2021, 12, 31)
    for stamp in list_timestamps_between(start, end, '00 12 14 * *'):
        print(stamp)
