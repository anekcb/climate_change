'''import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="ECOWATCH")

# Replicate Credentials
with st.sidebar:
    st.title('ECOWATCH 🍃')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('Go back to main page [home](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you with climate-related queries?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you with climate-related queries?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
# Refactored from https://github.com/a16z-infra/llama2-chatbot
def generate_llama2_response(prompt_input):
    string_dialogue = "You are an environmental chatbot named EcoGuide. Please provide information and advice on climate-related topics only and say sorry for any other topics unrelated to climate or weather. This includes questions related to climate change, environmental issues, sustainable practices, renewable energy, and biodiversity conservation. strictly avoid responding to non-environmental topics or questions that are not related to climate or environmental concerns."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Reflecting..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)'''
import streamlit as st
import requests
import json
import os
import replicate

# Set your OpenWeatherMap API key
API_KEY = "0d77fe8a900e85d0d7a6a25468afffa3"

# Set the base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Create a Streamlit app
st.title("Weather App")
st.markdown("Enter your location to get the current weather")

# Get the user's location
location = st.text_input("Location")

# Get the user's location
if st.button("Get Weather"):
    # Make a GET request to the OpenWeatherMap API
    response = requests.get(f"{BASE_URL}?q={location}&appid={API_KEY}&units=metric")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Get the weather data
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display the weather data
        st.markdown(f"Weather: {weather}")
        st.markdown(f"Temperature: {temperature}°C")
        st.markdown(f"Humidity: {humidity}%")
        st.markdown(f"Wind Speed: {wind_speed} m/s")
    else:
        st.error("Failed to retrieve weather data")

# App title
st.set_page_config(page_title="ECOWATCH")

# Replicate Credentials
with st.sidebar:
    st.title('ECOWATCH 🍃')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('Go back to main page [home](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you with climate-related queries?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you with climate-related queries?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
# Refactored from https://github.com/a16z-infra/llama2-chatbot
def generate_llama2_response(prompt_input):
    string_dialogue = "You are an environmental chatbot named EcoGuide. Please provide information and advice on climate-related topics only and say sorry for any other topics unrelated to climate or weather. This includes questions related to climate change, environmental issues, sustainable practices, renewable energy, and biodiversity conservation. strictly avoid responding to non-environmental topics or questions that are not related to climate or environmental concerns."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Reflecting..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
