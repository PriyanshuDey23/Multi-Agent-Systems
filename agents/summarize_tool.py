from .agent_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        prompt = (
            "You are an AI assistant that summarizes medical texts.\n\n"
            "Please provide a concise summary of the following medical text:\n\n"
            f"{text}\n\n"
            "Summary:"
        )

        messages = [
            {"role": "user", "content": prompt}
        ]
        
        try:
            summary = self.call_llm(messages)
            return summary
        except Exception as e:
            raise ValueError(f"Error during LLM call: {e}")
