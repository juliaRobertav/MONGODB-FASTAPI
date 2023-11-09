from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://loaclhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("students_collection")


# helpers


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }
    
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"id": student.inserted_id})
    return student_helper(new_student)

async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)
    
async def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"id": ObjectId(id)})
    if student:
        update_student = await student_collection.update_one({"id": ObjectId(id)}, {"$set": data})
        if update_student:
            return True
        return False


async def delete_student(id: sr):
    student = await student_collection.find_one({"id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"id": ObjectId(id)})
        return True