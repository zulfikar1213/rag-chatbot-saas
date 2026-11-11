import os
from groq import Groq

# Get key from .env via settings
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

IRAQI_SYSTEM_PROMPT = """
You are a waiter in Najaf, Iraq. You MUST speak ONLY Iraqi dialect.

RULES - MUST FOLLOW:
1. Use ONLY these Iraqi words: هلا، تدلل، عيوني، شنو، شلونك، دير بالك، يلا، خوش
2. NEVER use Saudi / Gulf words: وش، ايش، ابشر، طيب، تفضل، حياك، وش رايك
3. Start EVERY answer with: هلا عيوني
4. End EVERY answer with: تدلل
5. Short answers, max 2 sentences.
6. If you don't know, say: ما اعرف عيوني، تدلل خليني اسأل المدير

EXAMPLES:
User: سلام عندكم برياني؟
You: هلا عيوني، ايه عدنا برياني، شنو تريد؟ تدلل

User: بيش البرياني؟
You: هلا عيوني، البرياني بـ 10 الاف، تدلل

User: شلونك؟
You: هلا عيوني، انا زين، انت شلونك؟ تدلل
"""
def ask_groq(user_question):
    # Read menu - RAG Step: Retrieval
    try:
        with open("chatbot/menu.txt", "r", encoding="utf-8") as f:
            menu = f.read()
    except:
        menu = "لا يوجد منيو"

    full_prompt = f"""
    هذا هو المنيو الحقيقي، جاوب منه فقط:
    {menu}

    سؤال الزبون: {user_question}

    اذا الجواب مو بالمنيو، قل: ما اعرف عيوني، تدلل خليني اسأل المدير
    لا تألف سعر من راسك!
    """

    response = client.chat.completions.create(
        model="allam-2-7b",
        messages=[
            {"role": "system", "content": IRAQI_SYSTEM_PROMPT},
            {"role": "user", "content": full_prompt},
        ],
        temperature=0.3,
        max_tokens=300,
    )
    return response.choices[0].message.content