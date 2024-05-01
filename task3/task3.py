import json
import os.path
import sys


def search_id(list_dict_id: list, data_in_values: dict):
    for dict_search in list_dict_id:
        if dict_search['id'] == data_in_values['id']:
            dict_search['value'] = data_in_values['value']
        if dict_search.get('values'):
            search_id(dict_search['values'], data_in_values)


try:
    with (open(os.path.join((sys.argv[1]), 'values.json')) as f_values,
          open(os.path.join((sys.argv[2]), 'tests.json')) as f_tests,
          open(os.path.join((sys.argv[3]), 'report.json'), 'w+') as f_report):
        values = json.loads(f_values.read())
        tests = json.loads(f_tests.read())
        for id_values in values['values']:
            search_id(tests['tests'], id_values)
        json.dump(tests, f_report)

except OSError:
    print("OS Error")
