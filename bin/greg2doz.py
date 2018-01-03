#!/usr/bin/env python

import click

from dozenal import iso2doz


@click.command()
@click.argument('iso_date_str')
def main(iso_date_str):
    print(iso2doz(iso_date_str))


if __name__ == '__main__':
    main()
