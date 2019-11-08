from retrievers.i_retriever import Retriever


class MPDRetriever(Retriever):
    def parse_stream_url(self):
        return self.stream_site_url
