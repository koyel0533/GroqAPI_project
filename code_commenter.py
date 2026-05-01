from client import load_key as lk
def add_comments(code):
    obj=lk()
    response=obj.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                'role':"system","content":"add meaningfull python comments.",
            },
            {
                'role':"user","content":code
            }
        ]


    )
    return response.choices[0].message.content