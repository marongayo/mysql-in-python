import pandas as pd
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    Time,
    Date,
    ForeignKey,
)

engine = create_engine("mysql+mysqlconnector://root:divergent@localhost/pizza_data")
metadata = MetaData()
pizza_ingredients = Table(
    "pizzaingredients",
    metadata,
    Column("ingredient_id", Integer, primary_key=True),
    Column("pizza_ingredients", String(255)),
)

pizza = Table(
    "pizza",
    metadata,
    Column("pizza_id", String(255), primary_key=True),
    Column("pizza_name", String(255)),
    Column("unit_price", Float),
    Column("pizza_size", String(255)),
    Column("pizza_category", String(255)),
    Column("ingredient_id", Integer, ForeignKey("pizzaingredients.ingredient_id")),
)

order_details = Table(
    "orderdetails",
    metadata,
    Column("order_details_id", Integer, primary_key=True),
    Column("quantity", Integer),
    Column("total_price", Float),
    Column("pizza_id", String(255), ForeignKey("pizza.pizza_id")),
    Column("order_id", Integer),
    Column("order_date", Date),
    Column("order_time", Time),
)

metadata.create_all(engine)

# excel data operations
pizza_data = pd.read_excel("pizza_data.xlsx")
pizza_data["order_date"] = pd.to_datetime(pizza_data["order_date"])
pizza_data["order_time"] = pd.to_datetime(
    pizza_data["order_time"], format="%H:%M:%S"
).dt.time

order_details_data = pizza_data[
    [
        "order_details_id",
        "quantity",
        "total_price",
        "pizza_id",
        "order_id",
        "order_date",
        "order_time",
    ]
]
pizza_data = pizza_data[
    [
        "pizza_id",
        "pizza_name",
        "unit_price",
        "pizza_size",
        "pizza_category",
        "pizza_ingredients",
    ]
]


# Read each table into a Pandas DataFrame
df_pizza_ingredients = pd.read_sql_table("pizzaingredients", engine)
df_pizza = pd.read_sql_table("pizza", engine)
df_order_details = pd.read_sql_table("orderdetails", engine)

# Display the DataFrames
print("Pizza Ingredients DataFrame:")
print(df_pizza_ingredients)

print("\nPizza DataFrame:")
print(df_pizza)

print("\nOrder Details DataFrame:")
print(df_order_details)
