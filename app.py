import os
import html
import streamlit as st


# =========================================================
# BACKEND IMPORTS
# =========================================================

from utils.document_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import (
    create_embeddings,
    create_query_embedding
)
from utils.vector_store import (
    create_vector_store,
    search_vector_store
)
from utils.llm import ask_llm
from utils.router import classify_question


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Rexa",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE
# =========================================================

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_filename" not in st.session_state:
    st.session_state.uploaded_filename = None

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# =========================================================
# THEME COLORS
# =========================================================

if st.session_state.dark_mode:

    BG = "#212121"
    SIDEBAR_BG = "#171717"
    CARD_BG = "#242424"
    INPUT_BG = "#2b2b2b"

    TEXT_PRIMARY = "#eeeeee"
    TEXT_SECONDARY = "#aaaaaa"
    TEXT_MUTED = "#777777"

    BORDER = "#3a3a3a"
    BORDER_LIGHT = "#444444"

else:

    BG = "#ffffff"
    SIDEBAR_BG = "#f7f7f8"
    CARD_BG = "#ffffff"
    INPUT_BG = "#ffffff"

    TEXT_PRIMARY = "#202123"
    TEXT_SECONDARY = "#777777"
    TEXT_MUTED = "#999999"

    BORDER = "#eeeeee"
    BORDER_LIGHT = "#e1e1e1"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       GLOBAL
    ===================================================== */

    .stApp {{
        background: {BG};
        color: {TEXT_PRIMARY};
    }}

    .main .block-container {{
        max-width: 920px;
        padding-top: 1rem;
        padding-bottom: 7rem;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    header {{
        background: transparent !important;
    }}


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {{
        background: {SIDEBAR_BG};
        border-right: 1px solid {BORDER};
    }}

    section[data-testid="stSidebar"] > div:first-child {{
        padding: 1rem 0.8rem;
    }}


    /* =====================================================
       BRAND
    ===================================================== */

    .brand-container {{
        padding: 5px 7px 18px 7px;
    }}

    .brand-row {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .brand-icon {{
        width: 36px;
        height: 36px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 10px;

        background: #202123;

        font-size: 19px;
    }}

    .brand-title {{
        font-size: 18px;
        font-weight: 700;

        color: {TEXT_PRIMARY};

        letter-spacing: -0.3px;
    }}

    .brand-subtitle {{
        font-size: 11px;
        color: {TEXT_MUTED};

        margin-top: 4px;
        margin-left: 46px;
    }}


    /* =====================================================
       SIDEBAR SECTIONS
    ===================================================== */

    .section-title {{
        margin-top: 21px;
        margin-bottom: 8px;

        padding-left: 7px;

        font-size: 10px;
        font-weight: 700;

        letter-spacing: 0.8px;
        text-transform: uppercase;

        color: {TEXT_MUTED};
    }}


    /* =====================================================
       SIDEBAR BUTTONS
    ===================================================== */

    section[data-testid="stSidebar"] .stButton > button {{
        width: 100%;
        min-height: 38px;

        border-radius: 8px;

        border: 1px solid {BORDER_LIGHT};

        background: {CARD_BG};

        color: {TEXT_PRIMARY};

        font-size: 13px;
        font-weight: 500;

        transition: all 0.15s ease;
    }}

    section[data-testid="stSidebar"] .stButton > button:hover {{
        background: {INPUT_BG};
        border-color: {TEXT_MUTED};
    }}


    /* =====================================================
       FILE UPLOADER
    ===================================================== */

    [data-testid="stFileUploaderDropzone"] {{
        background: {CARD_BG};

        border: 1px dashed #888888;

        border-radius: 10px;
    }}

    [data-testid="stFileUploaderDropzone"]:hover {{
        border-color: {TEXT_MUTED};
    }}


    /* =====================================================
       DOCUMENT CARD
    ===================================================== */

    .document-card {{
        margin-top: 10px;

        padding: 12px;

        background: {CARD_BG};

        border: 1px solid {BORDER_LIGHT};

        border-radius: 10px;
    }}

    .document-name {{
        font-size: 12px;

        font-weight: 600;

        color: {TEXT_PRIMARY};

        overflow-wrap: anywhere;
    }}

    .document-ready {{
        margin-top: 6px;

        font-size: 10px;

        color: #16a34a;
    }}

    .document-meta {{
        margin-top: 3px;

        font-size: 10px;

        color: {TEXT_MUTED};
    }}


    /* =====================================================
       CHAT HISTORY
    ===================================================== */

    .history-item {{
        padding: 8px 9px;

        border-radius: 7px;

        font-size: 11px;

        color: {TEXT_SECONDARY};

        white-space: nowrap;

        overflow: hidden;

        text-overflow: ellipsis;
    }}

    .history-item:hover {{
        background: {INPUT_BG};
    }}


    /* =====================================================
       MAIN HEADER
    ===================================================== */

    .top-header {{
        display: flex;

        justify-content: space-between;

        align-items: center;

        padding: 4px 0 13px 0;

        border-bottom: 1px solid {BORDER};

        margin-bottom: 20px;
    }}

    .top-brand {{
        display: flex;

        align-items: center;

        gap: 8px;
    }}

    .top-logo {{
        font-size: 18px;
    }}

    .top-title {{
        font-size: 15px;

        font-weight: 650;

        color: {TEXT_PRIMARY};
    }}

    .model-badge {{
        padding: 5px 10px;

        border: 1px solid {BORDER_LIGHT};

        border-radius: 20px;

        background: {CARD_BG};

        font-size: 10px;

        color: {TEXT_SECONDARY};
    }}


    /* =====================================================
       THEME BUTTON
    ===================================================== */

    .theme-button-container {{
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }}

    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button {{
        border-radius: 10px;
        border: 1px solid {BORDER_LIGHT};
        background: {CARD_BG};
        color: {TEXT_PRIMARY};
        font-size: 16px;
        min-height: 38px;
        transition: all 0.15s ease;
    }}

    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button:hover {{
        background: {INPUT_BG};
        border-color: {TEXT_MUTED};
    }}


    /* =====================================================
       WELCOME
    ===================================================== */

    .welcome-container {{
        text-align: center;

        padding-top: 15vh;
    }}

    .welcome-icon {{
        width: 66px;
        height: 66px;

        margin: 0 auto 20px auto;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 18px;

        background: #202123;

        color: white;

        font-size: 30px;
    }}

    .welcome-brand {{
        font-size: 15px;

        font-weight: 600;

        color: {TEXT_SECONDARY};

        margin-bottom: 5px;
    }}

    .welcome-title {{
        font-size: 28px;

        font-weight: 650;

        color: {TEXT_PRIMARY};

        letter-spacing: -0.6px;
    }}

    .welcome-description {{
        max-width: 540px;

        margin: 10px auto 0 auto;

        font-size: 14px;

        line-height: 1.65;

        color: {TEXT_SECONDARY};
    }}


    /* =====================================================
       FEATURE CARDS
    ===================================================== */

    .feature-card {{
        min-height: 110px;

        padding: 15px;

        border: 1px solid {BORDER_LIGHT};

        border-radius: 12px;

        background: {CARD_BG};
    }}

    .feature-icon {{
        font-size: 18px;

        margin-bottom: 6px;
    }}

    .feature-title {{
        font-size: 11px;

        font-weight: 650;

        color: {TEXT_PRIMARY};
    }}

    .feature-description {{
        margin-top: 4px;

        font-size: 10px;

        line-height: 1.45;

        color: {TEXT_MUTED};
    }}


    /* =====================================================
       CHAT MESSAGES
    ===================================================== */

    [data-testid="stChatMessage"] {{
        padding: 15px 18px;

        border-radius: 12px;

        margin-bottom: 5px;

        color: {TEXT_PRIMARY};
    }}

    [data-testid="stChatMessage"] p {{
        font-size: 14px;

        line-height: 1.75;
    }}


    /* USER */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {{
        background: {INPUT_BG};
    }}


    /* ASSISTANT */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {{
        background: {BG};
    }}


    /* =====================================================
       RESPONSE TYPE
    ===================================================== */

    .response-type {{
        margin-bottom: 8px;

        font-size: 10px;

        font-weight: 500;

        color: {TEXT_MUTED};
    }}


    /* =====================================================
       CHAT INPUT
    ===================================================== */

    [data-testid="stChatInput"] {{
        border-radius: 14px;
    }}

    [data-testid="stChatInput"] textarea {{
        font-size: 14px;
    }}


    /* =====================================================
       CHAT DISCLAIMER
    ===================================================== */

    .chat-disclaimer {{
        width: 100%;
        max-width: 920px;

        margin: -1px auto 0 auto;

        text-align: center;

        font-size: 9px;
        line-height: 1.4;

        color: {TEXT_MUTED};

        padding: 0 10px;

        pointer-events: none;
    }}


    /* =====================================================
       DEVELOPER CREDIT
    ===================================================== */

    .developer-credit {{
        margin-top: 14px;

        padding-top: 10px;

        border-top: 1px solid {BORDER};

        text-align: center;

        font-size: 10px;

        line-height: 1.5;

        color: {TEXT_MUTED};
    }}

    .developer-name {{
        font-weight: 600;

        color: {TEXT_SECONDARY};
    }}


    /* =====================================================
       STREAMLIT TEXT
    ===================================================== */

    .stMarkdown,
    .stCaption,
    label {{
        color: {TEXT_PRIMARY};
    }}


    /* =====================================================
       RESPONSIVE
    ===================================================== */

    @media (max-width: 700px) {{

        .main .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}

        .welcome-container {{
            padding-top: 8vh;
        }}

        .welcome-title {{
            font-size: 23px;
        }}

        .welcome-description {{
            font-size: 13px;
        }}

        .chat-disclaimer {{
            width: 90%;
            font-size: 8px;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # -----------------------------------------------------
    # REXA BRAND
    # -----------------------------------------------------

    st.html(
        """
        <div class="brand-container">

            <div class="brand-row">

                <div class="brand-icon">
                    🔬
                </div>

                <div class="brand-title">
                    Rexa
                </div>

            </div>

            <div class="brand-subtitle">
                AI-Powered Research Assistant
            </div>

        </div>
        """
    )


    # -----------------------------------------------------
    # NEW CHAT
    # -----------------------------------------------------

    if st.button(
        "＋  New chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


    # -----------------------------------------------------
    # DOCUMENT
    # -----------------------------------------------------

    st.html(
        """
        <div class="section-title">
            Research Document
        </div>
        """
    )


    uploaded_file = st.file_uploader(
        "Upload PDF or DOCX",
        type=["pdf", "docx"]
    )


    # -----------------------------------------------------
    # PROCESS DOCUMENT
    # -----------------------------------------------------

    if uploaded_file is not None:

        if (
            st.session_state.uploaded_filename
            != uploaded_file.name
        ):

            with st.spinner(
                "Reading and indexing document..."
            ):

                os.makedirs(
                    "uploads",
                    exist_ok=True
                )


                file_path = os.path.join(
                    "uploads",
                    uploaded_file.name
                )


                with open(
                    file_path,
                    "wb"
                ) as file:

                    file.write(
                        uploaded_file.getbuffer()
                    )


                # Extract
                text = extract_text(
                    file_path
                )


                # Split
                chunks = split_text(
                    text
                )


                # Embeddings
                embeddings = create_embeddings(
                    chunks
                )


                # Vector Store
                vector_store = create_vector_store(
                    embeddings
                )


                # Save
                st.session_state.chunks = chunks

                st.session_state.vector_store = (
                    vector_store
                )

                st.session_state.uploaded_filename = (
                    uploaded_file.name
                )

                st.session_state.messages = []


            st.success(
                "Document indexed successfully."
            )


    # -----------------------------------------------------
    # DOCUMENT CARD
    # -----------------------------------------------------

    if st.session_state.uploaded_filename:

        chunk_count = (
            len(st.session_state.chunks)
            if st.session_state.chunks
            else 0
        )


        safe_filename = html.escape(
            st.session_state.uploaded_filename
        )


        st.html(
            f"""
            <div class="document-card">

                <div class="document-name">
                    📄 {safe_filename}
                </div>

                <div class="document-ready">
                    ● Ready for questions
                </div>

                <div class="document-meta">
                    {chunk_count} text chunks indexed
                </div>

            </div>
            """
        )


    # -----------------------------------------------------
    # RECENT CHATS
    # -----------------------------------------------------

    st.html(
        """
        <div class="section-title">
            Recent Chats
        </div>
        """
    )


    user_messages = [
        message["content"]
        for message in st.session_state.messages
        if message["role"] == "user"
    ]


    if user_messages:

        for message in user_messages[-6:]:

            safe_message = html.escape(
                message
            )

            if len(safe_message) > 40:

                safe_message = (
                    safe_message[:40] + "..."
                )


            st.html(
                f"""
                <div class="history-item">
                    💬 {safe_message}
                </div>
                """
            )

    else:

        st.caption(
            "Your conversations will appear here."
        )


    # -----------------------------------------------------
    # CONTROLS
    # -----------------------------------------------------

    st.html(
        """
        <div class="section-title">
            Controls
        </div>
        """
    )


    if st.button(
        "🗑  Clear conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


    # -----------------------------------------------------
    # SYSTEM
    # -----------------------------------------------------

    st.html(
        """
        <div class="section-title">
            System
        </div>
        """
    )


    if st.session_state.vector_store is not None:

        rag_status = "Active"

    else:

        rag_status = "Waiting for document"


    st.caption(
        f"🔬 Rexa\n\n"
        f"🤖 GPT-OSS-120B\n\n"
        f"🔎 RAG: {rag_status}\n\n"
        f"🧠 Hybrid question routing"
    )


    # -----------------------------------------------------
    # DEVELOPER CREDIT
    # -----------------------------------------------------

    st.html(
        """
        <div class="developer-credit">

            Developed by
            <br>

            <span class="developer-name">
                Taufiq Zahan Tushar
            </span>

        </div>
        """
    )


# =========================================================
# MAIN HEADER
# =========================================================

header_col1, header_col2 = st.columns(
    [8, 1],
    vertical_alignment="center"
)


with header_col1:

    st.html(
        """
        <div class="top-header">

            <div class="top-brand">

                <div class="top-logo">
                    🔬
                </div>

                <div class="top-title">
                    Rexa
                </div>

            </div>

            <div class="model-badge">
                GPT-OSS-120B
            </div>

        </div>
        """
    )


with header_col2:

    theme_icon = (
        "☀️"
        if st.session_state.dark_mode
        else "🌙"
    )


    if st.button(
        theme_icon,
        key="theme_button",
        help="Change theme",
        use_container_width=True
    ):

        st.session_state.dark_mode = (
            not st.session_state.dark_mode
        )

        st.rerun()


# =========================================================
# WELCOME SCREEN
# =========================================================

if not st.session_state.messages:

    st.html(
        """
        <div class="welcome-container">

            <div class="welcome-icon">
                🔬
            </div>

            <div class="welcome-brand">
                Rexa
            </div>

            <div class="welcome-title">
                How can I help you today?
            </div>

            <div class="welcome-description">
                Ask questions about your research documents,
                understand difficult concepts, summarize
                material, or explore a topic using AI.
            </div>

        </div>
        """
    )


    # -----------------------------------------------------
    # FEATURE CARDS
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(
        3,
        gap="small"
    )


    with col1:

        st.html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    📄
                </div>

                <div class="feature-title">
                    Document Research
                </div>

                <div class="feature-description">
                    Upload a PDF or DOCX and ask
                    questions about its contents.
                </div>

            </div>
            """
        )


    with col2:

        st.html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🔎
                </div>

                <div class="feature-title">
                    Smart Retrieval
                </div>

                <div class="feature-description">
                    Find relevant information using
                    semantic document search.
                </div>

            </div>
            """
        )


    with col3:

        st.html(
            """
            <div class="feature-card">

                <div class="feature-icon">
                    🧠
                </div>

                <div class="feature-title">
                    General AI
                </div>

                <div class="feature-description">
                    Ask general questions using
                    GPT-OSS-120B.
                </div>

            </div>
            """
        )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(
                message["content"]
            )

    else:

        with st.chat_message(
            "assistant",
            avatar="🔬"
        ):

            st.markdown(
                message["content"]
            )


# =========================================================
# CHAT INPUT
# =========================================================

question = st.chat_input(
    "Ask Rexa anything..."
)


# =========================================================
# CHAT DISCLAIMER
# =========================================================

st.html(
    """
    <div class="chat-disclaimer">
        ⚠️ Rexa can make mistakes. Please verify important information.
    </div>
    """
)


# =========================================================
# QUESTION PROCESSING
# =========================================================

if question:

    # -----------------------------------------------------
    # USER MESSAGE
    # -----------------------------------------------------

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(
            question
        )


    # -----------------------------------------------------
    # SAVE USER MESSAGE
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # -----------------------------------------------------
    # QUESTION ROUTING
    # -----------------------------------------------------

    question_type = classify_question(
        question
    )


    use_rag = (
        question_type == "DOCUMENT"
        and
        st.session_state.vector_store is not None
    )


    # =====================================================
    # RAG MODE
    # =====================================================

    if use_rag:

        query_embedding = create_query_embedding(
            question
        )


        scores, indices = search_vector_store(
            st.session_state.vector_store,
            query_embedding,
            top_k=3
        )


        relevant_chunks = []


        for index_number in indices[0]:

            relevant_chunks.append(
                st.session_state.chunks[
                    index_number
                ]
            )


        context = "\n\n".join(
            relevant_chunks
        )


        # -------------------------------------------------
        # GENERATE ANSWER
        # -------------------------------------------------

        with st.chat_message(
            "assistant",
            avatar="🔬"
        ):

            st.html(
                """
                <div class="response-type">
                    📄 Rexa is answering from your document
                </div>
                """
            )


            with st.spinner(
                "Searching your document..."
            ):

                answer = ask_llm(
                    question,
                    context,
                    st.session_state.messages[:-1]
                )


            st.markdown(
                answer
            )


    # =====================================================
    # GENERAL LLM MODE
    # =====================================================

    else:

        with st.chat_message(
            "assistant",
            avatar="🔬"
        ):

            st.html(
                """
                <div class="response-type">
                    ✨ Rexa is thinking
                </div>
                """
            )


            with st.spinner(
                "Thinking..."
            ):

                answer = ask_llm(
                    question,
                    chat_history=(
                        st.session_state.messages[:-1]
                    )
                )


            st.markdown(
                answer
            )


    # -----------------------------------------------------
    # SAVE ANSWER
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )