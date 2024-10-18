from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv
import tracemalloc
import asyncio  # To manage the event loop

# Start tracing Python memory allocations
tracemalloc.start()

load_dotenv()

async def main(url: str) -> None:
    # Fetch the webpage and create the index
    document = SimpleWebPageReader(html_to_text=True).load_data([url])
    index = VectorStoreIndex.from_documents(documents=document)
    
    print(index)
    
    # Create the query engine
    query_engine = index.as_query_engine()
    
    print(query_engine)
    
    # Asynchronously query the engine
    response = await query_engine.aquery("Real-world Examples of AI Applications")  # Use await to wait for the coroutine
    print("res==>", response)

if __name__ == "__main__":
    # Run the async main function using asyncio event loop
    asyncio.run(main(url="https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d"))
