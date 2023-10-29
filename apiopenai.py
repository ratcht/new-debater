import openai
import tiktoken
import logging
import json
from typing import Tuple


def authenticate(API_KEY, ORGANIZATION):
  openai.organization =  ORGANIZATION# organization name
  openai.api_key = API_KEY


def create_embedding(embedding_model: str, content):
  """Create an embedding"""
  try:
    response = openai.Embedding.create(model=embedding_model, input=content)
  except Exception as e:
    print(e)
    raise e

  
  for i, be in enumerate(response["data"]):
    assert i == be["index"]  # double check embeddings are in same order as input

  return response



def query(query: str, model: str = "gpt-4"):

  messages = [
    {"role": "system", "content": "You are a participant in a debate. You will be debating the topic provided that you must take the given view on. You will also be told the stage of the debate. You must offer logical arguments and develop them as the debate progresses"},
    {"role": "user", "content": query},
  ]

  try:
    response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=0
    )
  except Exception as e:
    raise Exception(f"From Chat Completion... {e}")
  
  response_message = response["choices"][0]["message"]["content"]
  return response_message

def query_message(messages: str, model: str = "gpt-4"):

  try:
    response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=0
    )
  except Exception as e:
    raise Exception(f"From Chat Completion... {e}")
  
  response_message = response["choices"][0]["message"]["content"]
  return response_message


def function_query(message, functions, model) -> Tuple:
  print("----Querying OpenAI----")
  messages = [
    {"role": "system", "content": "You are good at navigating websites and will order a pizza. You will navigate the given HTML and decide what function is most appropriate to call based on the given task."},
    {"role": "user", "content": message},
  ]

  try:
    response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=0,
      functions=functions,
      function_call="auto"
    )
  except Exception as e:
    raise Exception(f"From Chat Completion... {e}")
  
  print(response)
  
  response_message = response["choices"][0]["message"]


  try:
    function_name = response_message["function_call"]["name"]
    function_args = json.loads(response_message["function_call"]["arguments"])
  except Exception as e:
    for i in range(0,3):
      while True:
        print("Retrying 1...")
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        functions=functions,
        function_call="auto"
        )
        response_message = response["choices"][0]["message"]
        try:
          function_name = response_message["function_call"]["name"]
          function_args = json.loads(response_message["function_call"]["arguments"])
        except:
          continue
        break

  print("Function Name: "+function_name)
  print(function_args)

  return response_message["content"], function_name, function_args





def num_tokens(text: str, model: str) -> int:
  """Return the number of tokens in a string"""
  encoding = tiktoken.encoding_for_model(model)
  return len(encoding.encode(text))