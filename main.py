from fastapi import FastAPI
import requests
import random
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]


api=FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
async def root():
  d = requests.get('https://raw.githubusercontent.com/AxolotlAPI/data/main/pictures.txt').content
  r = d.decode('utf-8').split('\n')
  facts = requests.get('https://raw.githubusercontent.com/AxolotlAPI/data/main/facts.txt').content
  fact_list = facts.decode('utf-8').split('\n')
  return JSONResponse({"url":random.choice(r),
                       "facts":random.choice(fact_list),
                       "pics_repo":"https://github.com/AxolotlAPI/data",
                       "api_repo":"https://github.com/AxolotlAPI/axolotl.py-api"})

#keep_alive()
