# Task Overview

You are contributing to a recipe management platform that enables users to search for recipes by ingredients or categories. While the FastAPI application structure and routing are already complete, the application is experiencing slow response times and inefficiencies during recipe search and filtering due to missing or suboptimal database logic. Your assignment is to implement the PostgreSQL schema, define effective relationships, and provide performant, async-compatible database interaction code for core features like listing, searching, and logging recipe views.

# Guidance

- Database schema must be normalized, enforce appropriate keys, and use suitable data types
- Foreign key relationships must be set for data integrity between recipes, categories, and ingredients
- Indexes on columns frequently used in search (e.g., ingredient, category) are required to improve query performance
- All database accesses, both in endpoints and background tasks, should use async-compatible PostgreSQL drivers (no ORM)
- Efficient, non-blocking queries and connection management are essential to avoid performance bottlenecks
- FastAPI routing and API schemas are already in place; your deliverable is limited to database layer and async CRUD/search logic

# Database Access

- Host: <DROPLET_IP>
- Port: 5432
- Database Name: recipe_db
- Username: recipe_user
- Password: recipe_pass
- Connect using your favorite SQL tool (pgAdmin, DBeaver, psql, etc.) to inspect and test your schema and queries

# Objectives

- Design and implement normalized PostgreSQL tables for recipes, ingredients, and categories, with correct keys and constraints
- Define efficient relations and ensure that indexes exist on commonly searched columns
- Write async database interaction code (using asyncpg or equivalent) for core CRUD/search operations and a background logging task for recipe views
- Validate that the API endpoints for searching/filtering recipes return correct and prompt responses

# How to Verify

- Use the provided endpoints (e.g., /recipes/search, /recipes/by-category) to confirm correct and quick results for all query types
- Run EXPLAIN ANALYZE on your SQL to verify the use of indexes and examine query execution plans
- Trigger background recipe view logging, then verify that logs are written as expected
- Confirm that the system sustains performance and correctness as more sample data is added
