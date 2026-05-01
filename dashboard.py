import summarizer
from chatbot import chat_with_ai
from code_commenter import add_comments
from image_generator import generate_image
from math_tutor import solve_math
from sentiment_analyzer import analyze_review
from skill_extractor import extract_skills
from translator import  change_text
def main():
    while True:
        print("\n== openai multi Tool app ===========")
        print("1.summarize text")
        print("2. chatBot ")
        print("3.comment python code")
        print("4.generate image")
        print("5.solve math problem")
        print("6.analyze review sentiment")
        print("7.extract skills from resume")
        print("8.translate text")
        print("9.exit")

        choice=input("enter your choice:")

        if choice=='1':
            text=input("enter text : ")
            print("\n summarized text : ",summarizer.summarize_text(text))
        elif choice=='2':
            print("\n starting chatbot... ")
            chat_with_ai()
        elif choice=='3':
            code=input("enter python code : ")
            print("\n commented code : ",add_comments(code))
        elif choice=='4':
        
            print("\n generated image url : ",generate_image())
        elif choice=='5':
            question=input("enter math problem : ")
            print("\n solution : ",solve_math(question))
        elif choice=='6':
            review=input("enter product review : ")
            print("\n sentiment analysis : ",analyze_review(review))
        elif choice=='7':
            resume=input("paste resume text : ")
            print("\n extracted skills : ",extract_skills(resume))
        elif choice=='8':
            text=input("enter text to translate : ")
            print("\n translated text : ",change_text(text))
        elif choice=='9':
            print("============================Goodbye!===================")
            break
        else:
                print("invalid choice. please try again.")
if __name__=="__main__":
    main()
