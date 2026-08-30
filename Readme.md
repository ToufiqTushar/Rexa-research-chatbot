<div align="center">
  <h1>🔬 Rexa — AI Research Assistant</h1>
  <p><strong>Read • Retrieve • Understand • Research</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version"/>
    <img src="https://img.shields.io/badge/Streamlit-1.28.0-red?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
    <img src="https://img.shields.io/badge/Groq-API-orange?style=flat-square" alt="Groq API"/>
    <img src="https://img.shields.io/badge/FAISS-Vector%20DB-yellow?style=flat-square" alt="FAISS"/>
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License: MIT"/>
    <img src="https://img.shields.io/badge/Status-Active%20Development-blue?style=flat-square" alt="Status"/>
  </p>
  
  <p>
    <a href="#features">Features</a> •
    <a href="#system-architecture">Architecture</a> •
    <a href="#technology-stack">Tech Stack</a> •
    <a href="#how-it-works">How It Works</a> •
    <a href="#installation">Installation</a> •
    <a href="#deployment">Deployment</a>
  </p>
</div>

<hr>

<h2>📌 Overview</h2>

<p><strong>Rexa</strong> is an AI-powered research assistant that combines <strong>Retrieval-Augmented Generation (RAG)</strong> with general-purpose AI capabilities to help users explore research materials, ask questions, understand difficult concepts, and retrieve relevant information from documents.</p>

<p>The system supports <strong>PDF and DOCX documents</strong> and uses semantic search to retrieve relevant document content before generating an answer using <strong>GPT-OSS-120B</strong>. From intelligent document retrieval to conversational question answering, Rexa demonstrates how RAG can transform research workflows.</p>

<hr>

<h2>✨ Features</h2>

<table>
  <tr>
    <td width="33%">
      <h3>📄 Document Research</h3>
      <ul>
        <li>Upload PDF and DOCX files</li>
        <li>Automatic text extraction</li>
        <li>Semantic document processing</li>
        <li>Multi-format support</li>
      </ul>
    </td>
    <td width="33%">
      <h3>🔎 RAG-Based Retrieval</h3>
      <ul>
        <li>Retrieval-Augmented Generation</li>
        <li>Semantic similarity search</li>
        <li>Context-aware responses</li>
        <li>Relevant chunk retrieval</li>
      </ul>
    </td>
    <td width="33%">
      <h3>🧠 Hybrid Question Routing</h3>
      <ul>
        <li>Automatic question classification</li>
        <li>Document vs General routing</li>
        <li>Smart context switching</li>
        <li>Efficient query handling</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <h3>🤖 AI-Powered Responses</h3>
      <ul>
        <li>GPT-OSS-120B integration</li>
        <li>Natural language generation</li>
        <li>Context-enhanced answers</li>
        <li>High-quality responses</li>
      </ul>
    </td>
    <td>
      <h3>💬 Conversational Interface</h3>
      <ul>
        <li>Chat history maintenance</li>
        <li>Follow-up question support</li>
        <li>Interactive UI</li>
        <li>Seamless conversation flow</li>
      </ul>
    </td>
    <td>
      <h3>📊 Semantic Search</h3>
      <ul>
        <li>FAISS vector database</li>
        <li>Sentence Transformers</li>
        <li>Similarity-based retrieval</li>
        <li>Efficient searching</li>
      </ul>
    </td>
  </tr>
</table>

<hr>

<h2>🧠 AI Components</h2>

<p>Rexa implements <strong>five core AI components</strong> working together for intelligent research assistance:</p>

