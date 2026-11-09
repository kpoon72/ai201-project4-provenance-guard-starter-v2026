"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

How each criterion is tested (criteria.md):

    1. No false accusations   "my own writing" — 10 pieces I wrote myself.
    2. Score spread           "clearly AI" vs "clearly human" — 5 and 5.
    3. Label coverage         every text scenario below counts; the borderline
                              set is there to land in the middle of the range.
    4. Appeals                not here: run_eval.py only calls /submit. Tested
                              by eval_appeals.py, three trials of 5 appeals.
    5. Bad input              "bad input" — raw bodies. The two bodies that
                              aren't a JSON object can't be sent by run_eval.py
                              (it always sends JSON), so eval_appeals.py sends
                              those as well.
"""

# Ten pieces I wrote myself. Not AI text, not samples from the web.
MY_WRITING = [
    'Last weekend, I spent some time relaxing and taking care of things around the house. I also worked on a few personal projects and caught up with friends. I enjoy having a productive weekend, but I also like taking some time for myself to recharge before starting another busy week.',

    'One of my favorite foods is butter chicken. I love the combination of creamy tomato sauce, spices, and tender chicken. I enjoy Nepali and Indian food because of the rich flavors and different spices. I also like cooking at home because I can experiment with ingredients and adjust the flavors to my taste.',

    "One place I remember very well is Nepal, where I grew up. Even though I've been living in the United States for many years, Nepal will always have a special place in my heart. I have so many memories of my childhood, family, friends, food, and culture. Whenever I think about Nepal, I feel connected to my roots.",

    "Something annoying that happened recently was having to change my travel plans. I was hoping to travel to Canada and visit some friends, but due to some personal circumstances and legal advice, I had to postpone the trip. I was really looking forward to seeing everyone, so it was disappointing. But sometimes things don't go as planned, and we just have to be patient.",

    "I'm a software developer, and I work for a software company called Paycom. My job mainly involves developing and maintaining enterprise applications. I work with technologies like PHP, JavaScript, TypeScript, React, and APIs.\n\nA typical weekday starts with checking emails, reviewing tasks, and attending team meetings. Then I spend most of my time writing code, debugging issues, reviewing pull requests, and collaborating with other developers. After work, I usually spend some time learning new technologies, cooking, or working on personal projects.",

    "My parents are among the most important people in my life. They have always supported me and encouraged me to work hard and build a better future. They taught me the importance of family, respect, kindness, and responsibility.\n\nAs I've grown older, I've realized how much they have sacrificed for their children. I may not always agree with everything they say, but I will always respect and appreciate them.",

    "One important skill I learned is software development. I started learning programming during my college years, and gradually developed my skills through education, practice, and real-world experience.\n\nI completed my master's degree in computer science and started working professionally as a software developer. Most importantly, I learned that programming is not just about writing code. It's about understanding problems, thinking logically, and finding efficient solutions. I'm still learning something new every day.",

    "If I had a completely free day with no responsibilities, I would probably start my morning slowly with a nice cup of coffee and a good breakfast. Then I might go somewhere for a drive, explore a new place, or spend time with friends.\n\nI also enjoy cooking, so I might prepare something special at home. In the evening, I would probably watch a movie or relax. I think the best free day is one where you don't have to worry about time or responsibilities.",

    "I really enjoy watching football, especially NFL games. My favorite team is the Dallas Cowboys. I enjoy watching football because it's not just about the game itself. It's also about teamwork, strategy, competition, and the excitement of the fans.\n\nEven when the Cowboys don't play well, I still enjoy supporting them. Being a fan means staying loyal through both wins and losses!",

    'One thing I really want to do in the next year is continue growing professionally and personally. I want to improve my technical skills, especially in cloud computing, artificial intelligence, and automation.\n\nI also want to focus on my health and fitness, travel more when circumstances allow, and spend quality time with family and friends. My goal is to become a better version of myself, both personally and professionally.',
]

# Generated by Claude for this test, unedited.
CLEARLY_AI = [
    "Effective time management is essential for success in both academic and "
    "professional settings. By prioritizing tasks, setting clear goals, and "
    "minimizing distractions, individuals can significantly improve their "
    "productivity. Additionally, taking regular breaks helps maintain focus and "
    "prevents burnout. Ultimately, developing strong time management skills "
    "leads to reduced stress and better overall outcomes.",

    "Climate change is one of the most pressing challenges facing the world "
    "today. Rising global temperatures have led to more frequent extreme weather "
    "events, melting ice caps, and rising sea levels. Addressing this issue "
    "requires coordinated action from governments, businesses, and individuals. "
    "By investing in renewable energy and sustainable practices, we can work "
    "toward a healthier planet for future generations.",

    "Reading offers numerous benefits for people of all ages. It enhances "
    "vocabulary, improves concentration, and fosters empathy by allowing readers "
    "to experience different perspectives. Furthermore, reading can serve as a "
    "valuable source of relaxation and stress relief. In today's digital age, "
    "cultivating a regular reading habit remains as important as ever.",

    "Teamwork plays a crucial role in achieving organizational goals. When team "
    "members collaborate effectively, they can leverage diverse skills and "
    "perspectives to solve complex problems. Clear communication, mutual "
    "respect, and shared accountability are key components of successful "
    "teamwork. Organizations that foster a collaborative culture often see "
    "higher employee satisfaction and improved performance.",

    "Regular physical exercise provides a wide range of health benefits. It "
    "strengthens the cardiovascular system, helps maintain a healthy weight, and "
    "boosts mental well-being. Experts recommend at least 150 minutes of "
    "moderate activity per week. Incorporating exercise into a daily routine can "
    "lead to increased energy levels and a higher quality of life.",
]

# The five pieces of my own writing I judge most clearly human.
CLEARLY_HUMAN = MY_WRITING[:5]

# AI text reworded casually by hand, meant to land between the two bands.
BORDERLINE = [
    "Managing your time well matters a lot, at school and at work. If you sort "
    "out what's most important, set goals, and cut down on distractions, you get "
    "way more done. Breaks help too, they keep you focused and stop you burning "
    "out. In the end, being good with time means less stress and better results.",

    "Exercise is good for you in lots of ways. Your heart gets stronger, it's "
    "easier to keep a healthy weight, and you feel better mentally. Most experts "
    "say aim for about 150 minutes a week of moderate stuff. If you make it part "
    "of your day you'll probably have more energy and just feel better overall.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        "name": "c2 clearly AI",
        "criterion": 2,
        "texts": CLEARLY_AI,
    },
    {
        "name": "c2 clearly human",
        "criterion": 2,
        "texts": CLEARLY_HUMAN,
    },
    {
        "name": "c3 borderline",
        "criterion": 3,
        "texts": BORDERLINE,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t ", "creator_id": "eval_bad_space"},
            {"text": 42, "creator_id": "eval_bad_number"},
            {"text": ["a", "b"], "creator_id": "eval_bad_list"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 2001, "creator_id": "eval_bad_huge"},
            {"text": "A real sentence with no creator attached to it."},
            {"text": "A real sentence with an empty creator.", "creator_id": ""},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
