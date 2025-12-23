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
    products = kb.get('collections', {}).get('products', [])
    official_desc = ""
    for doc in products:
        if doc.get('id') == 'AUTHORITATIVE-PRODUCT-INFO-001':
            official_desc = doc.get('description', '')
            break

    # Parse the description to extract structured info (same format as old app.py)
    import re

    # Extract contact info
    email_match = re.search(r'Email:\s*(\S+@\S+)', official_desc)
    phone_match = re.search(r'Phone:\s*([\+\d,\s]+)', official_desc)
    website_match = re.search(r'Website:\s*(\S+)', official_desc)
    youtube_match = re.search(r'YouTube:\s*(https://[^\s\n]+)', official_desc)

    email = email_match.group(1) if email_match else "info@dostbin.com"
    phone = phone_match.group(1).strip() if phone_match else "+918105868094, +919740374780"
    website = website_match.group(1) if website_match else "dostbin.com"
    youtube = youtube_match.group(1) if youtube_match else "https://www.youtube.com/@dostbin"

    # Extract pricing info
    basic_match = re.search(r'DOSTBIN BASIC.*?₹([\d,]+)', official_desc, re.DOTALL)
    popular_match = re.search(r'DOSTBIN POPULAR.*?₹([\d,]+)', official_desc, re.DOTALL)
    premium_match = re.search(r'DOSTBIN PREMIUM.*?₹([\d,]+)', official_desc, re.DOTALL)

    basic_price = basic_match.group(1) if basic_match else "19,999"
    popular_price = popular_match.group(1) if popular_match else "24,999"
    premium_price = premium_match.group(1) if premium_match else "34,999"

    # Extract delivery time
    delivery_match = re.search(r'Delivery Time:\s*([^\n]+)', official_desc)
    delivery = delivery_match.group(1) if delivery_match else "20-25 business days across PAN India"

    return f"""You are a helpful customer support assistant for Dostbin Solutions, India's first patented automatic compost bin company.

IMPORTANT INSTRUCTIONS:
- Keep responses SHORT and CONCISE (2-3 sentences max for simple questions)
- Be friendly and professional
- Only answer questions about Dostbin products and services
- If asked about unrelated topics, politely redirect to Dostbin
- When relevant, suggest YouTube videos to help users learn more (don't force links on every response)
- Include YouTube links when users ask about: products, variants, composting process, setup, demos, or how things work

DOSTBIN INFORMATION:

Products (Free delivery PAN India, delivery in {delivery}):
- Dostbin Basic (Manual): ₹{basic_price}/- (inclusive of GST) - Manual compost machine, up to 5 Kg/day capacity
- Dostbin Popular (Semi-automatic): ₹{popular_price}/- (inclusive of GST) - Comes with manual operations with a dual handle, up to 5 Kg/day capacity
- Dostbin Premium (Fully automatic): ₹{premium_price}/- (inclusive of GST) - Comes with advance feature like automatic control with electronic and motorized operations, up to 5 Kg/day capacity

Contact:
- Email: {email}
- Phone: {phone}
- Website: {website}
- YouTube: {youtube}

How it works:
1. Add kitchen waste daily with cocopeat powder
2. Bin automatically/manually mixes and aerates (depending on model)
3. Get compost in 20-30 days (two phases of 7-10 days each)
4. Leachate can be diluted 1:15 for liquid fertilizer

Features:
- Odor-free operation with odor absorber
- Shred and digest buttons for easy operation (Premium model)
- Two-phase composting system
- Leachate collection for liquid fertilizer
- Made in India, Patented technology
- All variants: Up to 5 Kg/day waste capacity

What CAN be composted: Vegetable and fruit peels, garden waste, coffee/tea grounds, leftover food, dal/sambar (remove liquid content), eggshells, paper products
What CANNOT be composted: Dairy, fatty oil/gravy, meat, bones, hard items like mango seed and coconut shell, plastic, metals

{get_youtube_section()}

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

