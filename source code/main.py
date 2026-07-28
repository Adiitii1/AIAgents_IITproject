import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import TavilySearchTool
from tools.custom_tools import calculate_rice_score, format_jira_story

# Load Environment Variables
load_dotenv()

# Define explicitly configured Gemini LLM
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
)

def create_pm_crew():
    # 1. Define Specialist Agents
    feedback_analyst = Agent(
        role="Senior Customer Feedback Analyst",
        goal="Extract key user pain points, requirements, and sentiment from the user's input.",
        backstory="Expert user researcher skilled in qualitative feedback synthesis and user need extraction.",
        llm=gemini_llm,
        verbose=True
    )

    competitor_researcher = Agent(
        role="Market Intelligence Specialist",
        goal="Research market trends and competitor context related to the user's topic.",
        backstory="Strategic market analyst skilled at feature benchmarking and industry research.",
        tools=[TavilySearchTool()] if os.getenv("TAVILY_API_KEY") else [],
        llm=gemini_llm,
        verbose=True
    )

    feature_prioritizer = Agent(
        role="Lead Product Manager",
        goal="Evaluate impact, feasibility, and prioritization strategy based on the analysis.",
        backstory="Data-driven PM with expertise in feature prioritization, RICE scoring, and product strategy.",
        tools=[calculate_rice_score],
        llm=gemini_llm,
        verbose=True
    )

    prd_writer = Agent(
        role="Principal Technical PRD Writer",
        goal="Draft core technical requirements, specs, or detailed answers based on the PM strategy.",
        backstory="Technical PM known for clear product requirements, edge case definitions, and technical specs.",
        llm=gemini_llm,
        verbose=True
    )

    sprint_planner = Agent(
        role="Technical Scrum Master",
        goal="Synthesize the crew's findings into actionable user stories or execution steps.",
        backstory="Agile expert focusing on breaking down complex requirements into actionable tasks.",
        tools=[format_jira_story],
        llm=gemini_llm,
        verbose=True
    )

    # 2. Define Dynamic Tasks (Using {user_query})
    t1 = Task(
        description="Analyze the following user prompt/question:\n\n'{user_query}'\n\nIdentify the core user needs, pain points, or product questions being raised.",
        expected_output="Analysis of core user needs and key takeaways.",
        agent=feedback_analyst
    )

    t2 = Task(
        description="Review the extracted needs from Task 1 for the prompt: '{user_query}'. Provide relevant market context, benchmarking, or industry standards.",
        expected_output="Brief market intelligence context.",
        agent=competitor_researcher
    )

    t3 = Task(
        description="Synthesize the user feedback and market insights. Evaluate trade-offs, priority, or strategic direction for: '{user_query}'.",
        expected_output="Strategic PM recommendations and prioritization breakdown.",
        agent=feature_prioritizer
    )

    t4 = Task(
        description="Translate the strategic recommendations into detailed requirements or a technical breakdown addressing: '{user_query}'.",
        expected_output="Structured requirement specs or technical answer.",
        agent=prd_writer
    )

    t5 = Task(
        description="Synthesize all team insights into a clear, comprehensive final answer for the user's prompt: '{user_query}'. Include actionable next steps or user stories if relevant.",
        expected_output="Final polished response addressing the user query comprehensively.",
        agent=sprint_planner
    )

    # 3. Assemble Sequential Crew
    crew = Crew(
        agents=[feedback_analyst, competitor_researcher, feature_prioritizer, prd_writer, sprint_planner],
        tasks=[t1, t2, t3, t4, t5],
        process=Process.sequential,
        memory=False,
        verbose=True
    )

    return crew

def main():
    print("🚀 Dynamic Multi-Agent AI Product Team Initialized!")
    pm_crew = create_pm_crew()

    while True:
        user_prompt = input("\n💬 Ask your AI PM Crew anything (or type 'exit' to quit):\n> ")
        
        if user_prompt.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        if not user_prompt.strip():
            continue

        print("\n⏳ The AI PM Team is working on your request...\n")
        
        # Kick off all agents dynamically with your typed query
        result = pm_crew.kickoff(inputs={"user_query": user_prompt})
        
        print("\n" + "="*50)
        print("🎉 FINAL MULTI-AGENT RESPONSE")
        print("="*50)
        print(result)
        print("="*50 + "\n")

if __name__ == "__main__":
    main()