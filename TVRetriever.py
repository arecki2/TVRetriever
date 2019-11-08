import subprocess
from retrievers.dailymotion_retriever import DailymotionRetriever
from retrievers.m3u8_retriever import M3U8Retriever
from retrievers.mpd_retriever import MPDRetriever
from retrievers.tvibo_retriever import JSONRetriever
import tldextract
import json
import argparse

def set_player():
    config_file_path = ".\\config\\config.json"
    with open(config_file_path, 'r') as c:
        content = json.load(c)
        print(content["selected_player"])
        selected_player = content["selected_player"]
        print(content["players"][selected_player])
        return content["players"][selected_player]["name"], content["players"][selected_player]["path"]

def choose_retriever(stream_source_url):
    retriever = None
    if "m3u8" in stream_source_url:
        retriever = M3U8Retriever(stream_source_url)
    elif "mpd" in stream_source_url:
        retriever = MPDRetriever(stream_source_url)
    elif "pilot.wp" in stream_source_url:
        pass
    else:
        retriever = get_retriever_for_hostname(stream_source_url)
    return retriever

def get_retriever_for_hostname(stream_source_url):
    ext = tldextract.extract(stream_source_url)
    domain = ext.domain
    class_name = domain.capitalize() + "Retriever"
    return eval(class_name)(stream_source_url)

run_vlc_command = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
run_potplayer_command = "C:\\Program Files\\DAUM\\PotPlayer\\potplayermini64.exe \%1 \/add"

player_name, player_path = set_player()

parser = argparse.ArgumentParser()
parser.add_argument('url_arg', help="A URL of the video to play.")
args = parser.parse_args()
video_url = args.url_arg

#cnews_stream_url = "https://www.dailymotion.com/video/x3b68jn?playlist=x61esx"
#tadeusz_rydzyk_wam = "https://trwamtv.live.rd.insyscd.net/cl01/out/u/trwam.mpd"

stream_retriever = choose_retriever(video_url)

try:
    stream_url = stream_retriever.parse_stream_url()
    subprocess.call(player_path + " " + stream_url)
except NotImplementedError:
    print("For now, try watching the stream manually.")
except OSError:
    print("{0} not found.".format(player_name))
else:
    print("Something else is wrong")
