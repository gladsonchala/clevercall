import requests
from .github import get_github_user
from .stock import (
    get_current_stock_price,
    get_company_profile,
    get_analyst_recommendations,
)

class ToolManager:
    def __init__(self, account_id, api_token):
        self.account_id = account_id
        self.api_token = api_token
        self.url = f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run/@hf/nousresearch/hermes-2-pro-mistral-7b"
        self.tool_mapping = {
            "getGithubUser": get_github_user,
            "getCurrentStockPrice": get_current_stock_price,
            "getCompanyProfile": get_company_profile,
            "getAnalystRecommendations": get_analyst_recommendations,
        }
        self.tools = self.prepare_tools()

    def prepare_tools(self):
        return [
            {
                "name": "getGithubUser",
                "description": "Fetches publicly available information about a GitHub user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The GitHub username."
                        }
                    },
                    "required": ["username"]
                },
            },
            {
                "name": "getCurrentStockPrice",
                "description": "Get the current stock price for a given symbol.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "The stock symbol."
                        }
                    },
                    "required": ["symbol"]
                },
            },
            {
                "name": "getCompanyProfile",
                "description": "Get the company profile for a given symbol.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "The stock symbol."
                        }
                    },
                    "required": ["symbol"]
                },
            },
            {
                "name": "getAnalystRecommendations",
                "description": "Get analyst recommendations for a given stock symbol.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "The stock symbol."
                        }
                    },
                    "required": ["symbol"]
                },
            },
        ]

    def process_query(self, user_query):
        payload = {
            "messages": [{"role": "user", "content": user_query}],
            "tools": self.tools,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}",
        }

        response = requests.post(self.url, json=payload, headers=headers)
        print("Cloudflare API Response:", response.text)

        if response.status_code == 200:
            data = response.json()
            tool_calls = data.get("result", {}).get("tool_calls", [])

            for tool_call in tool_calls:
                tool_name = tool_call.get("name")
                arguments = tool_call.get("arguments", {})
                result = self.call_tool(tool_name, arguments)
                print(f"Result from {tool_name}: {result}")
        else:
            print("Error calling Cloudflare API:", response.status_code, response.text)

    def call_tool(self, tool_name, arguments):
        """
        Dynamically call a tool function based on the tool name.

        Args:
            tool_name (str): Name of the tool to call.
            arguments (dict): Arguments to pass to the tool.

        Returns:
            Result from the tool function or an error message.
        """
        func = self.tool_mapping.get(tool_name)
        if func:
            return func.invoke(input=arguments)
        return {"error": f"Tool '{tool_name}' not found."}
