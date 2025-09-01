from fastapi import FastAPI
from student_router import router as student_router  # <-- import the router object

app = FastAPI()

app.include_router(student_router)



#this class is the entrypoint...
# it creates the app, regiters student routes 
# adds a simple health check 
