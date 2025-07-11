from pydantic import BaseModel, RootModel
from typing import List

class WorkingHours(BaseModel):
    start: int
    end: int

class Shop(BaseModel):
    name: str
    workingHours: WorkingHours
    
    
class Shop(RootModel[List[Shop]]):
    pass