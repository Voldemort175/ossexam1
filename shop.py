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
            cbuy.append({})
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

@app.post("/buyers/{bname}")
async def buy(bname: str, prod_name: str):
    if bname in buyers:
        if prod_name in products:
            id = buyers.index(bname)
            if prod_name in cbuy[id]:
                count = cbuy[id][prod_name]
                cbuy[id][prod_name] = count+1
            else:
                cbuy[id][prod_name] = 1
        return {"result": "OK"}
    elif not(bname in buyers):
        return {"result": "Error: no buyer {bname}"}
    elif not (prod_name in products):
        return {"result": "Error: no product {prod_name}"}

@app.get("/buyers/{bname}/purchased")
async def shoplist(bname: str):
    if not (bname in buyers):
        return {"result":"Error: no buyer {bname}"}
    i = buyers.index(bname)
    return cbuy[i]