from client import load_key as lk
def analyze_review(review):
    obj=lk()
    response=obj.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                'role':"system","content":"you analyze the sentiment of the following review.",
            },
            {
                'role':"user","content":review
            }
        ]


    )
    return response.choices[0].message.content