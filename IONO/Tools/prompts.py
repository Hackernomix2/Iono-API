def chat_prompt():
    chat_template = """
            Given the following research details:

            - Research Name: {research_name}
            - Research Description: {research_description}
            - Research Goal: {research_goal}
            - Problem Statement: {problem_statement}
            - collected data: {collected_data}
            The researcher is seeking comprehensive information on the following topic: {question}.
            Use the provided context: {context} to craft a detailed and well-organized response. 
            Ensure that your answer addresses the question thoroughly and includes key citations from the context provided at the end of your response. 
            If the context does not cover the topic, explicitly state 'Information could not be found.'

            Your response should include:
            1. A clear and detailed answer to the question.
            2. Relevant citations from the context at the end, formatted as follows: [Citation 1]( https//.. ), [Citation 2]( https//.. ), etc.
            with clicable links to the original sources.

            Be sure to present the information in a structured and readable manner.
            """
    return chat_template

def chat_system_message():
    chat_system_message = """You are an advanced research assistant chatbot designed to help users with in-depth inquiries. 
                               Your role is to provide detailed, well-structured responses based on the provided context and research material. 
                               Always ensure that your answers are accurate and cite relevant sources from the context provided. 
                               If you cannot find relevant information, clearly state that the information could not be found."""
    return chat_system_message


def research_template():
    template = """
    Given the following research details:

    - Research Name: {research_name}
    - Research Description: {research_description}
    - Research Goal: {research_goal}
    - Problem Statement: {problem_statement}

    Create a detailed background study that includes:
    1. A summary of existing knowledge related to the research topic.
    2. Key issues and insights pertinent to the research.
    3. A discussion of the context and significance of the research.

    Additionally, based on the background study, provide a list of at least 10 questions that the researcher should ask during data collection. These questions should be:
    1. Relevant to the research topic and goal.
    2. Designed to elicit valuable information to address the research problem.
    3. Thought-provoking and aimed at gaining deeper insights.

    Your response should be structured as follows:
    1. Background Study
    2. List of Questions for Data Collection
    """
    return template

def research_system_message():
    content="""
    You are a research assistant chatbot designed to help researchers create a background study based on the provided research details. Your task is to generate a detailed background study that outlines the research context, including a summary of existing knowledge, key issues, and relevant insights related to the research topic.

    Based on the background study, you should also provide at least 10 insightful questions that the researcher should consider asking during data collection. These questions should be directly related to the research topic and aimed at gathering valuable information for the research.

    The information you need to work with includes:
    1. Research Name: The title or name of the research project.
    2. Research Description: A brief overview of the research.
    3. Research Goal: The primary objective of the research.
    4. Problem Statement: The key problem or issue the research aims to address.

    Ensure that your background study is comprehensive and well-structured, and that the questions are relevant and thought-provoking.
    """
    return content

def data_analysis_prompt():
    content = """The researcher has provided the following details and data for analysis:

        Research Name: {research_name}
        Research Description: {research_description}
        Research Goal: {research_goal}
        Problem Statement: {problem_statement}

        Form Data (structured as a string): {form_data}

        Your task is to perform a detailed analysis of the provided form data in the context of the research details. Follow these steps:

        1. Data Understanding: Clearly describe the provided form data, identifying the variables and their types (e.g., categorical, numerical).

        2. Data Cleaning: Mention any cleaning steps you take, such as handling missing values or correcting inconsistencies.

        3. **Exploratory Data Analysis (EDA):** Conduct a thorough EDA, including:
        - Descriptive statistics for each variable.
        - Visualizations (e.g., histograms, box plots) to identify patterns and distributions.
        - Identification of any anomalies or outliers.

        4. Correlational Analysis: Calculate and interpret correlation coefficients between relevant variables. Explain the strength and direction of the relationships.

        5. Statistical Testing: Perform appropriate statistical tests (e.g., t-tests, chi-square tests) to validate any significant correlations or differences. Clearly present the results, including p-values and confidence intervals.

        6. Conclusions: Based on the analysis, draw valid conclusions related to the research goal and problem statement. Discuss how the findings support or contradict the initial hypothesis or goal.

        7. Recommendations: Provide recommendations for further research or actions based on the conclusions.

        Ensure that your analysis is structured, logical, and clearly presented. Include any relevant citations or references to support your methods and conclusions.
        """
    return content

def data_analysis_system_message():
    content = """You are an advanced research assistant chatbot designed to analyze structured form data along with provided research details. 
    Your role is to perform comprehensive and step-by-step analysis, making correlational calculations and deriving valid conclusions.
    Always ensure that your responses are accurate, logically sound, and clearly presented. 
    If you cannot perform the analysis due to missing or insufficient data, explicitly state the limitation and suggest additional data or steps required."""
    return content