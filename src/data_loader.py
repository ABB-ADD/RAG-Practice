from pathlib import Path
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.config import Config

class DataLoader:
    def __init__(self):
        self.chunk_size = Config.CHUNK_SIZE
        self.chunk_overlap = Config.CHUNK_OVERLAP
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )

    def load_documents(self, doc_path: str = None):
        """加载文档"""
        if doc_path is None:
            doc_path = Config.DOCUMENTS_PATH

        documents = []
        path = Path(doc_path)

        if not path.exists():
            print(f"文档路径不存在: {doc_path}")
            return documents

        # 加载PDF文件
        for pdf_file in path.glob("*.pdf"):
            loader = PyPDFLoader(str(pdf_file))
            documents.extend(loader.load())

        # 加载TXT文件
        for txt_file in path.glob("*.txt"):
            loader = TextLoader(str(txt_file))
            documents.extend(loader.load())

        return documents

    def split_documents(self, documents):
        """分割文档"""
        return self.splitter.split_documents(documents)
