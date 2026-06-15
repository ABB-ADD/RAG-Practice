from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.config import Config

class LLMClient:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=Config.LLM_MODEL,
            openai_api_key=Config.OPENAI_API_KEY,
            temperature=0.7,
        )

    def generate_answer(self, query: str, context: str) -> str:
        """根据检索上下文生成答案"""
        prompt = ChatPromptTemplate.from_template(
            """基于以下上下文回答问题。如果上下文中没有相关信息，请说明。

上下文：
{context}

问题：{question}

答案："""
        )

        chain = prompt | self.llm
        response = chain.invoke({
            "context": context,
            "question": query
        })

        return response.content
