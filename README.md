# CleverCall

CleverCall is a powerful tool that leverages Cloudflare's AI capabilities to perform function calling and retrieve dynamic information. It integrates with various APIs to fetch user data from GitHub and stock information from Yahoo Finance, providing an efficient way to interact with APIs using natural language.

## Features

- **GitHub User Info**: Fetch publicly available information about any GitHub user.
- **Stock Information**: Get real-time stock prices, company profiles, and analyst recommendations.
- **Cloudflare AI Integration**: Use Cloudflare's AI model to process user queries and call the appropriate functions dynamically.

## Getting Started

### Prerequisites

- Python 3.x
- Install the required packages:
  ```bash
  pip install requests yfinance langchain
  ```

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/gladsonchala/clevercall.git
   cd clevercall
   ```

2. Update your Cloudflare account details in the code:
   - Replace `account_id` and `api_token` with your Cloudflare account credentials.

### Usage

Run the main script to start using CleverCall:

```bash
python main.py
```

You can customize the `user_query` variable in `main.py` to test different queries, such as:

```python
user_query = "Get information about the GitHub user 'octocat'."
```

### Available Tools

- **get_github_user(username)**: Fetches information about a GitHub user by username.
- **get_current_stock_price(symbol)**: Retrieves the current stock price for a given stock symbol.
- **get_company_profile(symbol)**: Provides the company profile for a specified stock symbol.
- **get_analyst_recommendations(symbol)**: Returns analyst recommendations for a specific stock.

### Example Queries

- Fetch GitHub user info:
  ```python
  user_query = "Get information about the GitHub user 'octocat'."
  ```

- Get current stock price:
  ```python
  user_query = "What is the current price of AAPL?"
  ```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries, feel free to reach out to [gladsonchala@gmail.com](mailto:gladsonchala@gmail.com).

---

CleverCall makes API interactions seamless and intuitive. Enjoy exploring its features!