<table>
  <tr>
    <th width="20%">Component</th>
    <th width="25%">Type</th>
    <th width="55%">Implementation</th>
  </tr>
  <tr>
    <td><strong>Document Loader</strong></td>
    <td>Text Extraction</td>
    <td>PyPDF for PDFs, python-docx for DOCX files with robust error handling</td>
  </tr>
  <tr>
    <td><strong>Text Splitter</strong></td>
    <td>Chunking Strategy</td>
    <td>Recursive character splitting with overlap for context preservation</td>
  </tr>
  <tr>
    <td><strong>Embedding Generator</strong></td>
    <td>Sentence Transformers</td>
    <td>Converts text chunks to vector embeddings using pre-trained models</td>
  </tr>
  <tr>
    <td><strong>Vector Store</strong></td>
    <td>FAISS</td>
    <td>Efficient similarity search with cosine similarity for retrieval</td>
  </tr>
  <tr>
    <td><strong>Question Router</strong></td>
    <td>Hybrid Router</td>
    <td>Classifies questions as document-related or general knowledge</td>
  </tr>
  <tr>
    <td><strong>LLM Interface</strong></td>
    <td>Groq API</td>
    <td>GPT-OSS-120B for natural language generation with context</td>
  </tr>
</table>

<hr>

<h2>🔧 How Each AI Component Works</h2>

<h3>1. Document Loader</h3>
<p><strong>Purpose:</strong> Extract readable text from uploaded documents.</p>
<pre>
Input: PDF or DOCX file
Processing:
  IF file is PDF:
    Use PyPDF2 to extract text page by page
    Handle image-only PDFs with error messages
  IF file is DOCX:
    Use python-docx to extract paragraphs
    Combine into single text document
Output: Extracted plain text
</pre>
<p><strong>Example:</strong></p>
<pre>
File: research_paper.pdf
Extracted Text: "This paper presents a novel approach to..."
Pages: 15
Characters: 45,672
</pre>

<h3>2. Text Splitter</h3>
<p><strong>Algorithm:</strong> Recursive character text splitting with overlap.</p>
<pre>
Configuration:
  • Chunk Size: 1000 characters
  • Overlap: 200 characters
  • Separators: ["\n\n", "\n", ".", " ", ""]
Process:
  1. Split by largest separator first
  2. Build chunks up to chunk_size
  3. Add overlap for context preservation
  4. Handle edge cases
Output: List of text chunks
</pre>
<p><strong>Example:</strong></p>
<pre>
Document: 5000 characters
Chunks: 6 chunks
Chunk 1: "This paper presents... (1000 chars)"
Chunk 2: "...continued with overlap... (1000 chars)"
</pre>

<h3>3. Embedding Generator</h3>
<p><strong>Model:</strong> Sentence Transformers (all-MiniLM-L6-v2).</p>
<pre>
Input: Text chunks
Processing:
  Load pre-trained embedding model
  Convert each chunk to vector embedding
  Normalize embeddings for similarity
Output: 384-dimensional vectors
</pre>
<p><strong>Example:</strong></p>
<pre>
Text: "RAG combines retrieval and generation"
Vector: [0.023, -0.456, 0.789, ..., 0.234] (384 dimensions)
Similarity: Cosine similarity between question and chunks
</pre>

<h3>4. FAISS Vector Store</h3>
<p><strong>Algorithm:</strong> Efficient similarity search with FAISS index.</p>
<pre>
Index Type: IndexFlatIP (Inner Product for cosine similarity)
Process:
  1. Convert all chunk vectors to FAISS index
  2. On question, embed question to vector
  3. Search for k most similar chunks
  4. Return top k chunks
Configuration:
  • k = 3 (number of chunks to retrieve)
  • Distance: Cosine similarity
</pre>
<p><strong>Example:</strong></p>
<pre>
Question: "What is RAG?"
Retrieved Chunks:
  1. "RAG stands for Retrieval-Augmented Generation..." (Score: 0.89)
  2. "The RAG model combines a retriever..." (Score: 0.76)
  3. "RAG was introduced by Lewis et al." (Score: 0.72)
</pre>

<h3>5. Question Router</h3>
<p><strong>Algorithm:</strong> Rule-based classification with keyword matching.</p>
<pre>
Rules:
  DOCUMENT keywords: "document", "paper", "research", "study", "according to"
  GENERAL keywords: "hello", "how are you", "what is AI"
  MEDICAL keywords: "disease", "cancer", "brain" (medical domain)
