# wheelhouse
pull all python dependency wheel files following pip depth tree

## How to use
1. (external env)pip install module_name

2. (external env)sh extract_package_wheels.sh module_name

3. (external env)copy to module_name_wheels folder to internal dev env

4. (internal env)move module_name_wheels

5. (internal env)pip install module_name_version.wheel --no-index --find-links .
