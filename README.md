# Google File Search with Gemini API

This project demonstrates how to use the Google Gemini API's File Search capability to generate content based on a provided document. It uploads a file to a File Search Store and then uses a Gemini model to extract key points from the document.

## Features

-   Uploads a local file (not limited to PDF) to a Google File Search Store.
-   Uses the `gemini-2.5-flash` model to generate a summary or key points from the uploaded document.
-   Provides grounding sources (links to the document) for the generated content.

## Supported File Types

This program accepts multiple file types, not just PDFs. For a full list of supported file types, see the [Gemini API documentation](https://ai.google.dev/gemini-api/docs/file-search#text).

## Setup

Follow these steps to set up and run the project:

### 1. Prerequisites

-   Python 3.8+
-   A Google Cloud Project with the Gemini API enabled.
-   An API key for the Google Gemini API.

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install google-generativeai python-dotenv
```

### 3. Configure API Key

Create a file named `.env` in the root directory of your project (the same directory as `google_file_search.py`) and add your Google API key:

```
google_aistudio_api_key="your_google_aistudio_api_key"
```
Replace `your_google_aistudio_api_key` with your actual API key.

### 4. Add Your Document

Place the file you want to analyze in the same directory as `google_file_search.py`. Make sure to update the `file` parameter in `google_file_search.py` to match your document's filename. For example, if your file is `my_document.docx`, change the line to:

```python
    file='my_document.docx' # this setup uses a file as knowledgebase. Add file path here.
```

### 5. Run the Application

Execute the Python script:

```bash
python google_file_search.py
```

The script will upload your document, process it with the Gemini model, and print the generated key points along with any grounding sources.

## Project Structure

```
.
├── .env                  # Stores your API key
├── google_file_search.py # Main script for interacting with the Gemini API
└── README.md             # This file
```
