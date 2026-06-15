from src.rag_system import RAGSystem

def main():
    # 初始化RAG系统
    rag = RAGSystem()

    # 构建知识库（首次使用）
    # rag.build_knowledge_base()

    # 查询示例
    questions = [
        "这个文档主要讲了什么？",
        "如何使用这个系统？",
    ]

    for question in questions:
        result = rag.query(question)
        print(f"答案: {result['answer']}\n")

if __name__ == "__main__":
    main()
