import subprocess
from retrievers.i_retriever import Retriever
from retrievers.dailymotion_retriever import DailymotionRetriever
from retrievers.m3u8_retriever import M3U8Retriever
from retrievers.tvibo_retriever import JSONRetriever
import tldextract

def choose_retriever(stream_source_url):
    retriever = None
    if "m3u8" in stream_source_url:
        retriever = M3U8Retriever(stream_source_url)
    else:
        retriever = get_retriever_for_hostname(stream_source_url)
    return retriever

def get_retriever_for_hostname(stream_source_url):
    ext = tldextract.extract(stream_source_url)
    domain = ext.domain
    class_name = domain.capitalize() + "Retriever"
    return eval(class_name)(stream_source_url)

run_vlc_command = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
run_potplayer_command = "C:\\Program Files\\DAUM\\PotPlayer\\potplayer.exe /add"

cnews_stream_url = "https://www.dailymotion.com/video/x3b68jn?playlist=x61esx"
tadeusz_rydzyk_wam = "http://trwamtv.live.e55-po.insyscd.net/trwamtv2.smil/chunklist_b950000.m3u8"

stream_retriever = choose_retriever(tadeusz_rydzyk_wam)

try:
    stream_url = stream_retriever.parse_stream_url()
    subprocess.call(run_vlc_command + " " + stream_url)
except NotImplementedError:
    print("For now, try watching the stream manually.")
except OSError:
    print("VLC not found.")
else:
    print("Something else is wrong")
