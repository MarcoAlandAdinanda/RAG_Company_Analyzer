# Embedding model builder
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor


def set_embed_model(model_name: str,
                    chunk_size: int = 256,
                    chunk_overlap: int = 25) -> None:
    """Sets the embedding model and related settings.

    Args:
        model_name (str): Name of the HuggingFace embedding model.
        chunk_size (int, optional): Size of text chunks for embedding. Defaults to 256.
        chunk_overlap (int, optional): Overlap size between chunks. Defaults to 25.
    """
    Settings.llm = None
    Settings.embed_model = HuggingFaceEmbedding(model_name=model_name)
    Settings.chunk_size = chunk_size
    Settings.chunk_overlap = chunk_overlap


class RAGModule:
    """Retrieval-Augmented Generation (RAG) module for querying and generating responses.

    Attributes:
        top_k (int): Number of top similar documents to retrieve.
        query_engine (RetrieverQueryEngine): Engine to query the retriever with postprocessing.
    """

    def __init__(self,
                 llm_model: str = "MarcoAland/llama3.1-rag-indo",
                 embedding_model: str = "MarcoAland/Indo-bge-m3",
                 docs_path: str = "data",
                 top_k: int = 3,
                 similarity_cutoff: float = 0.5):
        """Initializes the RAGModule with specified parameters.

        Args:
            llm_model (str, optional): Name of the language model. Defaults to "MarcoAland/llama3.1-rag-indo".
            embedding_model (str, optional): Name of the embedding model. Defaults to "MarcoAland/Indo-bge-m3".
            docs_path (str, optional): Path to the documents directory. Defaults to "data".
            top_k (int, optional): Number of top similar documents to retrieve. Defaults to 3.
            similarity_cutoff (float, optional): Cutoff similarity score for postprocessing. Defaults to 0.5.
        """

        # Define the embedding model
        set_embed_model(model_name=embedding_model)

        # Load documents and build the vector store index
        documents = SimpleDirectoryReader(docs_path).load_data()
        index = VectorStoreIndex.from_documents(documents)
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=top_k,
        )

        # Store parameters and create a query engine
        self.top_k = top_k
        self.query_engine = RetrieverQueryEngine(
            retriever=retriever,
            node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=similarity_cutoff)]
        )

    def format_context(self, response) -> str:
        """Formats the context from retrieved documents.

        Args:
            response: The response object containing retrieved documents.

        Returns:
            str: Formatted context string.
        """
        context = "Context:\n"
        for i in range(self.top_k):
            context += response.source_nodes[i].text + "\n\n"
        return context

    def query(self, query: str) -> str:
        """Queries the engine and retrieves the context.

        Args:
            query (str): The query string.

        Returns:
            str: The formatted context string if successful, empty string otherwise.
        """
        try:
            response = self.query_engine.query(query)
            context = self.format_context(response)
            return context
        except Exception as e:
            # Log the error message if necessary
            return ""

    def prompt(self, context: str, instruction: str) -> str:
        """Generates a prompt with the given context and instruction.

        Args:
            context (str): The context string.
            instruction (str): The instruction to be added to the prompt.

        Returns:
            str: The final prompt string.
        """
        return f"{context}\n ### Instruksi:\n {instruction}"

    def main(self, instruction: str) -> str:
        """Main method to generate a prompt from a given instruction.

        Args:
            instruction (str): The instruction string.

        Returns:
            str: The generated prompt string.
        """
        context = self.query(query=instruction)
        prompt = self.prompt(context=context, instruction=instruction)
        return prompt
