from fastapi import APIRouter, HTTPException
from module.database import users_collection
from bson import json_util
import json

router = APIRouter(
    tags=["Product_ID Services"],
    responses={404: {"description": "Not found"}}
)

@router.get("/search/{product_id}")
async def get_product_by_id(product_id: str):
    # Query to find the user document that contains the specified product_id in its list_product
    user_document = users_collection.find_one({"list_product.product_id": product_id}, {"_id": 0, "list_product.$": 1})
    if user_document:
        # Extract the product from list_product
        product_data = user_document.get("list_product", [])[0]  # Get the first product in the list
        product_json = json.loads(json_util.dumps(product_data))
        return product_json
    else:
        raise HTTPException(status_code=404, detail="Product not found")
