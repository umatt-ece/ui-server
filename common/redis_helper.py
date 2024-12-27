import redis
import json
from typing import Any, List, Dict

class ParameterStore:
    def __init__(self):
        self.key_value_store = redis.Redis(host='localhost', port=6379, db=0)

    def set(self, key: str, value: Any) -> None:
        """Store a key-value pair in Redis."""
        
        serialized_value = self.convert_to_redis_type(value)
        self.key_value_store.set(key, serialized_value)
        
    def get(self, key: str) -> Any:
        """Retrieve a value by key from Redis."""
        
        value = self.key_value_store.get(key)
        if value is None:
            raise KeyError(f"'{key}' not found")
        
        return self.convert_from_redis_type(value)
    
    def mset(self, key_values: Dict[str, Any]) -> None:
        """Set multiple key-value pairs in Redis."""
        
        for key, value in key_values.items():
            
            serialized_value = self.convert_to_redis_type(value)
            self.key_value_store.set(key, serialized_value)
            
    def mget(self, keys: List[str]) -> Dict[str, Any]:
        """Retrieve multiple values from Redis."""
        
        data = {}
        for key in keys:
            value = self.key_value_store.get(key)
            
            if value is None:
                raise KeyError(f"'{key}' not found")
            
            data[key] = self.convert_from_redis_type(value)
        return data
    
    @staticmethod
    def convert_to_redis_type(value: Any) -> str:
        """Convert Python objects into Redis-compatible types."""
        
        if isinstance(value, bool):
            return str(value).lower()  # Convert boolean to 'true'/'false'
        
        elif isinstance(value, (list, dict)):
            return json.dumps(value)  # Serialize list or dict as JSON string
        
        return str(value)  # Convert other types to string
    
    @staticmethod
    def convert_from_redis_type(value: bytes) -> Any:
        """Convert Redis-stored data back to Python objects."""
        
        try:
            decoded_value = value.decode("utf-8")  # Decode bytes to string
        except AttributeError as e:
            raise ValueError("Invalid value type from Redis") from e

        result = decoded_value  # Default to the decoded string
        
        if decoded_value == "true":
            result = True
        elif decoded_value == "false":
            result = False

        # Check for numerical data
        if decoded_value.isdigit():
            result = int(decoded_value)
        else:
            try:
                result = float(decoded_value) if '.' in decoded_value else result
            except ValueError:
                pass

            # Try to parse JSON
            try:
                result = json.loads(decoded_value)
            except (json.JSONDecodeError, ValueError):
                pass

        return result

