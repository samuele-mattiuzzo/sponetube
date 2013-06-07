SECS_TO_YEARS = 60 * 60 * 24 * 31 * 12


def format_plurals(number, string):
    """ Example: format_plurals(10, year)
    returns '10 years' """
    if number > 1:
        string += 's'
        return '%s %s' % (number, string)
    return 'less than 1 year'


def views_to_years(views, length):
    """
    Converts views to solar years for a video.
    Goes with few conventions:
        - 1 month = 30 days
        - 1 year = 12 months
    """

    secs = int(round(float(length) * float(views)))
    years, secs = divmod(secs, SECS_TO_YEARS)

    return format_plurals(years, 'year')
