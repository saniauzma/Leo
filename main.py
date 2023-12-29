from fastapi import FastAPI  
import random  
 
app = FastAPI()  
 
 
@app.get("/api/generate_random_number")  
async def generate_random_number():  
     random_number = random.randint(1, 100)  
     return {"random_number": random_number}