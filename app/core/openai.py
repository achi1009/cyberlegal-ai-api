from llama_index.llms.openai import OpenAI
from .config import settings

def get_openai_llm():
    return OpenAI(api_key=settings.openai_api_key)
