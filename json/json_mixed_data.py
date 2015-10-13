#!/usr/bin/env python
# encoding: utf-8

import json

decoder = json.JSONDecoder()


def get_decoded_and_remainder(input_data):
    obj, end = decoder.raw_decode(input_data)
    remaining = input_data[end:]
    return (obj, end, remaining)


encoded_object = '[{"a": "A", "c": 3.0, "b": [2, 4]}]'
extra_text = 'This text is not JSON.'

print 'JSON first:'
obj, end, remaining = get_decoded_and_remainder(' '.join([encoded_object, extra_text]))
print 'Object              :', obj
print 'End of parsed input :', end
print 'Remaining text      :', repr(remaining)

print
print 'JSON embedded:'
try:
    obj, end, remaining = get_decoded_and_remainder(
        ' '.join([extra_text, encoded_object, extra_text])
    )
except ValueError, err:
    print 'ERROR:', err
