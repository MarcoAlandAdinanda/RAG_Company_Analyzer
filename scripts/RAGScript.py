# LLM model builder
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

# Embedding model builder
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

# Initialize
# def set_llm_model(model_name: str = "MarcoAland/llama3.1-rag-indo"):
#     return Ollama(model=model_name)

def set_embed_model(model_name: str,
                    chunk_size: int = 256,
                    chunk_overlap: int = 25) -> None:
    Settings.llm = None
    Settings.embed_model = HuggingFaceEmbedding(model_name=model_name)
    Settings.chunk_size = chunk_size
    Settings.chunk_overlap = chunk_overlap


class RAGModule:
    def __init__(self,
                 llm_model: str = "MarcoAland/llama3.1-rag-indo",
                 embedding_model: str = "MarcoAland/Indo-bge-m3",
                 docs_path: str = "data",
                 top_k: int = 3,
                 similarity_cutoff: float = 0.3):
        
        # Define embedding model
        set_embed_model(model_name=embedding_model)

        # Define llm model in Settings module
        # self.llm_model = set_llm_model(model_name=llm_model)

        # Set vector DB
        documents = SimpleDirectoryReader(docs_path).load_data()
        index = VectorStoreIndex.from_documents(documents)
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=top_k,
        )

        self.top_k = top_k
        self.query_engine = RetrieverQueryEngine(
            retriever=retriever,
            node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=similarity_cutoff)]
        )

    def format_context(self, response):
        context = "Context:\n"
        for i in range(self.top_k):
            context += response.source_nodes[i].text + "\n\n"
        return context
    
    def query(self, query: str):
        try:
            response = self.query_engine.query(query)
            context = self.format_context(response)
            return context
        except:
            return ""

    def prompt(self, context: str, instruction: str):
        return f"{context}\n ### Instruksi:\n {instruction}"

        # Create the messages list
        messages = [ChatMessage(role="user", content=prompt_message)]
        
        # Get the model response
        response = self.llm_model.stream_chat(messages)
        # Collect and return the response
        response_text = ""
        for r in response:
            response_text += r.delta
        
        return response_text

    def main(self, instruction: str):
        context = self.query(query=instruction)
        prompt = self.prompt(context=context, instruction=instruction)
        # print(prompt)
        return prompt