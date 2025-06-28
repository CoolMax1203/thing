import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

# Gemini API Key and setup
gemini_api_key = "AIzaSyBqICNnPzHE36KrKDBnVQ_hMOZo1Z0HMNM"

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Create the agent
agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# Streamlit UI
st.set_page_config(page_title="Burhan's Gemini Agent Web App", layout="centered")
st.title("🤖Mubashir's Gemini Agent")

# User input
user_input = st.text_input("💬 Enter your prompt:", placeholder="Ask something...")

# Button to run agent
if st.button("Run Agent") and user_input:
    with st.spinner("Thinking..."):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(Runner.run(agent, user_input, run_config=config))

        st.success("✅ Response:")
        st.write(result.final_output)