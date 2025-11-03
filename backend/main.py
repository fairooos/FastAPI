from fastapi import FastAPI
from models import Product
from database import session

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
  Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20)
]

@app.get("/products")
def get_all_products():
    db = session()
    db.query()
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product 


@app.put("/product/{id}")
def update_product(id: int, updated_product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return {"message": "Product updated successfully"}
    return {"error": "No product found"}
    
@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"} 