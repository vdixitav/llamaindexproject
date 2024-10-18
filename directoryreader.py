
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import logging
import sys
import asyncio


load_dotenv()

async def main(url:str)->None:
    documents=SimpleDirectoryReader(url).load_data()
    index=VectorStoreIndex.from_documents(documents)
    query_engine=index.as_query_engine()
    response=await query_engine.aquery("what is AI")
    print(response)


if __name__=="__main__":
    # Run the asynchronous main function using asyncio event loop
    asyncio.run(main(url=r"C:\Users\ACER\Desktop\DIXITHA\GENAI"))
    