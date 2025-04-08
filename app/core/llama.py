from llama_index.core import VectorStoreIndex
from llama_index.core.storage.storage_context import StorageContext
from llama_index.indices.managed.llama_cloud import LlamaCloudIndex
from .config import settings

def get_llama_index():
     return LlamaCloudIndex(
        api_key=settings.llama_cloud_api_key,
        name="cyberAI"
    )
    # storage_context = StorageContext.from_defaults(
    #     vector_store=LlamaCloudIndex(api_key=settings.llama_cloud_api_key)
    # )
    # return VectorStoreIndex.from_vector_store(storage_context.vector_store)
