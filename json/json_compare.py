# http://stackoverflow.com/questions/25851183/how-to-compare-two-json-objects-with-the-same-elements-in-a-different-order-equa
import json

a = json.loads("""
{
    "errors": [
        {"error": "invalid", "field": "email"},
        {"error": "required", "field": "name"}
    ],
    "success": false
}
""")

b = json.loads("""
{
    "success": false,
    "errors": [
        {"error": "required", "field": "name"},
        {"error": "invalid", "field": "email"}
    ]
}
""")

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

print(ordered(a) == ordered(b))
