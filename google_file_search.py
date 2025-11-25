import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("google_aistudio_api_key"))
store = client.file_search_stores.create()

upload_op = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=store.name,
    file='file-name.pdf' # this setup uses a file as knowledgebase. Add file path here.
)

while not upload_op.done:
    time.sleep(5)
    upload_op = client.operations.get(upload_op)

# Use the file search store as a tool in generation call
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='show me the key points on this document',
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=[store.name]
            )
        )]
    )
)
print(response.text)

# Support response with links to the grounding sources.
grounding = response.candidates[0].grounding_metadata
if not grounding:
  print('No grounding sources found')
else:
    sources = {c.retrieved_context.title for c in grounding.grounding_chunks}
    print('Sources:', *sources)