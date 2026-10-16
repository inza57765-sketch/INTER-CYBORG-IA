import requests
from auth import API_URL, token_verif, headers

messages = []
def choice_models(model, user_message):
        
    if token_verif() is None:
        print("Exit")
        exit()


    messages.append({
        "role":"user",
        "content":user_message
    })


    data = {
        "model":model,
        "messages":messages
    }


    response    = requests.post(
        headers = headers,
        url     = API_URL,
        json    = data
    )

    
    if response.status_code == 200:
        
        api_response = response.json()

        model_response = api_response["choices"][0]["message"]["content"]

        print(model_response)

        
        messages.append({
            "role":"assistant",
            "content":model_response
        })
    
    else:
        print(api_response)
