import json
with open('mirrors', 'r') as f:
    mirrors = json.load(f)

data_cn = []
data_other = []
for data in mirrors['data']:
    if data['location'] == "CN":
        data_cn.append(data)
    else:
        data_other.append(data)

json_cn = {
        "status_code":0,
        "status_message":"ok",
        "data":data_cn
        }

json_other = {
        "status_code":0,
        "status_message":"ok",
        "data":data_other
        }

with open('mirror_cn', 'w') as f:
    json.dump(json_cn, f)

with open('mirror_other', 'w') as f:
    json.dump(json_other, f)
