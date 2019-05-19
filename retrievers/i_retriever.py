class Retriever:
    def __init__(self, stream_site_url):
        self.stream_site_url = stream_site_url

    def parse_stream_url(self):
        raise NotImplementedError("Retriever not found for this stream")