Process:
  1. Check for document-specific keywords
  2. Check for general conversation patterns
  3. Default to DOCUMENT if document uploaded
  4. Route to appropriate pipeline
Output: "DOCUMENT" or "GENERAL"
</pre>
<p><strong>Example:</strong></p>
<pre>
Question: "What does the paper say about neural networks?"
Route: DOCUMENT → RAG Pipeline

Question: "Hello, how are you?"
Route: GENERAL → Direct LLM
</pre>

<h3>6. RAG Pipeline (Retrieval-Augmented Generation)</h3>
<p><strong>Algorithm:</strong> Retrieve-then-generate with context.</p>
<pre>
Steps:
  1. Embed user question
  2. Search FAISS for top-k chunks
  3. Build prompt with context
  4. Send to GPT-OSS-120B
  5. Generate response

Prompt Template:
  "Context: {retrieved_chunks}
   Question: {user_question}
   Answer based on the context above:"
</pre>
<p><strong>Example:</strong></p>
<pre>
Context: "RAG combines a retriever and a generator..."
Question: "What is RAG?"
Response: "RAG (Retrieval-Augmented Generation) is a framework that combines..."
</pre>

<hr>

<h2>🏗️ System Architecture</h2>

<pre>
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Streamlit UI     │
                    └────────┬─────────┘
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │ Document Upload │     │ User Question   │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │ Text Extraction │     │ Question Router │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 ▼                 ┌─────┴─────┐
        ┌─────────────────┐        │           │
        │ Text Splitting  │     DOCUMENT    GENERAL
        └────────┬────────┘        │           │
                 │                 ▼           ▼
                 ▼        ┌──────────────┐  ┌──────────────┐
        ┌─────────────────┐│ Embedding    │  │ GPT-OSS-120B │
        │ Sentence        ││ + FAISS      │  └──────┬───────┘
        │ Embeddings      │└──────┬───────┘         │
        └─────────────────┘       │                 │
                                  ▼                 │
                         ┌──────────────────┐       │
                         │ Relevant Chunks  │       │
                         └────────┬─────────┘       │
                                  │                 │
                                  ▼                 │
                         ┌──────────────────┐       │
                         │ GPT-OSS-120B      │◄──────┘
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Rexa Response    │
                         └──────────────────┘
</pre>

<hr>

<h2>🛠️ Technology Stack</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><strong>Python 3.9+</strong></td>
    <td>Core programming language</td>
  </tr>
  <tr>
    <td><strong>Streamlit 1.28.0</strong></td>
    <td>Web interface framework</td>
  </tr>
  <tr>
    <td><strong>Groq API</strong></td>
    <td>LLM inference for GPT-OSS-120B</td>
  </tr>
  <tr>
    <td><strong>FAISS</strong></td>
    <td>Vector similarity search database</td>
  </tr>
  <tr>
    <td><strong>Sentence Transformers</strong></td>
    <td>Text embedding generation</td>
  </tr>
  <tr>
    <td><strong>PyPDF2</strong></td>
    <td>PDF text extraction</td>
  </tr>
  <tr>
    <td><strong>python-docx</strong></td>
    <td>DOCX file processing</td>
  </tr>
  <tr>
    <td><strong>python-dotenv</strong></td>
    <td>Environment variable management</td>
  </tr>
</table>

<hr>

<h2>📂 Project Structure</h2>

