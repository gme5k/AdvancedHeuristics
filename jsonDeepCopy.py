"""
Title: json deep copy: An alternative solution to deep copy
Author: yoheijana
Published on: December 29, 2014
Retrieved from https://technology.jana.com/2014/12/29/json-deep-copy/
"""

import copy
import json
import ujson

def update_dict(data_copy, data):
    for k, v in data_copy.iteritems():
        if v != data[k]:
            if isinstance(v, dict):
                update_dict(v, data[k])
            elif isinstance(v, list):
                update_list(v, data[k])
            elif isinstance(v, float):
                data_copy[k] = data[k]

def update_list(data_copy, data):
    for i, value in enumerate(data_copy):
        if value != data[i]:
            if isinstance(value, dict):
                update_dict(value, data[i])
            elif isinstance(value, list):
                update_list(value, data[i])
            elif isinstance(value, float):
                data_copy[i] = data[i]

def json_deep_copy(data):
    if data is None:
        return data

    #  precise_float is slower, but we get more reports of diffs
    #  without it (floats being floats)
    try:
        data_copy = ujson.loads(
            ujson.dumps(data, double_precision=15),
            precise_float=True)
        if isinstance(data_copy, list):
            update_list(data_copy, data)
        else:
            update_dict(data_copy, data)
    except OverflowError:
        data_copy = json.loads(json.dumps(data))
    except Exception:
        print ("non-json safe object passed. falling back to deepcopy")
        data_copy = copy.deepcopy(data)
    return data_copy