import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import hello as main

origins = [
    "*"
]

main.app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(main.app, host="0.0.0.0", port=8000)