<pre>
REXA-RESEARCH-CHATBOT/
│
├── 📁 uploads/                              # Uploaded documents storage
│
├── 📁 utils/                                # Utility modules
│   ├── 📄 __init__.py
│   ├── 📄 document_loader.py                # Document extraction
│   ├── 📄 embeddings.py                     # Text embeddings
│   ├── 📄 llm.py                            # LLM integration
│   ├── 📄 router.py                         # Question routing
│   ├── 📄 text_splitter.py                  # Text chunking
│   └── 📄 vector_store.py                   # FAISS operations
│
├── 📄 .env                                   # Environment variables (not in repo)
├── 📄 .env.example                           # Example environment variables
├── 📄 .gitignore                             # Git ignore rules
├── 📄 app.py                                 # Main Streamlit application
├── 📄 requirements.txt                       # Python dependencies
│
├── 📄 test_chunking.py                      # Test text chunking
├── 📄 test_document.py                      # Test document loading
├── 📄 test_embeddings.py                    # Test embeddings
├── 📄 test_groq.py                          # Test Groq API
├── 📄 test_rag.py                           # Test RAG pipeline
├── 📄 test_ui.py                            # Test UI components
└── 📄 test_vector_store.py                  # Test vector store
</pre>

<hr>

<h2>⚙️ How It Works</h2>

<h3>1. Document Upload</h3>
<p>The user uploads a PDF or DOCX file through the Streamlit interface.</p>
<pre>
PDF / DOCX
    ↓
Document Loader
</pre>
<p>The document loader extracts readable text from the uploaded file.</p>

<h3>2. Text Splitting</h3>
<p>The extracted text is divided into smaller chunks for efficient searching.</p>
<pre>
Document
    ↓
Extracted Text
    ↓
Text Chunks
</pre>

<h3>3. Generate Embeddings</h3>
<p>Each text chunk is converted into a numerical vector representation.</p>
<pre>
Text Chunk
    ↓
Embedding Model
    ↓
Vector
</pre>

<h3>4. FAISS Vector Store</h3>
<p>The generated vectors are stored in a FAISS index for efficient similarity search.</p>

<h3>5. Question Routing</h3>
<p>When the user asks a question, Rexa determines whether it requires document retrieval.</p>
<pre>
                    User Question
                         │
                         ▼
                  Question Router
                    /          \
                   /            \
                  ▼              ▼
             DOCUMENT         GENERAL
                │                │
                ▼                ▼
           FAISS Search      GPT-OSS-120B
                │
                ▼
        Relevant Document
             Chunks
                │
                ▼
          GPT-OSS-120B
</pre>

<h3>6. Response Generation</h3>
<p>For document-related questions, retrieved chunks are provided as context to the language model, which generates the final response.</p>

<hr>

<h2>🚀 Installation</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.9 or higher</li>
  <li>pip package manager</li>
  <li>Git (optional, for cloning)</li>
</ul>

<h3>Installation Steps</h3>

<ol>
  <li><strong>Clone the repository:</strong>
    <pre><code>git clone https://github.com/ToufiqTushar/Rexa-research-chatbot.git
cd Rexa-research-chatbot</code></pre>
  </li>
  <li><strong>Create virtual environment:</strong>
    <pre><code># Windows:
python -m venv venv
venv\Scripts\activate

# Mac/Linux:
python3 -m venv venv
source venv/bin/activate</code></pre>
  </li>
  <li><strong>Install dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><strong>Configure environment variables:</strong>
    <pre><code>cp .env.example .env
# Edit .env and add your GROQ_API_KEY</code></pre>
  </li>
  <li><strong>Run the application:</strong>
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

<hr>

<h2>🔑 Environment Configuration</h2>

<p>Rexa requires a Groq API key. Create a <code>.env</code> file in the project root:</p>

<pre><code>GROQ_API_KEY=your_groq_api_key_here</code></pre>

<p>You can use <code>.env.example</code> as a reference.</p>

<blockquote>
  <strong>⚠️ Important:</strong> Never upload your actual <code>.env</code> file or API key to GitHub.
</blockquote>

<h3>Configuring Streamlit Secrets (for deployment)</h3>

<p>When deploying to Streamlit Cloud, add the following to your secrets:</p>

<pre><code>GROQ_API_KEY = "your_groq_api_key"</code></pre>

<hr>

<h2>🧪 Testing</h2>

<p>The project contains several test files for individual components:</p>

