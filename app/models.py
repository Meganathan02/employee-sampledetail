from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    role: str
    department: str
    salary: float
    is_active: bool = True