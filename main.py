OPENAI_API_KEY = "sk-**********" 
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = OPENAI_API_KEY

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# story_excerpt = """
#     Once upon a time, in a faraway land,\
#             there lived a brave knight named Sir Arthur.\
#                 He embarked on a perilous quest to rescue a \
#                 captured princess from the clutches of a fearsome dragon
# """

# customer_review_excert = """
# The product is amazing! It exceeded my expectations,\
#       and the customer service was top-notch. \
#         However, the delivery was a bit slow.
# """

# prompt = f"""

# Your task is to Go through the customer reviews and\
#       generate the summary of the review. \
#     From the customer_review_excert delimited by triple quotes \

# review: ```{customer_review_excert}```
# """
#ITERATIVE PROMPT ENGINEERING
prompt1 =f"""
    Write a poem about the night sky.
"""
iteration1 =f"""
    Compose a vivid and enchanting poem about the moon and \
        stars that captivates the reader's imagination.
"""
iteration2 =f"""
    Craft a mesmerizing poem that evokes the beauty of \
        moonlit night, filled with stars that twinkle \
            like diamonds in the dark
"""

iteration3 =f"""
    Write a sonnet that captures the essence of \
        a serene night sky, with the moon as a \
            silent guardian and stars as its shimmering companions.
"""

#SUMMARIZATION
story_excerpt = """
    Once upon a time, in a faraway land,\
            there lived a brave knight named Sir Arthur.\
                He embarked on a perilous quest to rescue a \
                captured princess from the clutches of a fearsome dragon
"""
prompt2=f"""
    Read the story carefully and generate a concise conclusion.
"""

customer_review_excert = """
The product is amazing! It exceeded my expectations,\
      and the customer service was top-notch. \
        However, the delivery was a bit slow.
"""
prompt3=f"""
    Go through the customer reviews and generate the summary of the review.
"""


response = get_completion(prompt1)
# response = get_completion(prompt2)
# response = get_completion(prompt3)
# response = get_completion(iteration1)
# response = get_completion(iteration2)
# response = get_completion(iteration3)


print(response)

