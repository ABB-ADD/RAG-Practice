
md5_path = "./md5.text"


# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"


# spliter
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_number = 1000        # 文本分割的阈值

#
similarity_threshold = 1            # 检索返回匹配的文档数量

embedding_model_name = "text-embedding-v4"
dashscope_api_key = "sk-ws-H.RPRLDLY.oulA.MEUCIQCbp8ALCwG2DzUY-0aghkvMfh_CGeGZgl44Id-woWJ1RQIgeg2nde6A50TFKVsyQah0YqZWat1_EC8DPwsHHN_mdHw"  # 替换为你的 DashScope API Key
chat_model_name = "qwen3-max"

session_config = {
        "configurable": {
            "session_id": "user_001",
        }
    }
