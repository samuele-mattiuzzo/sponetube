import urlparse

from .conf import SECS_TO_YEARS


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


def strip_video(video_url):
    """
    Removes unwanted elements from a video url and returns
    only the video ID
    """

    url_data = urlparse.urlparse(video_url)
    query = urlparse.parse_qs(url_data.query)
    return query["v"][0]
