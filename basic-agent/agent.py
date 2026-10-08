from agno.agent import Agent

from agno.models.groq import Groq

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools

from agno.tools.file_generation import FileGenerationTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[
            DuckDuckGoTools(),
            FileGenerationTools(output_directory="generated_files")
            ],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response(" create a report file of is it safe to travel to UAE today?")