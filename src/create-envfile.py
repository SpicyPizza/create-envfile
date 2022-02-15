#!/usr/local/bin/python
import os

env_keys = list(dict(os.environ).keys())

out_file = ""

# Make sure the env keys are sorted to have reproducible output
for key in sorted(env_keys):
    if key.startswith("INPUT_ENVKEY_"):
        value = os.getenv(key, "")

        # If the key is empty, throw an error.
        if value == "":
            raise Exception(f"Empty env key found: {value}")

        out_file += "{}={}\n".format(key.split("INPUT_ENVKEY_")[1], value)

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
    # Throw an error saying that absolute paths are not allowed. This is because
    # we're in a Docker container, and an absolute path would lead us out of the
    # mounted directory.
    raise Exception("Absolute paths are not allowed. Please use a relative path.")
elif directory.startswith("./"):
    full_path = os.path.join(path, directory[2:], file_name)
# Any other case should just be a relative path
else:
    full_path = os.path.join(path, directory, file_name)

print("Creating file: {}".format(full_path))

with open(full_path, "w") as text_file:
    text_file.write(out_file)
