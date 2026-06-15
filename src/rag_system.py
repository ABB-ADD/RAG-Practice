from src.data_loader import DataLoader
from src.retriever import Retriever
from src.llm import LLMClient

class RAGSystem:
    def __init__(self):
        self.data_loader = DataLoader()
        self.retriever = Retriever()
        self.llm = LLMClient()

    def build_knowledge_base(self):
        """构建知识库"""
        print("开始加载文档...")
        documents = self.data_loader.load_documents()

        if not documents:
            print("未找到文档")
            return

        print(f"已加载 {len(documents)} 个文档")

        print("开始分割文档...")
        split_docs = self.data_loader.split_documents(documents)
        print(f"已分割为 {len(split_docs)} 个块")

        print("开始构建向量索引...")
        self.retriever.build_index(split_docs)
        print("知识库构建完成")

    def query(self, question: str) -> dict:
        """查询问题"""
        print(f"\n问题: {question}")

        # 检索相关文档
        retrieved_docs = self.retriever.retrieve(question)

        if not retrieved_docs:
            return {
                "question": question,
                "answer": "未找到相关信息",
                "sources": []
            }

        # 构建上下文
        context = "\n".join([doc.page_content for doc in retrieved_docs])

        # 生成答案
        answer = self.llm.generate_answer(question, context)

        return {
            "question": question,
            "answer": answer,
            "sources": [doc.metadata for doc in retrieved_docs]
        }
