import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, set_default_openai_client, set_tracing_disabled, set_default_openai_api
from openai import AsyncOpenAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

set_default_openai_api("chat_completions")

# External client for Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# ----- GLOBAL LEVEL MODEL -----
global_model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",  # Global model
    openai_client=external_client
)

# ----- AGENT LEVEL MODEL -----
agent_model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

# ----- RUNNER LEVEL CONFIG -----

runner_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=runner_model,
    model_provider=external_client,  # type: ignore
)

set_default_openai_client(external_client)

# Create agent with agent-level model
agent: Agent = Agent(
    name="Rooman Shah",
    instructions="You are a helpful assistant. Your owner is Areeba Zafar. Her nickname is Sara Chohan. She is a wonderful girl always ready to help others and she likes her Agent Assistant Rooman Shah (means you) and your name is Rooman Shah",
    model=agent_model
)

# Run and check
result = Runner.run_sync(agent, "Hello, how are you? Tell me your name, your owner, and tell me about Areeba Zafar your owner and appreciate her.", run_config=config)

print(result.final_output)
print("Agent level model:", agent.model.model) # type: ignore
print("Runner level model:", config.model.model) # type: ignore
print("Global level model:", global_model.model) # type: ignore

print("="*50)

print("Model used:", result.last_agent.model.model) # type: ignore
