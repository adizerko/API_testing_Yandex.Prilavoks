from pydantic import BaseModel, RootModel
from typing import List

class WorkingHours(BaseModel):
    start: int
    end: int

class Shop(BaseModel):
    name: str
    workingHours: WorkingHours
    
    def is_7_23(self):
        self.workingHours.start == 7 and self.workingHours.end == 21
    
class Shop(RootModel[List[Shop]]):
    pass