<table>
  <tr>
    <th>Test File</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><code>test_document.py</code></td>
    <td>Test document processing</td>
  </tr>
  <tr>
    <td><code>test_embeddings.py</code></td>
    <td>Test embeddings generation</td>
  </tr>
  <tr>
    <td><code>test_vector_store.py</code></td>
    <td>Test FAISS operations</td>
  </tr>
  <tr>
    <td><code>test_rag.py</code></td>
    <td>Test RAG pipeline</td>
  </tr>
  <tr>
    <td><code>test_groq.py</code></td>
    <td>Test Groq API connection</td>
  </tr>
  <tr>
    <td><code>test_chunking.py</code></td>
    <td>Test text chunking</td>
  </tr>
  <tr>
    <td><code>test_ui.py</code></td>
    <td>Test UI components</td>
  </tr>
</table>

<p>Run any test with:</p>

<pre><code>python test_&lt;component&gt;.py</code></pre>

<p>Example:</p>

<pre><code>python test_document.py</code></pre>

<hr>

<h2>🎯 Sample Run</h2>

<pre>
🚀 Document Upload:
-------------------
File: research_paper.pdf

📄 Document Processing:
-------------------
Pages: 15
Chunks: 24 chunks created
Embeddings: 24 vectors generated
Vector Store: FAISS index created

🤖 AI Processing:
-------------------
Step 1: Document Loader
  Extracted: 45,672 characters

Step 2: Text Splitter
  Chunk Size: 1000 characters
  Overlap: 200 characters
  Total Chunks: 24

Step 3: Embedding Generator
  Model: all-MiniLM-L6-v2
  Vector Dimension: 384

Step 4: FAISS Index
  Index Type: IndexFlatIP
  Total Vectors: 24

Step 5: Question Router
  Question: "What is the main contribution of this paper?"
  Route: DOCUMENT

Step 6: RAG Pipeline
  Retrieved Chunks: 3 most relevant
  Context Added: 2,800 characters

Step 7: LLM Generation
  Model: GPT-OSS-120B
  Response: "The paper's main contribution is..."

✅ Response generated successfully!
</pre>

<hr>

<h2>☁️ Deployment</h2>

<p>Rexa can be deployed using <strong>Streamlit Community Cloud</strong>.</p>

<h3>Deployment Steps</h3>

<ol>
  <li>Push your code to a GitHub repository</li>
  <li>Visit <a href="https://streamlit.io/cloud">Streamlit Community Cloud</a></li>
  <li>Connect your GitHub account</li>
  <li>Deploy your app</li>
  <li>Configure secrets in the Streamlit dashboard</li>
</ol>

<h3>Required Secrets</h3>

<p>Add the following to your Streamlit secrets:</p>

<pre><code>GROQ_API_KEY = "your_groq_api_key"</code></pre>

<blockquote>
  <strong>Note:</strong> Do not commit the API key to the repository.
</blockquote>

<hr>

<h2>⚠️ Limitations</h2>

<p>Rexa currently has some limitations:</p>

<ul>
  <li><strong>Document Quality</strong> — Depends on the quality of extracted text</li>
  <li><strong>Scanned PDFs</strong> — Image-only PDFs may require OCR before processing</li>
  <li><strong>Context Window</strong> — Retrieved context is limited to the most relevant chunks</li>
  <li><strong>AI Accuracy</strong> — AI-generated responses may contain errors</li>
  <li><strong>Not a Replacement</strong> — Should not be treated as a replacement for professional research or expert review</li>
</ul>

<hr>

<h2>🔐 Privacy & Security</h2>

<ul>
  <li>Uploaded documents are processed locally to generate embeddings</li>
  <li>No documents are stored permanently unless explicitly saved</li>
  <li>Users should avoid uploading sensitive or confidential information</li>
  <li>API keys must always be stored securely using environment variables or deployment secrets</li>
  <li>The <code>uploads/</code> directory is ignored by Git for security</li>
</ul>

<hr>

