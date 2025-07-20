import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community import Ollama
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

def llm_response(question):
    model = Ollama(model_name = "Llama2")
    prompts = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant, Please help with user queries"),
            ("user", "question: {question}")
        ]
    )
    # Format the prompt with input
    formatted_prompt = prompts.format_messages(question=question)

    # Get the response from the model
    response = model.invoke(formatted_prompt)

    # Parse and return the result
    parser = StrOutputParser()
    return parser.invoke(response)
    

st.set_page_config(page_title = "Chatbot")
st.header("Chatbot")
input = st.text_input("Ask the question ", key = "input")
submit = st.button("submit")

if submit:
    st.write("The Response is")
    output = llm_response(input)
    st.write(output)
        
