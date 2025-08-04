from fastapi import APIRouter, Depends, BackgroundTasks
from app.database import get_db
from app.schemas.schemas import RecipeOut, RecipeCreate, LogView
from typing import List

router = APIRouter()

@router.get('/recipes/', response_model=List[RecipeOut])
async def list_recipes(db=Depends(get_db)):
    q = '''SELECT r.id, r.title, c.name as category_name
           FROM recipes r JOIN categories c ON r.category_id = c.id'''
    records = await db.fetch(q)
    return [RecipeOut(id=rec['id'], title=rec['title'], category=rec['category_name']) for rec in records]

@router.get('/recipes/search', response_model=List[RecipeOut])
async def search_recipes(ingredient: str, db=Depends(get_db)):
    # No optimized index in schema; joins may be slow for large tables
    q = '''SELECT r.id, r.title, c.name as category_name
           FROM recipes r
           JOIN recipe_ingredients ri ON r.id = ri.recipe_id
           JOIN ingredients i ON ri.ingredient_id = i.id
           JOIN categories c ON r.category_id = c.id
           WHERE LOWER(i.name) = LOWER($1)'''
    records = await db.fetch(q, ingredient)
    return [RecipeOut(id=rec['id'], title=rec['title'], category=rec['category_name']) for rec in records]

@router.get('/recipes/by-category', response_model=List[RecipeOut])
async def recipes_by_category(category: str, db=Depends(get_db)):
    q = '''SELECT r.id, r.title, c.name as category_name
           FROM recipes r JOIN categories c ON r.category_id = c.id
           WHERE LOWER(c.name) = LOWER($1)'''
    records = await db.fetch(q, category)
    return [RecipeOut(id=rec['id'], title=rec['title'], category=rec['category_name']) for rec in records]

@router.post('/recipes/', response_model=RecipeOut)
async def add_recipe(recipe: RecipeCreate, db=Depends(get_db)):
    q = 'INSERT INTO recipes (title, category_id) VALUES ($1, $2) RETURNING id'
    rec = await db.fetchrow(q, recipe.title, recipe.category_id)
    return RecipeOut(id=rec['id'], title=recipe.title, category=recipe.category, category=None)

@router.post('/recipes/log-view')
async def log_view(log: LogView, background_tasks: BackgroundTasks, db=Depends(get_db)):
    async def bg_log():
        await db.execute('INSERT INTO recipe_views (recipe_id, viewed_at) VALUES ($1, NOW())', log.recipe_id)
    background_tasks.add_task(bg_log)
    return {"status": "logging started"}
