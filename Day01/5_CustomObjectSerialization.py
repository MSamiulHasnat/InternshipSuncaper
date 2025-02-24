data ={
    "name": "Samiul",
    "age": 21,
    "height": 5.9,
    "weight": 102,
    "isStudent": True
}

def serialize(obj):
    if not isinstance(obj, dict):
        raise ValueError("Input is not a dictionary.")
    serializedParts = []
    for key, value in obj.items():
        if not isinstance(key, str):
            raise ValueError("All keys must be strings.")
        if isinstance(value, (str, int, float)):
            serializedParts.append(f"{key}:{value}")
        else:
            raise ValueError(f"Unsupported type: {type(value)}")

    return ";".join(serializedParts)

def deserialize(s):
    if not s:
        return {}

    result = {}
    pairs = s.split(";")
    for pair in pairs:
        if ":" not in pair:
            raise ValueError(f"Invalid format of pair: {pair}")
        key, value = pair.split(":", 1)
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        result[key] = value
    return result

# Serialize the object
serialized_data = serialize(data)
print("Serialized:", serialized_data)

# Deserialize the string back to an object
deserialized_data = deserialize(serialized_data)
print("Deserialized:", deserialized_data)