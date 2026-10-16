from auth import token_verif

if token_verif() is not None:
    print("Token Ok.")
    print("--------------------------")
    print("TOKEN :", token_verif())
    print("--------------------------")
    
else:
    print("Token Introuvable.")
    print(token_verif())