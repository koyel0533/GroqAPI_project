from client import load_key as lk
def extract_skills(text):
    obj=lk()
    response=obj.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                'role':"system","content":"extract professional and technical skills from resume and return in list format.",
            },
            {
                'role':"user","content":text
            }
        ]


    )
    return response.choices[0].message.content