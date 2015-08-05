

import json


def error_message(test_data=None, test_result=None):
    message = ['']
    if test_data is not None:
        message.append('// Data')
        message.append(
            json.dumps(
                test_data,
                sort_keys=True,
                indent=2,
                separators=(',', ': ')
            )
        )
    if test_result is not None:
        message.append('// Result')
        message.append(
            json.dumps(
                test_result,
                sort_keys=True,
                indent=2,
                separators=(',', ': ')
            )
        )
    return '\n'.join(message)

