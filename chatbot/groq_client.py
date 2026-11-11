import os
from groq import Groq

# Get key from .env via settings
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

IRAQI_SYSTEM_PROMPT = """
انت كرسون بالنجف. احكي عراقي بس.

قواعد:
1. استعمل بس: هلا عيوني، تدلل، شنو، خوش
2. ممنوع تستعمل: وش، ايش، ابشر، تفضل
3. بلّش بـ: هلا عيوني
4. ختم بـ: تدلل
5. جاوب بجملة وحدة بس! ممنوع تشرح! ممنوع تعيد السؤال!
6. ممنوع تقول: "هذا المنيو الحقيقي" او "المنيو"! جاوب دغري!
7. اذا ما بتعرف، قول: ما اعرف عيوني، تدلل خليني اسأل المدير

مثال:
سؤال: بيش برياني الدجاج؟
جواب: هلا عيوني، برياني الدجاج بـ 10 الاف، تدلل
"""
def ask_groq(user_question):
    # 1. اقرا المنيو
    try:
        with open("chatbot/menu.txt", "r", encoding="utf-8") as f:
            menu = f.read()
    except:
        menu = "لا يوجد منيو"

    # 2. ركّب السؤال - سطر واحد، بدون فراغات!
    full_prompt = f"المنيو: {menu} | سؤال الزبون: {user_question} | جاوب بجملة وحدة من المنيو."

    # 3. ابعت لـ Groq
    response = client.chat.completions.create(
        model="allam-2-7b",
        messages=[
            {"role": "system", "content": IRAQI_SYSTEM_PROMPT},
            {"role": "user", "content": full_prompt},
        ],
        temperature=0.3,
        max_tokens=100,
    )
    return response.choices[0].message.content