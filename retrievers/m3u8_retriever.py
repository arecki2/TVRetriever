from retrievers.i_retriever import Retriever


class M3U8Retriever(Retriever):
    def parse_stream_url(self):
        return self.stream_site_url
