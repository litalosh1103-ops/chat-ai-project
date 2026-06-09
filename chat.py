import requests

API_KEY = "YOUR_API_KEY_HERE"
URL = "https://server.iac.ac.il/api/v1/studentapi/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}"}

history = []

print("צ'אט עם AI! כתבי 'יציאה' כדי לסיים.")
print("-" * 40)

while True:
    user_input = input("את: ")
    
    if user_input.strip() == "יציאה":
        print("להתראות!")
        break
    
    history.append({"role": "user", "content": user_input})
    
    payload = {
        "messages": history,
        "max_completion_tokens": 1000
    }
    
    response = requests.post(URL, json=payload, headers=headers)
    result = response.json()
    
    assistant_message = result["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": assistant_message})
    
    print(f"AI: {assistant_message}")
    print("-" * 40)
    