from .agent_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="WriteArticleTool", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):
        # Prepare the system and user messages
        system_message = "You are an expert academic writer."
        user_content = f"Write a research article on the following topic:\nTopic: {topic}\n\n"
        
        if outline:
            user_content += f"Outline:\n{outline}\n\n"
        
        user_content += "Article:\n"

        # Now structure the messages for LLM
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        try:
            # This assumes `call_llm` is a method that processes the messages in the correct format
            article = self.call_llm(messages)
            return article
        except Exception as e:
            # Log and raise error if LLM fails
            raise ValueError(f"Error during LLM call: {e}")
