from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = ""
mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client["terabox_db"]
users_collection = db["users"]

async def save_user(user_id, username):
    existing = await users_collection.find_one({"user_id": user_id})
    if not existing:
        await users_collection.insert_one({
            "user_id": user_id,
            "username": username
        })
