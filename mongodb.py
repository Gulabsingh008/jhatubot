from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client['terabox_bot']
users_collection = db['users']

async def add_user(user_id, name):
    user = await users_collection.find_one({'user_id': user_id})
    if not user:
        await users_collection.insert_one({
            'user_id': user_id,
            'name': name,
            'is_banned': False
        })

async def is_banned(user_id):
    user = await users_collection.find_one({'user_id': user_id})
    return user and user.get('is_banned', False)

async def ban_user(user_id):
    await users_collection.update_one({'user_id': user_id}, {'$set': {'is_banned': True}})

async def unban_user(user_id):
    await users_collection.update_one({'user_id': user_id}, {'$set': {'is_banned': False}})

async def get_all_users():
    users = users_collection.find()
    return await users.to_list(length=10000)

async def get_total_users():
    return await users_collection.count_documents({})

async def get_banned_users():
    return await users_collection.count_documents({'is_banned': True})
