from __future__ import unicode_literals
from retrievers.i_retriever import Retriever
import re
import youtube_dl

class YouTubeRetriever(Retriever):
    def parse_stream_url(self):
        link_type = self.check_type_of_link()
        if link_type == "video":
            # both VLC and PotPlayer are able to parse the video on their own ...
            return self.stream_site_url
        else:
            # ... unless the links are like /channel/<channel_id>/live
            ydl_opts = {
                'playlist_items': 0,
                'forceid': 'true',
                'simulate': 'true'
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                video_id = ydl.download([self.stream_site_url])
                return "https://www.youtube.com/watch?v=" + video_id


    def check_type_of_link(self):
        direct_video_link_pattern = "https://www.youtube.com/watch?v=[A-Za-z0-9-_]+"
        channel_live_link_pattern = "https://www.youtube.com/channel/[A-Za-z0-9-_]/live"
        x = re.match(direct_video_link_pattern, self.stream_site_url)
        if x is not None:
            return "video"
        x = re.match(channel_live_link_pattern, self.stream_site_url)
        if x is not None:
            return "channel"
        return "unknown"

run_vlc_command = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
test_stream_direct = "https://www.youtube.com/watch?v=GTthea0TEKU"
test_stream_channel = "https://www.youtube.com/channel/UCvufartoVu2ScVS7R6TsB6A/live"
retriever = YouTubeRetriever(test_stream_channel)
try:
    stream_url = retriever.parse_stream_url()
    subprocess.call(run_vlc_command + " " + stream_url)
except NotImplementedError:
    print("For now, try watching the stream manually.")
except OSError:
    print("VLC not found.")
else:
    print("Something else is wrong")