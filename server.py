import sys
import uvicorn

import hello as main



if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except:
        port = 8000
    uvicorn.run("hello:app", host="0.0.0.0", port=port, workers=1)