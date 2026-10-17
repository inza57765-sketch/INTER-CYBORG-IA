import requests
from auth import API_URL, token_verif, headers

messages = []
def choice_models(model, user_message):
    if token_verif() is None:
        return "Token Introuvable."


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

    api_response = response.json()
    if response.status_code == 200:

        model_response = api_response["choices"][0]["message"]["content"]
        
        messages.append({
            "role":"assistant",
            "content":model_response
        })
        return model_response
    
    else:
        return api_response