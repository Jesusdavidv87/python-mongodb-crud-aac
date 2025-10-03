"""
CRUD_Python_Module.py
Reusable CRUD class for MongoDB (Create & Read for Module Four).
"""

from typing import Any, Dict, List, Optional
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import PyMongoError


class AnimalShelter:
    """
    CRUD operations for the AAC 'animals' collection.

    Example:
        shelter = AnimalShelter(
            username="aacuser",
            password="YOUR_PASSWORD",
            host="localhost",
            port=27017,
            db_name="aac",
            collection_name="animals",
            auth_db="aac",
        )
        ok = shelter.create({"animal_id": "A123", "name": "Buddy"})
        rows = shelter.read({"animal_id": "A123"})
    """

    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 27017,
        db_name: str = "aac",
        collection_name: str = "animals",
        auth_db: str = "aac",
        **client_kwargs: Any,
    ) -> None:
        """Initialize MongoDB connection and target collection."""
        uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}"
        try:
            self._client = MongoClient(uri, **client_kwargs)
            self._db = self._client[db_name]
            self._col: Collection = self._db[collection_name]
            # Quick connectivity check
            self._client.admin.command("ping")
        except PyMongoError as exc:
            raise RuntimeError(f"Failed to connect to MongoDB: {exc}") from exc

    # -------------------- C: Create --------------------
    def create(self, document: Dict[str, Any]) -> bool:
        """
        Insert a single document.

        Returns:
            True if exactly one doc inserted; otherwise False.
        """
        if not isinstance(document, dict) or not document:
            return False
        try:
            result = self._col.insert_one(document)
            return result.acknowledged and result.inserted_id is not None
        except PyMongoError:
            return False

    # -------------------- R: Read ----------------------
    def read(self, query: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Find documents using `find()` and return a list.

        Args:
            query: MongoDB filter dict. If None/empty, returns all docs.

        Returns:
            List of documents (possibly empty). Returns [] on error.
        """
        try:
            cursor = self._col.find(query or {})
            return list(cursor)
        except PyMongoError:
            return []
