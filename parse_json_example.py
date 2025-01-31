import json
json_data = '{"x": 10, "y": 20, "z": 30}'
parsed_data = json.loads(json_data)

print(parsed_data["x"])
