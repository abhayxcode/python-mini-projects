from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
  id : Optional[object] = None
  task : str
  completed : Optional[bool] = False
