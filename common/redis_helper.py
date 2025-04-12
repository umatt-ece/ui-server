# =======================================================
# redis_helper.py - Typed Key-Value Store via Redis
#
# This module provides a `ParameterStore` class that acts as a
# typed interface for storing and retrieving parameter values
# from a Redis key-value database. It handles automatic
# conversion between Python types and Redis string formats,
# and supports both individual and batch operations.
# =======================================================

import redis
import json
from typing import Any, List, Dict

# =======================================================
# Class: ParameterStore
#
# Purpose:
#   Abstracts access to Redis for storing typed key-value pairs.
#   Converts between Python native types and Redis string storage.
#
# Usage:
#   ps = ParameterStore()
#   ps.set("GEAR", 2)
#   val = ps.get("GEAR")
# =======================================================
class ParameterStore:
    def __init__(self):
        """
        Establish a connection to the Redis server.

        Redis must be accessible at hostname 'redis-container'
        with default port 6379 and using database index 0.
        """
        self.key_value_store = redis.Redis(host='redis-container', port=6379, db=0)

    # ===================================================
    # Method: set
    #
    # Purpose:
    #   Store a single key-value pair in Redis after serialization.
    #
    # Parameters:
    #   - key (str): Redis key name
    #   - value (Any): Python value to store (e.g., int, bool, list)
    #
    # Returns:
    #   - None
    # ===================================================
    def set(self, key: str, value: Any) -> None:
        """Store a key-value pair in Redis."""
        serialized_value = self.convert_to_redis_type(value)
        self.key_value_store.set(key, serialized_value)

    # ===================================================
    # Method: get
    #
    # Purpose:
    #   Retrieve and deserialize a single value from Redis by key.
    #
    # Parameters:
    #   - key (str): Redis key to retrieve
    #
    # Returns:
    #   - Any: Deserialized Python value
    #
    # Raises:
    #   - KeyError: if the key is not found in Redis
    # ===================================================
    def get(self, key: str) -> Any:
        """Retrieve a value by key from Redis."""
        value = self.key_value_store.get(key)
        if value is None:
            raise KeyError(f"'{key}' not found")
        return self.convert_from_redis_type(value)

    # ===================================================
    # Method: mset
    #
    # Purpose:
    #   Store multiple key-value pairs into Redis.
    #
    # Parameters:
    #   - key_values (Dict[str, Any]): Dictionary of key-value pairs
    #
    # Returns:
    #   - None
    # ===================================================
    def mset(self, key_values: Dict[str, Any]) -> None:
        """Set multiple key-value pairs in Redis."""
        for key, value in key_values.items():
            serialized_value = self.convert_to_redis_type(value)
            self.key_value_store.set(key, serialized_value)

    # ===================================================
    # Method: mget
    #
    # Purpose:
    #   Retrieve multiple keys from Redis and deserialize their values.
    #
    # Parameters:
    #   - keys (List[str]): List of Redis keys to retrieve
    #
    # Returns:
    #   - Dict[str, Any]: Dictionary of deserialized key-value pairs
    #
    # Raises:
    #   - KeyError: if any key is not found in Redis
    # ===================================================
    def mget(self, keys: List[str]) -> Dict[str, Any]:
        """Retrieve multiple values from Redis."""
        data = {}
        for key in keys:
            value = self.key_value_store.get(key)
            if value is None:
                raise KeyError(f"'{key}' not found")
            data[key] = self.convert_from_redis_type(value)
        return data

    # ===================================================
    # Method: convert_to_redis_type (static)
    #
    # Purpose:
    #   Convert a Python value into a string suitable for Redis storage.
    #
    # Parameters:
    #   - value (Any): A Python object (bool, int, str, list, dict)
    #
    # Returns:
    #   - str: Serialized string representation for Redis
    # ===================================================
    @staticmethod
    def convert_to_redis_type(value: Any) -> str:
        """Convert Python objects into Redis-compatible types."""
        if isinstance(value, bool):
            return str(value).lower()  # Convert boolean to 'true'/'false'
        elif isinstance(value, (list, dict)):
            return json.dumps(value)  # Serialize list or dict as JSON string
        return str(value)  # Convert other types (int, float, str) to string

    # ===================================================
    # Method: convert_from_redis_type (static)
    #
    # Purpose:
    #   Convert Redis byte string back into appropriate Python type.
    #
    # Parameters:
    #   - value (bytes): Raw Redis byte data
    #
    # Returns:
    #   - Any: Deserialized Python object (bool, int, float, list, dict, or str)
    #
    # Raises:
    #   - ValueError: If decoding fails
    # ===================================================
    @staticmethod
    def convert_from_redis_type(value: bytes) -> Any:
        """Convert Redis-stored data back to Python objects."""
        try:
            decoded_value = value.decode("utf-8")  # Decode bytes to string
        except AttributeError as e:
            raise ValueError("Invalid value type from Redis") from e

        result = decoded_value  # Default to the decoded string

        # Boolean handling
        if decoded_value == "true":
            result = True
        elif decoded_value == "false":
            result = False

        # Integer and float handling
        if decoded_value.isdigit():
            result = int(decoded_value)
        else:
            try:
                result = float(decoded_value) if '.' in decoded_value else result
            except ValueError:
                pass

            # Try parsing JSON
            try:
                result = json.loads(decoded_value)
            except (json.JSONDecodeError, ValueError):
                pass

        return result
