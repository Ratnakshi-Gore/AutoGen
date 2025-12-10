import os
from dotenv import load_dotenv

# llm_config = {"config_list": [{"model": "gpt-4", "api_key" : os.environ.get("OPENAI_API_KEY")}]}

load_dotenv()

llm_config = {
    "config_list": [
        {
            "model": "llama3.2", 
            "api_key": os.getenv("OLLAMA_API_KEY", "ollama"),
            "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
            "api_type": "openai",  
            "price": [0, 0]
        }
    ]
}