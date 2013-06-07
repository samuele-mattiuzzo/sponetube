import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine

from .utils import views_to_years


def get_video_info(videoID='9bZkp7q19f0'):
    # default video: Gangnam Style

    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    gdata.alt.appengine.run_on_appengine(yt_service)

    video = yt_service.GetYouTubeVideoEntry(video_id=videoID)

    if isinstance(video.media.title.text, str):
        video_title = unicode(video.media.title.text, 'utf-8')
    else:
        video_title = unicode(video.media.title.text)

    # stuff we need: title, views, length
    return {
        'length': video.media.duration.seconds,
        'title': video_title,
        'views': video.statistics.view_count,
        'thumbnail': video.media.thumbnail[0].url,
        'ytm': views_to_years(
            video.statistics.view_count, video.media.duration.seconds
        )
    }
