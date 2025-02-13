import random
import json


output_file_path = "/ailab/user/liziyang/workspace/AstroIR/tools/creat_dataset/output_file_path.txt"
with open(output_file_path, 'r+') as f:
    lines = f.readlines()
    lines = [i.strip() for i in lines]
    lines = [i.split(":")[0] for i in lines]

random.shuffle(lines)
train_ratio = 0.7

total_samples = len(lines)
train_size = int(total_samples * train_ratio)

train_set = lines[:train_size]
val_set = lines[train_size:]

print(len(train_set))
print(len(val_set))

with open('train_set.json', 'w') as file:
    json.dump(train_set, file)

with open('val_set.json', 'w') as file:
    json.dump(val_set, file)

