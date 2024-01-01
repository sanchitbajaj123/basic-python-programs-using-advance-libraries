import openai
#open ai connected with openai website and got a key 
openai.api_key = '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'
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003', 
        prompt=message,
        max_tokens=100,  
        n=1,
        stop=None,
        temperature=0.7
    )
    reply = response.choices[0].text.strip()
    return reply

message =input("enter your query=")
reply = send_message(message)
print(reply)
