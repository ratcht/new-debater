from apiopenai import *

class DebatorAI:
  def __init__(self, topic, side, personality):
    self.over_prompt = f"You are debating a friend. You will speak in a casual tone, mimicking the personality of {personality}, but will follow logical arguments. You will try to incorporate humor in your answers. You will be debating the topic {topic} that you must take the '{side}' view on. You will also be told the stage of the debate. You must offer logical arguments and develop them as the debate progresses."

  def query(self, stage, previous_stages):
    prompt = f"You must follow the current stage of the debate, meaning that you will either provide an argument or a rebuttal, depending on the stage. The debate is currently in the {stage}. Below, you will find the rest of the debate. Create a thoughtful and argumentative answer {previous_stages}. Do not open your response with 'Stage' or your team name, just state your response immedietly. "
    response = query(self.over_prompt+"\n\n"+prompt, "gpt-4")
    return response
  
  def conclusion(self, previous_stages):
    prompt = f"Now, based on your previous argument, you will come to a conclusion based on objective facts and the arguments discussed above. Your answer will be short and concise, no longer than 2 sentences. Be open and try to acknowledge your opponents arguments in your conclusion.\n\nThe previous conversation is as follows:\n{previous_stages}"
    response = query(prompt, "gpt-4")
    return response


