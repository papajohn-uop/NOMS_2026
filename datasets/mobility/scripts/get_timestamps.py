import os


def get_timestamp_list(path='data/actual_mobility_1/gnb/202/config_get'):
    timestamps = []
    if not os.path.exists(path) or not os.path.isdir(path):
        print("HERE")
        return []

    filenames = [f for f in sorted(os.listdir(path)) if os.path.isfile(os.path.join(path, f))]
    for fn in filenames:
        timestamps.append(fn.split('.',2)[2])
    return timestamps

def get_filenames_in_config_get(path='data/actual_mobility_1/gnb/202/config_get'):
    filenames = []
    timestamps=[]
    if not os.path.exists(path) or not os.path.isdir(path):
        return []

    filenames = [f for f in sorted(os.listdir(path)) if os.path.isfile(os.path.join(path, f))]
    return filenames

if __name__ == "__main__":
    filenames = get_filenames_in_config_get()
    print("Filenames in 'config_get':", filenames)
    timestamps = get_timestamps()
    print("Timestamps in 'config_get':", timestamps)