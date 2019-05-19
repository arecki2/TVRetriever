import requests
import json
from retrievers.i_retriever import Retriever


class DailymotionRetriever(Retriever):
    metadataUrlBase = "https://www.dailymotion.com/player/metadata/video/"

    def parse_stream_url(self):
        stream_id = self.get_video_id()
        metadata_url = self.get_metadata_url(stream_id)
        json_metadata = self.get_metadata_json(metadata_url)
        stream_url = self.parse_stream_url_from_json(json_metadata)
        return stream_url.strip('\"')

    def is_link_to_video(self):
        return '/video/' in self.stream_site_url

    def get_video_id(self):
        if not self.is_link_to_video():
            raise ValueError(self.stream_site_url + ": The link supplied does not point to a video")
        id_with_args = self.stream_site_url.split('/')[-1]
        proper_id = id_with_args.split('?')[0]
        return proper_id

    def get_metadata_url(self, stream_id):
        return self.metadataUrlBase + stream_id

    def get_metadata_json(self, metadata_url):
        r = requests.get(metadata_url)
        return r.text

    def parse_stream_url_from_json(self, jsonfile):
        data = json.loads(jsonfile)
        return data['qualities']['auto'][0]['url']

