from langchain_google_genai import ChatGoogleGenerativeAI
from abc import ABC, abstractmethod
from loguru import logger
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY is not set in the environment.")



class AgentBase(ABC):
    """
    Base class for AI agents using Google Gemini.
    """

    def __init__(self, name, model="gemini-2.0-flash", max_retries=3, verbose=True):
        self.name = name
        self.model = model
        self.max_retries = max_retries
        self.verbose = verbose
        self.llm = ChatGoogleGenerativeAI(model=self.model, api_key=GOOGLE_API_KEY)

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Abstract method to be implemented by child classes for specific tasks.
        """
        pass

    def call_llm(self, messages):
        """
        Calls the Google Gemini LLM with the given messages.
        """
        retries = 0 # Start

        while retries < self.max_retries:
            try:
                #  format the prompt based on messages
                prompt = ""
                for msg in messages:
                    prompt += f"{msg['role']}: {msg['content']}\n" # Parse the output
                
                if self.verbose:
                    logger.info(f"[{self.name}] Sending prompt to LLM: {prompt}")

                # Response
                response = self.llm.predict(prompt)  

                
                if response:
                    if self.verbose:
                        logger.info(f"[{self.name}] Received response: {response}")
                    return response

                raise ValueError("Empty response from Generative AI API.")

            except Exception as e:
                logger.error(f"[{self.name}] Error during LLM call: {e}. Retry {retries + 1}/{self.max_retries}")
                retries += 1

        # If retries are exhausted, raise an exception
        error_message = f"[{self.name}] Failed to get a valid response after {self.max_retries} retries."
        logger.critical(error_message)
        raise RuntimeError(error_message)


