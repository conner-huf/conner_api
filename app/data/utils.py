from bson import ObjectId

def convert_oid_to_str(doc):
    if isinstance(doc, dict):
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
            elif isinstance(value, list):
                doc[key] = [convert_oid_to_str(item) for item in value]
            elif isinstance(value, dict):
                doc[key] = convert_oid_to_str(value)
    return doc