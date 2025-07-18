from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://ravi:ravi12345@cluster0.hndinhj.mongodb.net/?retryWrites=true&w=majority"
mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client["terabox_db"]
users_collection = db["users"]

async def save_user(user_id: int, username: str):
    await users_collection.update_one(
        {"user_id": user_id},
        {
            "$setOnInsert": {
                "user_id": user_id,
                "username": username,
                "is_banned": False
            }
        },
        upsert=True
    )

# ✅ Ban a user
async def ban_user(user_id: int):
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"is_banned": True}}
    )

# ✅ Unban a user
async def unban_user(user_id: int):
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"is_banned": False}}
    )

# ✅ Check if user is banned
async def is_banned(user_id: int) -> bool:
    user = await users_collection.find_one({"user_id": user_id})
    return user and user.get("is_banned", False)

