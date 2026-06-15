import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API 配置
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # 模型配置
    EMBEDDING_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-3.5-turbo"

    # 向量库配置
    VECTOR_STORE_PATH = "data/vector_store"

    # 文档配置
    DOCUMENTS_PATH = "data/documents"

    # Chunk 配置
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    # 检索配置
    TOP_K = 3
