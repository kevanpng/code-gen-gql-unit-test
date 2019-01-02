from jinja2 import Environment, FileSystemLoader
import inflection
import json
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
with open('input.json') as f:
    _input = json.load(f)

def camel_to_snake(word):
    result = inflection.underscore(word)
    return result

env.filters['camel_to_snake'] = camel_to_snake
template = env.get_template('gql-to-unit-test.txt')
output = template.render(_input=_input)
with open('tmp/output.py', 'w') as _file:
    _file.write(output)
print(output)
