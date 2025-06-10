# nlp/response_generator.py

import openai
import logging
import os

class GPTResponse:
    def __init__(self, model="gpt-3.5-turbo-instruct", max_tokens=150, temperature=0.7):
        """
        Initialize the GPT response generator.

        Args:
            model (str): GPT model to use (default: 'gpt-3.5-turbo-instruct').
            max_tokens (int): Maximum tokens for the generated response.
            temperature (float): Sampling temperature for response diversity.
        """
        logging.info("Initializing GPT Response Generator")

        # Retrieve API key from environment variables
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key not found. Set the OPENAI_API_KEY environment variable."
            )
        openai.api_key = self.api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def generate_response(self, user_input: str, context: str = "") -> str:
        """
        Generate a response based on user input and context.

        Args:
            user_input (str): The user's input text.
            context (str): Optional additional context to provide to the model.

        Returns:
            str: Generated response text.
        """
        try:
            logging.info("Generating response from GPT model")
            prompt = self._build_prompt(user_input, context)

            response = openai.Completion.create(
                model=self.model,
                prompt=prompt,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                n=1,
                stop=["\n"]
            )
            return response.choices[0].text.strip()
        except openai.error.AuthenticationError:
            logging.error("Authentication error: Invalid API key.")
            return "Authentication error: Please check your API key."
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "I'm sorry, I couldn't generate a response at the moment."

    def _build_prompt(self, user_input: str, context: str) -> str:
        """
        Construct the prompt for the GPT model.

        Args:
            user_input (str): The user's input text.
            context (str): Optional additional context.

        Returns:
            str: A well-formatted prompt for GPT.
        """
        base_prompt = (
            "You are an advanced virtual assistant. Respond to the user's query accurately and concisely.\n"
            "Context: {context}\n"
            "User: {user_input}\n"
            "Assistant:"
        )
        return base_prompt.format(
            context=context if context else "No additional context",
            user_input=user_input
        )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example usage
    try:
        gpt = GPTResponse()

        user_query = "Can you tell me about the weather today?"
        additional_context = "This assistant provides weather updates and general advice."

        response = gpt.generate_response(user_query, additional_context)
        print("GPT Response:", response)
    except ValueError as e:
        logging.error(f"Initialization error: {e}")
