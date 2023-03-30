import transformers
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import transformers

# Load the saved model

translator = transformers.pipeline("translation_en_to_de","model/my_awesome_model")
pipeline = translator
app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

class ListToTranslate(BaseModel):
    input_texts: List[str]
    
    
@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
 
@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(input_text: TextToTranslate):
    return translator(input_text.input_text)

@app.post("/batch_translation")
def batch_translation(input_text: ListToTranslate):
    print(input_text.input_texts)
    translated_text = translator(input_text.input_texts)
    return translated_text
  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

"""
from fastapi import FastAPI
#from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from typing import List
#import transformers

#load the saved model
translator = "fast_api_tutorial/app/model/my_awesome_model"
pipeline = translator

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

class ListToTranslate(BaseModel):
    input_texts: List()
    
    
@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
 
@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(input_text: TextToTranslate):
    return translator(input_text.input_text)

@app.post("/batch_translation")
def batch_translation(request: ListToTranslate):
    translated_text = translator(request.input_texts)
    return translator(translated_text[0])
  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)




import transformers
from transformers import pipeline
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

translate_pipeline = transformers.pipeline('translation_en_to_de', model='model/my_awesome_model') 
app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

@app.get("/")
def index():
    return {"message": "Hello World"}
"""


"""
@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}


    
#from fastapi import FastAPI, 
from transformers import pipeline

app = FastAPI()
translate_pipeline = pipeline('translation_en_to_de', model='t5-base')


    
                          
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)



#pipeline = # complete this line with the code to load the pipeline from the local files (path to model directory f
#translator('fast_api_tutorial/app/model/'+ 'my_awesome_model')
#pipeline = translator('fast_api_tutorial/app/model/' + 'my_awesome_model') #"translation_en_to_de", model = 'T5-base')
"""

