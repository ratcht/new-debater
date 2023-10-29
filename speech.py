
import time
from bs4 import BeautifulSoup
from fakeyou import *
from wave import *
import os


# website = SeleniumWebsite("https://fakeyou.com/tts")
# website.select_voice("Donald Trump")
# website.send_prompt("My name  is j trump")
# website.generate()




def create_joe(fake_you, list_prompt):

  joe_biden_token = "TM:wsvak9gwrdqf"
  for i, prompt in enumerate(list_prompt):
    print(f"Generating J{i}")
    joe = fake_you.make_tts_job(prompt, joe_biden_token)
    file_joe = fake_you.tts_poll(joe)
    file_joe.save(f"j{i}.wav")
    time.sleep(20)

def create_trump(fake_you, list_prompt):
  donald_trump_token = "TM:03690khwpsbz"

  for i, prompt in enumerate(list_prompt):
    print(f"Generating D{i}")
    trump = fake_you.make_tts_job(prompt, donald_trump_token)
    file_trump = fake_you.tts_poll(trump)
    file_trump.save(f"d{i}.wav")
    time.sleep(20)

