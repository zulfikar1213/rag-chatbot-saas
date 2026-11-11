import os
from dotenv import load_dotenv
from groq import Groq

# Load .env - read GROQ_API_KEY
load_dotenv()

# Connect to Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Iraqi Personality - 2 sentences only!
IRAQI_SYSTEM_PROMPT = """
انت كرسون بالنجف. احكي عراقي بس.

قواعد:
1. جاوب بجملتين بس! مو اكتر!
2. الجملة الاولى: هلا عيوني
3. الجملة الثانية: الجواب + تدلل
4. استعمل بس: هلا عيوني، تدلل، شنو، خوش
5. ممنوع تستعمل: وش، ايش، ابشر، تفضل
6. ممنوع تقول: "هذا المنيو الحقيقي" او "المنيو"
7. ممنوع تقول: "الجواب:" او "عندك سؤال"
8. ممنوع تعيد سؤال الزبون!
9. ممنوع تشرح زيادة!
10. اذا ما بتعرف، قول: ما اعرف عيوني، تدلل خليني اسأل المدير

مثال:
سؤال: بيش برياني الدجاج؟
جواب: هلا عيوني، برياني الدجاج بـ 10 الاف، تدلل

سؤال: عندكم بيتزا؟
جواب: هلا عيوني، لا ما عدنا بيتزا، تدلل
"""

def ask_groq(user_question):
    # 1. Read menu - RAG Retrieval
    try:
        with open("chatbot/menu.txt", "r", encoding="utf-8") as f:
            menu = f.read()
    except:
        menu = "لا يوجد منيو"

    # 2. Build prompt - RAG Augmented - 1 line, clean!
    full_prompt = f"المنيو: {menu} | سؤال الزبون: {user_question} | جاوب بجملتين: هلا عيوني + الجواب + تدلل"

    # 3. Send to Groq - RAG Generation
    response = client.chat.completions.create(
        model="allam-2-7b",
        messages=[
            {"role": "system", "content": IRAQI_SYSTEM_PROMPT},
            {"role": "user", "content": full_prompt},
        ],
        temperature=0.3,
        max_tokens=150,
    )
    return response.choices[0].message.content