#!/usr/bin/python3
from base_model import BaseModel

model_instance = BaseModel()
model_instance.name = "Holberton"
model_instance.number = 89
print(model_instance.id)
print(model_instance)
print(type(model_instance.created_at))
print("--")
model_instance_dict = model_instance.to_dict()
print(model_instance_dict)
print("JSON of model_instance:")
for key in model_instance_dict.keys():
    print(
        "\t{}: ({}) - {}".format(
            key, type(model_instance_dict[key]), model_instance_dict[key]
        )
    )

print("--")
new_model_instance = BaseModel(**model_instance_dict)
print(new_model_instance.id)
print(new_model_instance)
print(type(new_model_instance.created_at))

print("--")
print(model_instance is new_model_instance)

