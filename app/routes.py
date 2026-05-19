from fastapi import APIRouter
from app.database import collection
from app.models import Employee

router = APIRouter()

# CREATE
@router.post("/employees")
def add_employee(emp: Employee):
    collection.insert_one(emp.dict())
    return {"message": "Employee added successfully"}

# READ ALL
@router.get("/employees")
def get_employees():
    data = list(collection.find({}, {"_id": 0}))
    return data

# READ ONE
@router.get("/employees/{name}")
def get_employee(name: str):
    emp = collection.find_one({"name": name}, {"_id": 0})
    return emp

# UPDATE
@router.put("/employees/{name}")
def update_employee(name: str, emp: Employee):
    collection.update_one(
        {"name": name},
        {"$set": emp.dict()}
    )
    return {"message": "Employee updated"}

# DELETE
@router.delete("/employees/{name}")
def delete_employee(name: str):
    collection.delete_one({"name": name})
    return {"message": "Employee deleted"}