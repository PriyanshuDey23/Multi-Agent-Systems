from .agent_base import AgentBase

class SummarizeValidatorAgent(AgentBase):
    """
    Agent to validate the quality of summaries of medical texts.
    """

    def __init__(self, max_retries=2, verbose=True):
        """
        Initializes the SummarizeValidatorAgent.

        Args:
            max_retries (int): Maximum number of retries for LLM calls.
            verbose (bool): Flag to enable verbose logging.
        """
        super().__init__(name="SummarizeValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_text, summary):
        """
        Validates the quality of a summary against the original text.

        Args:
            original_text (str): The original medical text.
            summary (str): The summary of the medical text.

        Returns:
            str: The validation result from the LLM.
        """

        # Prepare the system message
        system_message = "You are an AI assistant that validates summaries of medical texts."

        # Prepare the user content message
        user_content = (
            "Given the original text and its summary, assess whether the summary accurately and concisely captures the key points of the original text.\n"
            "Provide a brief analysis and rate the summary on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Original Text:\n{original_text}\n\n"
            f"Summary:\n{summary}\n\n"
            "Validation:"
        )

        # Format messages for Gemini
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        # Call the LLM and return the validation result
        validation = self.call_llm(messages)
        return validation
