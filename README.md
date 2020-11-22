# Create Envfile Github Action

**Name: SpicyPizza/create-envfile@v1**

Github Action to create a .env file with Github Secrets

## Usage

The action looks for environment variables that start with `INPUT_ENVKEY_` and creates an envfile with them. To add a key to the envfile, add a key/pair to the `with:` section. It must begin with `envkey_`.

```yml
name: Create envfile

on: [push]

jobs:

  create-envfile:
 
    runs-on: ubuntu-18.04
 
    steps:
    - name: Make envfile
      uses: SpicyPizza/create-envfile@v1
      with:
        envkey_DEBUG: false
        envkey_SOME_API_KEY: "123456abcdef"
        envkey_SECRET_KEY: ${{ secrets.SECRET_KEY }}
        some_other_variable: foobar
        directory: <directory_name>
        file_name: .env
```

In this example, there are 6 keys:

`envkey_DEBUG`, `envkey_SOME_API_KEY` - String values

`envkey_SECRET_KEY` - A secret stored in the repository's Github Secrets

`some_other_variable` - Won't be used because it doesn't start with `envkey_`

`directory`(**Optional**) - This key will set the directory in which you want to create `env` file. (**Action will fail if the specified directory doesn't exist.**)

`file_name`(**Optional**) - Set the name of the output envfile. Defaults to `.env`
