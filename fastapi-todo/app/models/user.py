from pydantic import BaseModel, Field
from typing import Optional

# User Model
class User(BaseModel):
  id: Optional[object] = None
  name: str
  email: str
  password: str