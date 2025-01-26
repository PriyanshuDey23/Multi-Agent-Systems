from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    """
    Agent to refine and enhance research article drafts for clarity, coherence, and academic quality.
    """

    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        """
        Refines the given research article draft for improved language, coherence, and academic quality.

        Args:
            draft (str): The research article draft to refine.

        Returns:
            str: The refined research article.
        """

        # Prepare the system and user messages
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert editor who refines and enhances research articles for clarity, coherence, "
                    "and academic quality."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Please refine the following research article draft to improve its language, coherence, "
                    "and overall quality:\n\n"
                    f"{draft}\n\nRefined Article:"
                ),
            },
        ]

        # Call the LLM and return the refined article
        try:
            refined_article = self.call_llm(messages)
            return refined_article
        except Exception as e:
            error_message = f"Failed to refine the draft due to an error: {e}"
            if self.verbose:
                print(error_message)
            raise RuntimeError(error_message)
