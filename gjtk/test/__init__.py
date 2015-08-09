

import json


def error_message(test_data=None, test_result=None):
    message = ['']
    if test_data is not None:
        message.append('// Data')
        try:
            message.append(
                json.dumps(
                    test_data,
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': ')
                )
            )
        except:
            message.append('The test data is not JSON serializable:\n{0}'.format(test_data))
    if test_result is not None:
        message.append('// Result')
        try:
            message.append(
                json.dumps(
                    test_result,
                    sort_keys=True,
                    indent=2,
                    separators=(',', ': ')
                )
            )
        except:
            message.append('The test result is not JSON serializable:\n{0}'.format(test_result))
    return '\n'.join(message)

