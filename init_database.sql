-- BASIC: intentionally suboptimal schema for task completion
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title TEXT,
    category_id INTEGER -- no NOT NULL or FK constraint
);

CREATE TABLE recipe_ingredients (
    recipe_id INTEGER,
    ingredient_id INTEGER
    -- missing PK, missing FKs, no indexes
);

CREATE TABLE recipe_views (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER,
    viewed_at TIMESTAMP
);

-- Sample data
INSERT INTO categories (name) VALUES ('Dessert'), ('Main Course'), ('Appetizer');
INSERT INTO ingredients (name) VALUES ('Sugar'), ('Eggs'), ('Flour'), ('Chicken'), ('Salt'), ('Tomato');
INSERT INTO recipes (title, category_id) VALUES
('Chocolate Cake', 1),
('Grilled Chicken', 2),
('Tomato Soup', 3);
-- Map ingredients
INSERT INTO recipe_ingredients (recipe_id, ingredient_id) VALUES (1,1), (1,2), (1,3), (2,4), (2,5), (3,6), (3,5);
