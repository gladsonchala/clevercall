from config import account_id, api_token, url
from tools.tool_manager import ToolManager

def main():
    user_query = "What is the current price of AAPL?"
    tool_manager = ToolManager(account_id, api_token)
    tool_manager.process_query(user_query)

if __name__ == "__main__":
    main()
