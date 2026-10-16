from .token_auth import token_verif
headers = {
    "Authorization":f"Bearer {token_verif()}",
    "Content-Type":"application/json"
}