<h2>💡 Future Improvements</h2>

<ul>
  <li>✅ <strong>Document Loader</strong> — Implemented for PDF and DOCX</li>
  <li>✅ <strong>Text Splitter</strong> — Implemented with overlap</li>
  <li>✅ <strong>Embedding Generator</strong> — Implemented with Sentence Transformers</li>
  <li>✅ <strong>Vector Store</strong> — Implemented with FAISS</li>
  <li>✅ <strong>Question Router</strong> — Implemented with keyword matching</li>
  <li>✅ <strong>RAG Pipeline</strong> — Implemented with Groq API</li>
  <li>🔲 <strong>OCR Support</strong> — Add OCR for scanned PDFs</li>
  <li>🔲 <strong>Multiple Documents</strong> — Support for multiple documents simultaneously</li>
  <li>🔲 <strong>Document Summarization</strong> — Generate summaries of uploaded documents</li>
  <li>🔲 <strong>Citation Support</strong> — Provide citations for retrieved information</li>
  <li>🔲 <strong>Export History</strong> — Export conversation history</li>
  <li>🔲 <strong>Advanced Routing</strong> — Use ML for more accurate question routing</li>
</ul>

<hr>

<h2>📖 Educational Value</h2>

<p>This project is ideal for:</p>
<ul>
  <li><strong>AI Courses</strong> — Demonstrates RAG, semantic search, and LLM integration</li>
  <li><strong>Research Workflows</strong> — Real-world application of AI for research</li>
  <li><strong>Vector Databases</strong> — Practical implementation of FAISS</li>
  <li><strong>Web Development</strong> — Streamlit integration with AI backend</li>
  <li><strong>Natural Language Processing</strong> — Embeddings, retrieval, and generation</li>
  <li><strong>Final Year Projects</strong> — Comprehensive system with multiple AI components</li>
</ul>

<hr>

<h2>📝 License</h2>

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/>
  <p>This project is licensed under the MIT License.</p>
  <p>Free for academic and learning use.</p>
</div>

<hr>

<h2>🤝 Contributing</h2>

<p>Contributions are welcome! Please feel free to submit issues and pull requests.</p>

<h3>How to Contribute</h3>

<ol>
  <li>Fork the repository</li>
  <li>Create a feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>Open a Pull Request</li>
</ol>

<hr>

<div align="center">
  <h2>👨‍💻 Developer</h2>
  
  <h3>Taufiq Zahan Tushar</h3>
  <p>
    🎓 Computer Science & Engineering Undergraduate<br>
    Green University of Bangladesh
  </p>
  
  <p>
    <a href="mailto:toufiqtushar99@gmail.com">
      <img src="https://img.shields.io/badge/Email-toufiqtushar99%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"/>
    </a>
    <a href="https://www.linkedin.com/in/taufiq-zahan-tushar/">
      <img src="https://img.shields.io/badge/LinkedIn-Taufiq%20Zahan%20Tushar-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
    <a href="https://github.com/ToufiqTushar">
      <img src="https://img.shields.io/badge/GitHub-ToufiqTushar-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/>
    </a>
  </p>
  
  <p>
    ⭐ If you found this project helpful, consider giving it a star!<br>
    📬 Feel free to reach out for questions, suggestions, or collaborations.
  </p>
</div>

<hr>

<div align="center">
  <h3>🔬 Rexa — Where Intelligence Meets Research 📚</h3>
  <p><i>Read, Retrieve, Understand, Research — AI-powered research assistance at your fingertips.</i></p>
  
  <p>
    <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python" alt="Made with Python"/>
    <img src="https://img.shields.io/badge/Powered%20by-Streamlit-red?style=flat-square&logo=streamlit" alt="Powered by Streamlit"/>
    <img src="https://img.shields.io/badge/AI-RAG%20%7C%20Embeddings%20%7C%20FAISS%20%7C%20LLM-brightgreen?style=flat-square" alt="AI Technologies"/>
  </p>
</div>
