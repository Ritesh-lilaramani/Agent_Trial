from huggingface_hub import login
login ()   # Past my_agent token at hugging face

from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# # Load  data (replace with  file path)
# loader = TextLoader("")
# documents = loader.load()
#
# # Split into manageable chunks
# splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# docs_processed = splitter.split_documents(documents)


# Initialize the agent with web search tool and default LLM
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=InferenceClientModel()  # Uses Qwen/Qwen2.5-Coder-32B-Instruct by default
)

# Run the agent
response = agent.run("Imagine you are Ai researcher and explain your views on hinduism")
print(response)
