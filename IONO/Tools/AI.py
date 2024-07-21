import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from tavily import TavilyClient
from .prompts import chat_system_message, chat_prompt , research_system_message , research_template , data_analysis_prompt , data_analysis_system_message


load_dotenv()
api = os.getenv("TAVILY_API_KEY")
g_api = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=g_api , verbose=True)
output = StrOutputParser()

#for chat
chat_system_message_ = SystemMessage(content=chat_system_message())
chat_template = chat_prompt()
data_analysis_template_ = data_analysis_prompt()

#for initial research
research_template_ = research_template()
research_system_message_ = SystemMessage(content=research_system_message())
data_analysis_system_message_ = SystemMessage(content=data_analysis_system_message())

research_prompt = PromptTemplate.from_template(system_message=research_system_message_, template=research_template_)
chat_prompt_ = PromptTemplate.from_template(system_message=chat_system_message_, template=chat_template)
data_analysis_prompt_ = PromptTemplate.from_template(system_message=data_analysis_system_message_, template=data_analysis_template_)


def get_context(question):
    client = TavilyClient(api_key=api)
    try:
        refs = client.get_search_context(question , max_results=10)
        search_results = client.search(question , max_results=10)
        return refs, search_results
    except Exception as e:
        print(f"Error fetching context: {e}")
        return "Context could not be retrieved", "Search results could not be retrieved"


def chat(research_name, research_description, research_goal, problem_statement , question , collected_data = ""):
    try:
        context_refs, search_results = get_context(question)
        chain = chat_prompt_ | llm | output

        answer = chain.invoke({
            "research_name": research_name,
            "research_description": research_description,
            "research_goal": research_goal,
            "problem_statement": problem_statement,
            "question": question,
            "collected_data": collected_data,
            "context": f"{context_refs} {search_results}",
        })
        return answer
    except Exception as e:
        print(f"Error during chat execution: {e}")
        return "An error occurred during processing."


def research(research_name, research_description, research_goal, problem_statement):
    try:
        chain = research_prompt | llm | output
        answer = chain.invoke({
            "research_name": research_name,
            "research_description": research_description,
            "research_goal": research_goal,
            "problem_statement": problem_statement
        })
        return answer
    except Exception as e:
        print(f"Error during research execution: {e}")
        return "An error occurred during processing."
    


def data_analysis(research_name, research_description, research_goal, problem_statement ,formdata):
    try:
        chain = data_analysis_prompt_ | llm | output
        answer = chain.invoke({
            "research_name": research_name,
            "research_description": research_description,
            "research_goal": research_goal,
            "problem_statement": problem_statement,
            "formdata": formdata
        })
        return answer
    except Exception as e:
        print(f"Error during research execution: {e}")
        return "An error occurred during processing."