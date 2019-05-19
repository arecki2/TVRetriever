from retrievers.i_retriever import Retriever
import json
import re

class JSONRetriever(Retriever):
    def parse_stream_url(self):
        json_file = json.loads(self.stream_site_url)
        for key in json_file:
            value = json_file[key]
            if "m3u8" in value or "mpd" in value:
                value = value.strip('\"')
                if value.startswith("http"):
                    return value
                else:
                    value = re.sub(r"^(https?)?:?\/\/", "http://", value)
                    return value
            else:
                print(json_file)
                raise ValueError("No valid streaming address found")
