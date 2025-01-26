from .agent_base import AgentBase

class SanitizeDataValidatorAgent(AgentBase):
    """
    Agent to validate the sanitization of medical data by ensuring all Protected Health Information (PHI) is removed.
    """

    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_data, sanitized_data):
        """
        Validates the sanitization of medical data by comparing the original data and the sanitized data.

        Args:
            original_data (str): The original medical data containing PHI.
            sanitized_data (str): The sanitized medical data to validate.

        Returns:
            str: Validation results, including any remaining PHI and a sanitization score.
        """

        # Prepare the messages for the LLM
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI assistant specializing in validating the sanitization of medical data. "
                    "Your task is to check if all Protected Health Information (PHI) has been removed."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Given the original data and the sanitized data, verify that all PHI has been removed.\n"
                    "List any remaining PHI in the sanitized data and rate the sanitization process on a scale of 1 to 5, "
                    "where 5 indicates complete sanitization.\n\n"
                    f"Original Data:\n{original_data}\n\n"
                    f"Sanitized Data:\n{sanitized_data}\n\n"
                    "Validation:"
                ),
            },
        ]

        # Call the LLM to validate the data
        try:
            validation_result = self.call_llm(messages)
            return validation_result
        except Exception as e:
            error_message = f"Failed to validate sanitized data due to an error: {e}"
            if self.verbose:
                print(error_message)
            raise RuntimeError(error_message)
