import re

def is_compliant_string(input_str):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    truth_value = False
    if pattern.match(input_str):
        truth_value = True
    return truth_value
st1 = 'Hello@'

if is_compliant_string(st1):
    print(f'The string {st1} is compliant with the rules')
else:
    print(f'The string {st1}  is not compliant with the rules')