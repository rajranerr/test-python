# Requests Module: The requests module is a popular third-party Python library used to send HTTP requests easily to web servers to interact with REST APIs, fetch web data, or perform web scraping. Because it is not a built-in module, you must install it separately before importing it.

# ⚙️ Installation
# Install the package via your terminal using the PyPI package manager: 
# pip install requests

# 🚀 Core Usage & Common HTTP Methods

# 1. GET Request (Retrieving Data): Use requests.get() to request data from a specified resource. You can append URL query strings using the params argument. 
# Ex:
import requests

payload = {'search': 'python', 'page': 1}
response = requests.get('https://httpbin.org', params=payload)

if response.status_code == 200:
    print(response.text)

# 2. POST Request (Sending Data): Use requests.post() to submit data to be processed to a specified resource. Use json for modern APIs or data for form-encoded submissions.
# Ex:
import requests

# Sending a JSON payload
user_data = {'username': 'coder123', 'email': 'test@example.com'}
response = requests.post('https://httpbin.org', json=user_data)

print(response.status_code)