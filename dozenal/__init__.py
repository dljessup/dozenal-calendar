#!/usr/bin/env python

from datetime import date


def dozenal_digit(n):
    if type(n) != int or n < 0 or 12 <= n:
        raise ValueError('Invalid dozenal digit: {}'.format(n))
    if n < 10:
        return str(n)
    return {10: 'ᘔ', 11: 'Ɛ'}[n]


def dozenal_str(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(dozenal_digit(n % 12))
        n //= 12
    return ''.join(digits[::-1])


def get_prev_dozenal_new_year(greg_date):
    solstices = {
        2017: (date(2016, 12, 21), '6901'),
        2018: (date(2017, 12, 21), '6902'),
        2019: (date(2017, 12, 21), '6903'),
    }
    if solstices[greg_date.year + 1][0] <= greg_date:
        return solstices[greg_date.year + 1]
    return solstices[greg_date.year]


def days2doz(days_diff):
    bimonth, bimonth_day = divmod(days_diff, 61)
    semibimonth, day = (0, bimonth_day) if bimonth_day < 30 else (1, bimonth_day - 30)
    month = 2 * bimonth + semibimonth
    return '{}-{}'.format(dozenal_str(month), dozenal_str(day).rjust(2, '0'))


def iso2doz(iso_date_str):
    greg_year_str, greg_month_str, greg_day_str = iso_date_str.split('-')
    greg_date = date(int(greg_year_str), int(greg_month_str), int(greg_day_str))
    prev_new_year, doz_year = get_prev_dozenal_new_year(greg_date)
    days_diff = (greg_date - prev_new_year).days
    return '{}-{}'.format(doz_year, days2doz(days_diff))
