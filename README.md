# CodeBot 2.0

CodeBot 2.0 is a simple chatbot designed to leverage the power of Groq and Pinecone, enabling efficient data retrieval and AI-based interactions with open source models, deployed on the cloud.
The notebook provides a code demo, taken from the documentation of Groq and Pinecone, that provides you an interactive example of getting a response from Llama-3 on Groq, and uploading some data onto Pinecone vector database, and performing a similarity search for a query.

## Libraries

- **[Groq](https://groq.com/)**: Integrates open source models, free of cost, using Groq's AI accelerator for high-speed processing, optimizing chatbot performance.
- **[Pinecone](https://www.pinecone.io/)**: Manage and retrieve vector data, enhancing response relevance with the assistance of a powerful vector database.
- **[Streamlit](https://streamlit.io/)**: An easy to code library that let's you build a simple and elegant UI with only a few extra lines, providing support for session management.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SSKlearns/codebot-2.0.git
   cd codebot-2.0
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Export Groq and Pinecone API Keys**:

   Create your Groq and Pinecone accounts and obtain the respective API keys. Once done, set them as environment variables:

   ```bash
   export GROQ_API_KEY="your_groq_api_key"
   export PINECONE_API_KEY="your_pinecone_api_key"
   ```

## Usage

To load your Pinecone vector DB with some data, first run the cells of `trial.ipynb`. This stores some default data onto your vector db.
After storing some data in your vector db, run the chatbot application and ask it something related to your data in the db:

```bash
streamlit run chatapp.py
```

## Contributing

If you have some meaningful contributions to be made to this basic guide, please create a PR.

## License

This project is open-source under the MIT License.