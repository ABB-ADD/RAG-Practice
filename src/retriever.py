from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from src.config import Config

class Retriever:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )
        self.vector_store = None

    def build_index(self, documents):
        """构建向量索引"""
        self.vector_store = Chroma.from_documents(
            documents,
            self.embeddings,
            persist_directory=Config.VECTOR_STORE_PATH
        )
        self.vector_store.persist()
        print(f"向量索引已构建，共 {len(documents)} 个文档")

    def load_index(self):
        """加载已有的向量索引"""
        self.vector_store = Chroma(
            embedding_function=self.embeddings,
            persist_directory=Config.VECTOR_STORE_PATH
        )

    def retrieve(self, query: str, top_k: int = None):
        """检索相关文档"""
        if self.vector_store is None:
            self.load_index()

        if top_k is None:
            top_k = Config.TOP_K

        results = self.vector_store.similarity_search(query, k=top_k)
        return results
