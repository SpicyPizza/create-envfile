#!/usr/local/bin/python
import os

env_keys = list(dict(os.environ).keys())

out_file = ""

for key in env_keys:
    if key.startswith("INPUT_ENVKEY_"):
        out_file += "{}={}\n".format(key.split("INPUT_ENVKEY_")[1], os.getenv(key))

# get directory name in which we want to create .env file
directory = str(os.getenv("INPUT_DIRECTORY", ""))

# get file name in which we want to add variables
# .env is set by default
file_name = str(os.getenv("INPUT_FILE_NAME", ".env"))

path = str(os.getenv("GITHUB_WORKSPACE", "/github/workspace"))

# This should resolve https://github.com/SpicyPizza/create-envfile/issues/27
if path in ["", "None"]:
    path = "."

if directory == "":
    full_path = os.path.join(path, file_name)
elif directory.startswith("/"):
    full_path = os.path.join(directory, file_name)
elif directory.startswith("./"):
    full_path = os.path.join(path, directory[2:], file_name)
# Any other case should just be a relative path
else:
    full_path = os.path.join(path, directory, file_name)

with open(full_path, "w") as text_file:
    text_file.write(out_file)
