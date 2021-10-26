import os

env_keys = list(dict(os.environ).keys())

out_file = ""

for key in env_keys:
    if key.startswith("INPUT_ENVKEY_"):
        out_file += key.split("INPUT_ENVKEY_")[1] + "=" + os.environ.get(key) + "\n"

# get directory name in which we want to create .env file
directory = str(os.environ.get("INPUT_DIRECTORY", ""))

# get file name in which we want to add variables
# .env is set by default
file_name = str(os.environ.get("INPUT_FILE_NAME", ".env"))

path = str(os.environ.get("GITHUB_WORKSPACE", "."))

# This should resolve https://github.com/SpicyPizza/create-envfile/issues/27
if path in ["", "None"]:
    path = "."

with open(os.path.join(path, directory, file_name), "w") as text_file:
    text_file.write(out_file)
