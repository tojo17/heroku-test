import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import hello as main

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    main.router,
    prefix = "/"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)