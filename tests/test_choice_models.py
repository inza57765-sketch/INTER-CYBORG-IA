from core import choice_models

while True:
    user_msg = input("> ")
    print(choice_models(model="openai/gpt-oss-120b", user_message=user_msg))