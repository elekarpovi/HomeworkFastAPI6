# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: 
#товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес 
#электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), 
#id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из 
#трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.



import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from store_models import database
import users
import products
import orders

app = FastAPI()


app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Добро пожаловать в магазин!</h1>"


if __name__ == '__main__':
    uvicorn.run(app)