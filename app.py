import streamlit as st
from agents import AgentManager
from utils.logger import logger
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

def main():
    st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
    st.title("Multi-Agent AI System with Collaboration and Validation")

    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox(
        "Choose a task:", 
        ["Summarize Medical Text", "Write and Refine Research Article", "Sanitize Medical Data (PHI)"]
    )

    agent_manager = AgentManager(max_retries=2, verbose=True)

    if task == "Summarize Medical Text":
        render_summarize_section(agent_manager)
    elif task == "Write and Refine Research Article":
        render_write_refine_section(agent_manager)
    elif task == "Sanitize Medical Data (PHI)":
        render_sanitize_section(agent_manager)

def render_summarize_section(agent_manager):
    st.header("Summarize Medical Text")
    text = st.text_area("Enter medical text to summarize:", height=200)

    if st.button("Summarize"):
        if not text.strip():
            st.warning("Please enter some text to summarize.")
            return

        try:
            with st.spinner("Summarizing..."):
                # Get agents for summarizing and validation
                main_agent = agent_manager.get_agent("summarize")
                validator_agent = agent_manager.get_agent("summarize_validator")

                # Execute the summarize and validation processes
                summary = main_agent.execute(text)
                st.subheader("Summary:")
                st.write(summary)

                validation = validator_agent.execute(original_text=text, summary=summary)
                st.subheader("Validation:")
                st.write(validation)
        except Exception as e:
            logger.error(f"Error in summarizing: {e}")
            st.error(f"An error occurred: {e}")

def render_write_refine_section(agent_manager):
    st.header("Write and Refine Research Article")
    topic = st.text_input("Enter the topic for the research article:")
    outline = st.text_area("Enter an outline (optional):", height=150)

    if st.button("Write and Refine Article"):
        if not topic.strip():
            st.warning("Please enter a topic for the research article.")
            return

        try:
            with st.spinner("Writing article..."):
                # Get agents for writing, refining, and validation
                writer_agent = agent_manager.get_agent("write_article")
                refiner_agent = agent_manager.get_agent("refiner")
                validator_agent = agent_manager.get_agent("validator")

                # Execute the write, refine, and validation processes
                draft = writer_agent.execute(topic, outline)
                st.subheader("Draft Article:")
                st.write(draft)

                refined_article = refiner_agent.execute(draft)
                st.subheader("Refined Article:")
                st.write(refined_article)

                validation = validator_agent.execute(topic=topic, article=refined_article)
                st.subheader("Validation:")
                st.write(validation)
        except Exception as e:
            logger.error(f"Error in write and refine flow: {e}")
            st.error(f"An error occurred: {e}")

def render_sanitize_section(agent_manager):
    st.header("Sanitize Medical Data (PHI)")
    medical_data = st.text_area("Enter medical data to sanitize:", height=200)

    if st.button("Sanitize Data"):
        if not medical_data.strip():
            st.warning("Please enter medical data to sanitize.")
            return

        try:
            with st.spinner("Sanitizing data..."):
                # Get agents for sanitization and validation
                main_agent = agent_manager.get_agent("sanitize_data")
                validator_agent = agent_manager.get_agent("sanitize_data_validator")

                # Execute the sanitization and validation processes
                sanitized_data = main_agent.execute(medical_data)
                st.subheader("Sanitized Data:")
                st.write(sanitized_data)

                validation = validator_agent.execute(original_data=medical_data, sanitized_data=sanitized_data)
                st.subheader("Validation:")
                st.write(validation)
        except Exception as e:
            logger.error(f"Error in sanitizing data: {e}")
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
