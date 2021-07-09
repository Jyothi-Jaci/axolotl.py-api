from fastapi import FastAPI
import requests
import random
from fastapi.responses import JSONResponse

api=FastAPI()

@api.get("/")
async def root():
  d = requests.get('https://raw.githubusercontent.com/AxolotlAPI/data/main/pictures.txt').content
  r = d.decode('utf-8').split('\n')
  facts = requests.get('https://github.com/AxolotlAPI/data/blob/main/facts.txt').content
  fact_list = facts.decode('utf-8').split('\n')
  return JSONResponse({"url":random.choice(r),
                       "facts":random.choice(fact_list),
                       "pics_repo":"https://github.com/AxolotlAPI/data",
                       "api_repo":"https://github.com/AxolotlAPI/axolotl.py-api"})

#keep_alive()