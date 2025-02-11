import requests

def ask_glm(question):
    api_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "103f067729ac42b2a159f9a66a281dd7.Q2IQv5mgWbidoacD" 
    }
    payload = {
        "model": "chatglm_6b",
        "messages": [{"role": "user", "content": question}]
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result.get("choices")[0].get("message").get("content")
    else:
        print(f"Request failed with status {response.status_code}")
        return None

if __name__ == "__main__":
    question = "1+1是多少"
    answer = ask_glm(question)
    if answer:
        print(f"回答：{answer}")
    else:
        print("未能获取回答")
