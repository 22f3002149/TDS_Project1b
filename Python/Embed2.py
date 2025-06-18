import hashlib
import httpx
import json
import os
import time
import numpy as np
from pathlib import Path
from tqdm import tqdm
import google.generativeai as genai
#from google import genai
from semantic_text_splitter import MarkdownSplitter
from openai import OpenAI

# Get chunks from a file, splitting the content into manageable pieces.
def get_chunks(file_path: str, chunk_size: int = 3000):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    _overlap = 100
    splitter = MarkdownSplitter(chunk_size, overlap=_overlap)
    #splitter = MarkdownSplitter(chunk_size)
    chunks = splitter.chunks(content)
    return chunks

# Get embeddings for a given text using OpenAI API.
def get_embeddings(text: str) -> list:
    """ Get embeddings for a given text using OpenAI API. """
    client = OpenAI()
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    embedding = response.data[0].embedding
    return embedding

def get_embeddings2(text: str) -> list:
    return "**********************************"

"""
def get_embedding(text: str, max_retries: int = 3) -> list[float]:
    #Get embedding for text chunk with rate limiting and retry logic
    client = genai.Client(api_key=os.environ.get("GENAI_API_KEY"))

    for attempt in range(max_retries):
        try:
            # Apply rate limiting
            rate_limiter.wait_if_needed()

            result = client.models.embed_content(
                model="gemini-embedding-exp-03-07",
                contents=text
            )

            embedding = result.embeddings[0].values
            return embedding

        except Exception as e:
    if "rate limit" in str(e).lower() or "quota" in str(e).lower():
        # Exponential backoff for rate limit errors
        wait_time = 2 ** attempt
        print(f"Rate limit hit, waiting {wait_time} seconds...")
        time.sleep(wait_time)
    elif attempt == max_retries - 1:
        print(f"Failed to get embedding after {max_retries} attempts: {e}")
        raise
    else:
        print(f"Attempt {attempt + 1} failed: {e}, retrying...")
        time.sleep(1)
"""

# Create chunks for all files in '03a_FunalMds' directory
if __name__ == "__main__":
    # get all makrdown files stored in the '03a_FinalMds' directory and its subdirectories
    files = list(Path("04a_FinalMds").rglob("*.md"))
#    files = [Path("markdowns").glob("*.md"), Path("markdowns").rglob("*.md")]
    all_chunks = []
    all_embeddings = []
    total_chunks = 0
    file_chunks = {}

    # Getting chunks from all markdown files and store in file_chunks with file_path as key
    for file_path in files:
        chunks = get_chunks(file_path)
        file_chunks[file_path] = chunks
        total_chunks += len(chunks)

    # for the chunks get embeddings and store them in all_embeddings
    with tqdm(total=total_chunks, desc="Processing embeddings") as pbar:
        for file_path, chunks in file_chunks.items():
            print(f"Processing file: {file_path} with {len(chunks)} chunks")
            for chunk in chunks:
                try:
                    # Process the chunk: get embedding and append to all_embeddings
                    embedding = get_embeddings(chunk)
                    time.sleep(0.5)  # Pause for 1 second to avoid rate limiting
                    all_embeddings.append(embedding)
                    all_chunks.append(chunk)
                    pbar.update(1)
                except Exception as e:
                    print(f"Error processing chunk: {e}")
                    pbar.update(1)
                    continue

np.savez("embeddings3.npz", chunks=all_chunks, embeddings=all_embeddings)


"""
file_path = ("markdowns/Contribute1.md")
chunks = get_chunks(file_path, chunk_size=1000)
embedding = get_embedding(chunks[0])
print(len(embedding))


file_path = "test/archive.md"
chunks = get_chunks(file_path)
em = get_embeddings(chunks[3])

print(f"Number of chunks: {len(chunks)}")
print(f"First chunk: {chunks[3]}")
print(len(em))
print(f"Embedding for the chunk: {em}")  
"""