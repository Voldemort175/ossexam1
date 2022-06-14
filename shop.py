from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

buyers = []
products = []
cbuy = []
count = 0
@app.post("/buyers")
async def addbuyer(name):
    if name in buyers:
        if isinstance(name,str) == True:
            return {"result: Duplicate entry"}
    else:
        if isinstance(name,str) == True:
            buyers.append(name)
            return {"result": "OK"}

@app.post("/products")
async def addprods(name):
    if name in products:
        return {"result: Duplicate entry"}
    else:
        if isinstance(name,str) == True:
            products.append(name)
            return {"result": "OK"}

@app.get("/buyers")
async def getbuyers():
        return {"buyers": buyers }
        
@app.get("/products")        
async def getprods():
        return {"products": products }

# @app.post("/buyers/{bname}")
# async def buy(bname: str, prod_name: str):
#     if bname in buyers:
#         if prod_name in products:
#             cbuy.append(prod_name)
#             count += 1 
#             return {"result":"OK"}
#     elif bname not in buyers:
#         return {"result":"Error:no buyer {bname}"}
#     elif bname in buyers & prod_name not in products:
#         return {"result":"Error: no product {prod_name}"}
@app.post("/buyers/{buyer_name}")
async def purchase(buyer_name: str, prod_name: str):
    if not(buyer_name in buyers):
        return {"result": f"Error: no buyer {buyer_name}"}
    if not (prod_name in products):
        return {"result": f"Error: no product {buyer_name}"}
    i = buyers.index(buyer_name)
    if prod_name in cbuy[i]:
        n = cbuy[i][prod_name]
        cbuy[i][prod_name] = n+1
    else:
        cbuy[i][prod_name] = 1

    return {"result": "OK"}

@app.get("/buyers/{bname}/purchased")
async def shoplist(bname: str):
    if bname in buyers:
        return {cbuy , count}
    else:
        return {"result": " Error: no buyer {bname}"}