from client import load_key as lk
def solve_math(question):
    obj=lk()
    response=obj.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                'role':"system","content":"you are a math tutor.show step by step solution for the following math problem.",
            },
            {
                'role':"user","content":question
            }
        ]


    )
    return response.choices[0].message.content