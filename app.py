import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Optional: LangSmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q & A Chatbot"

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Function to generate response using Groq
def generate_response(question, api_key, model_name, temperature, max_tokens):
    llm = ChatGroq(
        model_name=model_name,
        groq_api_key=api_key,  # Uses user-provided API key
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Streamlit UI
st.title("💬 Q&A Chatbot with Groq")
st.sidebar.title("⚙️ Settings")

# User input for API key
api_key = st.sidebar.text_input("🔑 Enter your Groq API key:", type="password")

# Model selection
model_name = st.sidebar.selectbox(
    "🤖 Select a Groq model:",
    ["mistral-saba-24b", "llama3-70b-8192", "gemma2-9b-it"]
)

# Temperature and token sliders
temperature = st.sidebar.slider("🔥 Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("🧠 Max Tokens", 50, 300, 150)

# Main input area
st.write("💡 Ask me anything!")
user_input = st.text_input("📝 Your Question")

# Handle response generation
if user_input:
    if api_key.strip() == "":
        st.error("❌ Please enter a valid Groq API key.")
    else:
        try:
            response = generate_response(user_input, api_key.strip(), model_name, temperature, max_tokens)
            st.success("✅ Response:")
            st.write(response)
        except Exception as e:
            st.error("⚠️ Something went wrong! Check your API key or model.")
            st.exception(e)
else:
    st.info("👈 Enter your API key and question to get started.")
