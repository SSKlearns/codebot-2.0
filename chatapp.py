import streamlit as st
import streamlit as st
import base64
import os
from groq import Groq
from pinecone import Pinecone, ServerlessSpec

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pc.Index("quickstart")

st.session_state.api_key = os.environ.get("GROQ_API_KEY")

# Only show the API key input if the key is not already set
if not st.session_state.api_key:
    # Ask the user's API key if it doesn't exist
    api_key = st.text_input("Enter API Key", type="password")
    
    # Store the API key in the session state once provided
    if api_key:
        st.session_state.api_key = api_key
        st.rerun()  # Refresh the app once the key is entered to remove the input field
else:
    # If the API key exists, show the chat app
    st.title("Chat App")

    # Initialize the chat message list in session state if it doesn't exist
    if "chat_messages" not in st.session_state:
        st.session_state.groq_chat_messages = [{"role": "system", "content": "You are a helpful assistant. The user will ask a query, and you will respond to it. If any additional context for the query is found, you will be provided with it."}]
        st.session_state.chat_messages = []
        
    # Display previous chat messages
    for messages in st.session_state.chat_messages:
        if messages["role"] in ["user", "assistant"]:
            with st.chat_message(messages["role"]):
                st.markdown(messages["content"])
    
    # Define a function to simulate chat interaction (you would replace this with an actual API call)
    def get_chat():
        embedding = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[st.session_state.chat_messages[-1]["content"]],
            parameters={
                "input_type": "query"
            }
        )
        results = index.query(
            namespace="ns1",
            vector=embedding[0].values,
            top_k=3,
            include_values=False,
            include_metadata=True
        )
        context = ""
        for result in results.matches:
            if result['score'] > 0.8:
                context += result['metadata']['text']
            
        st.session_state.groq_chat_messages[-1]["content"] = f"User Query: {st.session_state.chat_messages[-1]['content']} \n Retrieved Content (optional): {context}"
        chat_completion = client.chat.completions.create(
            messages=st.session_state.groq_chat_messages,
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content

    # Handle user input
    if prompt := st.chat_input("Try asking the bot what it can do, or thank it for its help!"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        st.session_state.groq_chat_messages.append({"role": "user", "content": prompt})
        # Get the assistant's response (in this case, it's just echoing the prompt)
        with st.spinner("Getting responses..."):
            response = get_chat()
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Add user message and assistant response to chat history
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        st.session_state.groq_chat_messages.append({"role": "assistant", "content": response})