import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

def llm_response(question):
    model = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = os.environ["OPENAI_API_KEY"])#"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")
    prompts = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant, Please help with user queries"),
            ("user", "question: {question}")
        ]
    )
    # Format the prompt with input from user
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
        
