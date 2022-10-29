import json

INPUT_FILE = "input.csv"

def line_separator(line_s, delimeter=',') -> list:
    line_s = line_s.rstrip()
    line_s = line_s.split(delimeter)
    return line_s

def csv_to_list_dict(filename) -> list[dict]:


    with open(INPUT_FILE, 'r') as f:

        json_list = []
        keys = line_separator(f.readline())

        for lines in f:

            if line_separator(lines) != keys:
                lines_new = line_separator(lines)
                json_list += [dict(zip(keys, lines_new)) for _ in range(1)]

    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


