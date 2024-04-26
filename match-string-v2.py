import re
'''string should start with a and is followed by or without b and has some othe charaters'''
def is_compliant_string(input_str):
    pattern = re.compile(r'^a(b*).*')
    truth_value = False
    if pattern.match(input_str):
        truth_value = True
    return truth_value
st1 = 'abbey'

if is_compliant_string(st1):
    print(f'The string {st1} is compliant with the rules')
else:
    print(f'The string {st1}  is not compliant with the rules')