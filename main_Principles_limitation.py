OPENAI_API_KEY = "sk-*********************" 
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


prompt = f"""
***Create a Structured Recipe for a Delicious Fruit Smoothie***  #Tactic 1#
***Instructions:*** #Tactic 1#
1. Use the following structure for your recipe:
     Recipe for [Name of the Smoothie]
      Ingredients:
       - [List of ingredients, separated by commas]
   Instructions: #Tactic 2#
   1. [Step 1: Describe the first step] 
   2. [Step 2: Describe the second step]
   3. [Step 3: Describe the third step]
   ...
   Enjoy your [Name of the Smoothie]!

2. Create a fruit smoothie recipe, with a specific focus on a tropical theme.

3.Include  at least three tropical fruits (e.g., mango, pineapple, banana) among the ingredients. #Tactic 3#

4. Sample smoothie names that convey a tropical or exotic vibe.

5. Prioritize creativity and originality in the recipe's content, and feel free to add personal touches to make it unique. #Give model time to think #

***Few-shot prompting for inspiration:*** #Tactic 4#
Few-shot 1: "Create a smoothie name with a tropical feel."
Few-shot 2: "Suggest a name that evokes an island paradise."
"""

response = get_completion(prompt)
print(response)
