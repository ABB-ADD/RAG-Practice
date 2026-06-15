# RAG 项目模板

一个简单的 RAG (Retrieval-Augmented Generation) 系统实现。

## 项目结构

```
├── src/
│   ├── config.py          # 配置文件
│   ├── data_loader.py     # 数据加载器
│   ├── retriever.py       # 向量检索器
│   ├── llm.py            # LLM 接口
│   └── rag_system.py     # RAG 主系统
├── data/
│   ├── documents/         # 放置你的文档（PDF、TXT）
│   └── vector_store/      # 向量数据库存储
├── main.py               # 主程序入口
├── requirements.txt      # 依赖包
├── .env.example         # 环境变量示例
└── README.md           # 本文件
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env`，并填入你的 OpenAI API Key：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```
OPENAI_API_KEY=sk-your-api-key-here
```

### 3. 放置文档

将你的文档（PDF 或 TXT）放在 `data/documents/` 目录下。

### 4. 构建知识库

在 `main.py` 中取消注释以下行：

```python
rag.build_knowledge_base()
```

然后运行：

```bash
python main.py
```

### 5. 查询

知识库构建完成后，可以直接运行 `main.py` 进行查询：

```bash
python main.py
```

## 配置说明

编辑 `src/config.py` 可以自定义：

- `EMBEDDING_MODEL`: 嵌入模型
- `LLM_MODEL`: 大语言模型
- `CHUNK_SIZE`: 文档分割大小
- `CHUNK_OVERLAP`: 文档块重叠
- `TOP_K`: 检索返回数量

## 主要组件

- **DataLoader**: 加载和分割文档
- **Retriever**: 构建向量索引和检索相关文档
- **LLMClient**: 调用 LLM 生成答案
- **RAGSystem**: 集成所有组件的主系统

## 扩展建议

1. 支持更多文档格式（Word、Markdown等）
2. 实现流式输出
3. 添加对话历史管理
4. 集成不同的向量数据库（Pinecone、Weaviate等）
5. 添加用户界面（Web/CLI）
