my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old


for key, values in my_family.items():
  sentence = f"{values['name']} is my {key} and is {values['age']} years old"
  print(sentence)