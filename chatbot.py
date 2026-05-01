from client import load_key as lk
def chat_with_ai():
    obj=lk()
    
    messages=[
            {
                'role':"system","content":"you are a friendly assistant.",
            },
           
        ]
    
    print("chatbot type exit to create")
    while True:
        user_input=input("you:")
        if user_input.lower()=='exit':
            break
        messages.append({"role":"user","content":user_input})
        
    response=obj.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages)
    reply=response.choices[0].message.content
    print("AI: ",reply)
    messages.append({"role":"assistant","content":reply})