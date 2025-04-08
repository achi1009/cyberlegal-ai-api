class RAGEngine:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def query(self, prompt: str):
        context_nodes = self.retriever.get_context(prompt)
        context_texts = [node.text for node in context_nodes]
        full_prompt = prompt + "\n\nContext:\n" + "\n".join(context_texts)
        return self.llm.complete(full_prompt).text
