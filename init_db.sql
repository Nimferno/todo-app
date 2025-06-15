-- Создание таблицы, если она не существует
CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Опционально: можно добавить тестовые данные
INSERT INTO todo (title, description, completed)
VALUES 
    ('Купить продукты', 'Молоко, хлеб, яйца', false),
    ('Сделать домашку', 'Доделать практическую по Docker', false)
ON CONFLICT DO NOTHING;