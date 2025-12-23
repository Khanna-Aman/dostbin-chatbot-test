#!/usr/bin/env python3
"""
Dostbin Groq Llama 3.1 8B Chatbot - Streamlit Cloud Version
Ultra-cheap AI chatbot using Groq's free tier
Cost: $0.05 input / $0.08 output per 1M tokens
"""

import streamlit as st
import json
from groq import Groq
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
MODEL = "llama-3.1-8b-instant"

# --- Secrets Retrieval (Streamlit Cloud) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets. Please configure it in app settings.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Page configuration
st.set_page_config(
    page_title="Dostbin AI Assistant",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for chat styling
st.markdown("""
<style>
    .stApp { background-color: #f5f7f9; }
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #28a745;
        color: white;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: white;
        color: #333;
        margin-right: 20%;
        border: 1px solid #e0e0e0;
    }
    /* Hide Streamlit branding for embed */
    iframe[title="streamlit_chat_message"] { display: none; }
</style>
""", unsafe_allow_html=True)

# Load knowledge base from file (bundled with app)
@st.cache_data
def load_knowledge_base():
    try:
        with open('knowledge_base.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

kb = load_knowledge_base()

# Build YouTube videos section
def get_youtube_section():
    if not kb or 'collections' not in kb or 'youtube_videos' not in kb['collections']:
        return ""
    
    videos = kb['collections']['youtube_videos']
    youtube_section = "\n\nAVAILABLE YOUTUBE VIDEOS:\n"
    
    videos_by_category = defaultdict(list)
    for video in videos:
        videos_by_category[video['category']].append(video)
    
    for category, vids in videos_by_category.items():
        youtube_section += f"\n{category}:\n"
        for vid in vids:
            summary = vid.get('content_summary', '')[:150]
            youtube_section += f"- {vid['title']}\n  URL: {vid['video_url']}\n  Summary: {summary}...\n"
    
    return youtube_section

# Create system prompt with knowledge base
def get_system_prompt():
    if not kb:
        return "You are a helpful assistant for Dostbin Solutions."

    # Extract official product info from knowledge base
    official_info = ""
    products = kb.get('collections', {}).get('products', [])
    for doc in products:
        if doc.get('id') == 'AUTHORITATIVE-PRODUCT-INFO-001':
            official_info = doc.get('description', '')
            break

    return f"""You are a helpful customer support assistant for Dostbin Solutions.

CRITICAL INSTRUCTIONS:
- Keep responses SHORT and CONCISE (2-3 sentences max for simple questions)
- Be friendly and professional
- Only answer questions about Dostbin products and services
- If asked about unrelated topics, politely redirect to Dostbin
- When relevant, suggest YouTube videos to help users learn more (don't force links on every response)
- Include YouTube links when users ask about: products, variants, composting process, setup, demos, or how things work

⚠️ IMPORTANT: For ALL information (pricing, delivery, contact, how it works, features), ONLY use the official information below. This is the single source of truth.

OFFICIAL DOSTBIN INFORMATION (COMPLETE - USE THIS ONLY):

{official_info}

{get_youtube_section()}

When users ask about tutorials, demos, setup, or how things work, ALWAYS provide specific YouTube video links from the official information above.
Answer questions naturally and conversationally."""

SYSTEM_PROMPT = get_system_prompt()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'total_tokens' not in st.session_state:
    st.session_state.total_tokens = {'input': 0, 'output': 0}

# Header
st.title("🌱 Dostbin AI Assistant")
st.caption("Powered by Groq Llama 3.1 8B - Ultra-fast AI Support")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about Dostbin..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare messages for API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend([{"role": m["role"], "content": m["content"]}
                     for m in st.session_state.messages])

    # Get response from Groq
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_tokens=500,
                temperature=0.7,
            )
            assistant_message = response.choices[0].message.content
            st.markdown(assistant_message)
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Sidebar with info (dynamically loaded from knowledge base)
with st.sidebar:
    st.header("ℹ️ About Dostbin")

    # Extract contact info from knowledge base
    kb_data = load_knowledge_base()
    products = kb_data.get('collections', {}).get('products', [])
    contact_info = ""
    company_desc = ""

    for doc in products:
        if doc.get('id') == 'AUTHORITATIVE-PRODUCT-INFO-001':
            desc = doc.get('description', '')
            # Extract company info
            if 'India\'s first patented' in desc:
                company_desc = "**India's First Patented Automatic Compost Bin**"
            # Extract contact info
            if 'Email:' in desc:
                import re
                email_match = re.search(r'Email:\s*(\S+@\S+)', desc)
                phone_match = re.search(r'Phone:\s*([\+\d,\s]+)', desc)
                if email_match:
                    email = email_match.group(1)
                if phone_match:
                    phones = phone_match.group(1).strip()
                    phone = phones.split(',')[0].strip()  # First phone number
            break

    st.markdown(f"""
    {company_desc}

    🌿 Convert kitchen waste to compost at home
    📱 IoT & Mobile App control (Premium)
    🚚 Free delivery PAN India

    **Contact:**
    - 📧 {email if 'email' in locals() else 'info@dostbin.com'}
    - 📞 {phone if 'phone' in locals() else '+918105868094'}
    - 🌐 [dostbin.com](https://dostbin.com)
    """)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

