from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
from uvicorn.main import main
#from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/{sensor_dir}/{config}', response_class=PlainTextResponse)
def camera(sensor_dir: str, config: str):
    path = './%s/%s'%(sensor_dir,config)
    content = open(path, 'rb')
    readline = content.read()
    return readline

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

###
#origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],  
#     allow_headers=["*"],
# )
###

#print(readline, type(readline))


# @app.get('/sw420.py', response_class=PlainTextResponse)
# async def sw420():
#     content = open('sw420.py', 'rb')
#     readline = content.read()
#     print(readline, type(readline))
#     return readline

# @app.get('/lm75a.py', response_class=PlainTextResponse)
# async def sw420():
#     content = open('lm75a.py', 'rb')
#     readline = content.read()
#     print(readline, type(readline))
#     return readline


# readlines = list
# read = bytes