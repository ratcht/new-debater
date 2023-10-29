from models import DebatorAI
from apiopenai import *
from speech import *
from fakeyou import *
from api import api_key

organization = "org-XFRiKEA3bXXTSifH2T4XNFwX"

authenticate(api_key, organization)

topic = input("Enter the debate topic: ")

pro_ai = DebatorAI(topic, "For", "Donald Trump")
neg_ai = DebatorAI(topic, "Against", "Joe Biden")

print("\n\n------DEBATE START------\n\n")

current = ""

def add_next(current, stage, team, response):
  str = f"\nStage: {stage}: Team {team}:\nReponse:\n{response}\n\n"
  print(f"-----Team {team}-----\n")
  print(f"{response}\n\n")
  current += str
  return current

# stage of debate

# STAGE 1A
stage_1a = "1a. Team For presents the affirmative position: 2 sentences. You will write very concisely. The argument (s) is introduced. Evidence is submitted to support the argument"

print("Stage 1. Presentations\n")
pro_1 = pro_ai.query(stage_1a, current)

current = add_next(current, "1A", "For", pro_1)


# STAGE 1B
stage_1b = "1b. Team Against presents the negative position: 2 sentences. You will write very concisely. The argument is introduced. Evidence is submitted to support the argument. No direct response is made to Team One"


neg_1 = neg_ai.query(stage_1b, current)

current = add_next(current, "1B", "Against", neg_1)


# STAGE 2A
stage_2a = "2a. Team For reintroduces the affirmative position: 2 sentences. You will write very concisely. Secondary arguments are introduced. More evidence is submitted. The negative position's evidence and arguments are rebutted (anticipate!)"

pro_2 = pro_ai.query(stage_2a, current)

current = add_next(current, "2A", "For", pro_2)


# STAGE 2B
stage_2b = "2b. Team Against reintroduces the negative position: 2 sentences. You will write very concisely. Secondary arguments are introduced. More evidence is submitted. The affirmative position's evidence and arguments are rebutted (anticipate!)"

neg_2 = neg_ai.query(stage_2b, current)

current = add_next(current, "2B", "Against", neg_2)

# Stage 3A
stage_3a = "Team For rebuttal: 2 sentences. You will write very concisely. Respond directly to opposing team arguments. Sum up key points of your team position"

pro_3 = pro_ai.query(stage_3a, current)

current = add_next(current, "3A", "For", pro_3)


# Stage 3B
stage_3b = "Team Against rebuttal: 2 sentences. You will write very concisely. Respond directly to opposing team arguments. Sum up key points of your team position "

neg_3 = neg_ai.query(stage_3b, current)

current = add_next(current, "3B", "Against", neg_3)

# Come to a conclusion
pro_4 = pro_ai.conclusion(current)

current = add_next(current, "Conclusion", "For", pro_4)

neg_4 = neg_ai.conclusion(current)

current = add_next(current, "Conclusion", "Against", neg_4)


fake_you = FakeYou()
fake_you.login("ratcht", "HarryPotter2")

list_trump = [pro_1, pro_2, pro_3, pro_4]
list_joe = [neg_1, neg_2, neg_3, neg_4]

create_trump(fake_you, list_trump)
create_joe(fake_you, list_joe)







