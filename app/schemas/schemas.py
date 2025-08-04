from pydantic import BaseModel
from typing import Optional

class RecipeCreate(BaseModel):
    title: str
    category_id: int
    category: Optional[str] = None

class RecipeOut(BaseModel):
    id: int
    title: str
    category: str

class LogView(BaseModel):
    recipe_id: int
