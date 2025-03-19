from config import *
import motor.motor_asyncio, datetime


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users  # Correct reference for the users collection

    def new_user(self, id):
        return dict(
            id=int(id),
            shortner=None,
            api=None
        )

    async def add_user(self, id):
        """Add a user to the database if they are not already present."""
        if not await self.is_user_exist(id):  # Check before adding
            user = self.new_user(id)
            await self.col.insert_one(user)

    async def is_user_exist(self, id):
        """Check if a user exists in the database."""
        user = await self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        return await self.col.count_documents({})

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_shortner(self, uid, shortner, api):
        """Store shortener settings for the user."""
        await self.col.update_one({'id': int(uid)}, {'$set': {'shortner': shortner, 'api': api}}, upsert=True)

    async def get_value(self, key, uid):
        """Retrieve stored shortener values (URL or API key)."""
        user = await self.col.find_one({'id': int(uid)})
        return user.get(key, None) if user else None

    async def delete_value(self, key, uid):
        """Delete a specific key (shortner or api) from the user's record."""
        await self.col.update_one({'id': int(uid)}, {'$unset': {key: ""}})


db = Database(DATABASE_URL, " TechifyBots")
