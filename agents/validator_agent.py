from .agent_base import AgentBase

class ValidatorAgent(AgentBase):
    """
    An agent to validate research articles for accuracy, completeness, and adherence to academic standards.
    """

    def __init__(self, max_retries=2, verbose=True):
        """
        Initializes the ValidatorAgent.

        Args:
            max_retries (int): Maximum number of retries for LLM calls.
            verbose (bool): Flag to enable verbose logging.
        """
        super().__init__(name="ValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, article):
        """
        Validates the research article based on its accuracy, completeness, and academic standards.

        Args:
            topic (str): The topic of the research article.
            article (str): The research article to be validated.

        Returns:
            str: The validation result from the LLM.
        """

        # Prepare the system message
        system_message = (
            "You are an AI assistant that validates research articles for accuracy, completeness, and adherence to academic standards."
        )

        # Prepare the user content message
        user_content = (
            "Given the topic and the research article below, assess whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Topic: {topic}\n\n"
            f"Article:\n{article}\n\n"
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
