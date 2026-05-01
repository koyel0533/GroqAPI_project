from client import load_key as lk
def summarize_text(text):
    obj=lk()
    response=obj.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                'role':"system","content":"summarize the following text 2 sentences.",
            },
            {
                'role':"user","content":text
            }
        ]


    )
    return response.choices[0].message.content