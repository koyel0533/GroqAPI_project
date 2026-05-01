from client import load_key as lk
def change_text(text,lang=input("enter target language : ")):
    obj=lk()
    response=obj.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                'role':"system","content":f"translate the following text in the language {lang}:"
            },
            {
                'role':"user","content":text
            }
        ]


    )
    return response.choices[0].message.content