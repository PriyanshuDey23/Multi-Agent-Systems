from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    """
    Tool to sanitize medical data by removing Protected Health Information (PHI).
    """

    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        """
        Sanitizes the given medical data by removing all Protected Health Information (PHI).

        Args:
            medical_data (str): The medical data to sanitize.

        Returns:
            str: The sanitized data with all PHI removed.
        """

        # Prepare the messages for the LLM
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI assistant specializing in sanitizing medical data by removing Protected Health "
                    "Information (PHI)."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Please sanitize the following medical data by removing all PHI:\n\n"
                    f"{medical_data}\n\nSanitized Data:"
                ),
            },
        ]

        # Call the LLM to sanitize the data
        try:
            sanitized_data = self.call_llm(messages)
            return sanitized_data
        except Exception as e:
            error_message = f"Failed to sanitize medical data due to an error: {e}"
            if self.verbose:
                print(error_message)
            raise RuntimeError(error_message)
