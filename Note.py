import os

project_structure = {
    "app": ["__init__.py", "routes.py", "models.py", "templates/index.html"],
    "": ["run.py"]
}

for folder, files in project_structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        path = os.path.join(folder, file)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("")
print("Project structure created!")
