"""
Random Joke Generator
Fetches jokes from an external API and displays them.
"""

import requests
import json
from typing import Dict, Optional

class JokeGenerator:
    """A class to generate random jokes using external APIs."""
    
    def __init__(self):
        """Initialize the joke generator with API endpoints."""
        self.jokes_api_url = "https://official-joke-api.appspot.com/random_joke"
        self.useless_api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    def get_random_joke(self) -> Optional[Dict]:
        """
        Fetch a random joke from the Official Joke API.
        
        Returns:
            Dict: A dictionary containing joke setup and punchline
            None: If the API call fails
        """
        try:
            response = requests.get(self.jokes_api_url, timeout=5)
            response.raise_for_status()
            joke_data = response.json()
            return {
                "type": "joke",
                "setup": joke_data.get("setup", ""),
                "punchline": joke_data.get("punchline", ""),
                "id": joke_data.get("id", "")
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    def get_useless_fact(self) -> Optional[Dict]:
        """
        Fetch a random useless fact from the API.
        
        Returns:
            Dict: A dictionary containing a random fact
            None: If the API call fails
        """
        try:
            response = requests.get(self.useless_api_url, timeout=5)
            response.raise_for_status()
            fact_data = response.json()
            return {
                "type": "fact",
                "fact": fact_data.get("text", ""),
                "source_url": fact_data.get("source_url", "")
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching fact: {e}")
            return None
    
    def display_joke(self, joke: Dict) -> None:
        """
        Display a joke in a formatted way.
        
        Args:
            joke (Dict): Joke data containing setup and punchline
        """
        if joke:
            print("\n" + "="*50)
            print("🎭 JOKE OF THE DAY 🎭")
            print("="*50)
            print(f"\n📝 Setup: {joke.get('setup', 'N/A')}")
            print(f"\n😂 Punchline: {joke.get('punchline', 'N/A')}")
            print("\n" + "="*50 + "\n")
    
    def display_fact(self, fact: Dict) -> None:
        """
        Display a fact in a formatted way.
        
        Args:
            fact (Dict): Fact data
        """
        if fact:
            print("\n" + "="*50)
            print("🧠 USELESS FACT 🧠")
            print("="*50)
            print(f"\n💡 Fact: {fact.get('fact', 'N/A')}")
            if fact.get('source_url'):
                print(f"📚 Source: {fact.get('source_url')}")
            print("\n" + "="*50 + "\n")


def main():
    """Main function to demonstrate the joke generator."""
    generator = JokeGenerator()
    
    print("\n🎉 Welcome to the Random Joke & Fact Generator! 🎉\n")
    
    # Fetch and display a joke
    print("Fetching a random joke...")
    joke = generator.get_random_joke()
    generator.display_joke(joke)
    
    # Fetch and display a fact
    print("Fetching a random fact...")
    fact = generator.get_useless_fact()
    generator.display_fact(fact)
    
    # Generate multiple jokes
    print("\n📊 Generating 3 random jokes:\n")
    for i in range(1, 4):
        joke = generator.get_random_joke()
        if joke:
            print(f"{i}. Setup: {joke.get('setup')}")
            print(f"   Punchline: {joke.get('punchline')}\n")


if __name__ == "__main__":
    main()
