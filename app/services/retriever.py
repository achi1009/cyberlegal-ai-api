class Retriever:
    def __init__(self, index):
        self.retriever = index.as_retriever()

    def get_context(self, query: str):
        return self.retriever.retrieve(query)
