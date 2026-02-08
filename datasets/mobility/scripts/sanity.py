import json

# Open and read the JSON file
filename="dataset_IPERF_DL_TEST_2_GNB_202.json"
with open(filename, 'r') as file:
    data = json.load(file)

# Print the data
print(len(data["entries"]))

filename="dataset_IPERF_DL_TEST_2_GNB_203.json"
with open(filename, 'r') as file:
    data = json.load(file)

# Print the data
print(len(data["entries"]))