import os

# Construct dotenv file contents
env_keys = dict(os.environ).keys()
keys_to_set = filter(lambda key: key.startswith("INPUT_ENVKEY_"), env_keys)
output_lines = map(lambda key: f'{key.split("INPUT_ENVKEY_")[1]}={os.environ.get(key)}\n', keys_to_set)
file_content = '\n'.join(output_lines)

# Construct filepath to write to
action_working_dir = os.environ.get("GITHUB_WORKSPACE")
if not action_working_dir:
    raise Exception("Could not get the GITHUB_WORKSPACE environment variable.")

directory = str(os.environ.get("INPUT_DIRECTORY", '.'))
file_name = str(os.environ.get("INPUT_FILE_NAME", '.env'))
file_path = os.path.join(action_working_dir, directory, file_name)

with open(file_path, "w") as text_file:
    text_file.write(file_content)
