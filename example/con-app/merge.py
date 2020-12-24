# r full file dict
r_file = {}

# r_file_headers
r_file_header = []

# s file headers
# s_file_header = []

# s file dict
s_file = {}

# new file
f = open("test.txt", "w+")
f.write('|'.join(r_file_header))
f.write("\n")

# read r full file
def read_r_full_file(filename):
    with open(filename, "r") as ofs:
        data = ofs.readlines()
        for dat in data:
            temp_dat = dat.strip().split("|")
            r_file[''.join(temp_dat[:4])] = temp_dat

# read s delta file
def read_s_delta_file(filename):
    with open(filename, "r") as ofs:
        data = ofs.readlines()
        for dat in data:
            temp_dat = dat.strip().split("|")
            s_file[''.join(temp_dat[:4])] = temp_dat

# merge_dicts
def merge_files():
    # check for keys
    for k, v in r_file.items():
        try:
            s_file[k]
            tmp_data = v
            # replace last position date
            tmp_data[-1] = tmp_data[4]
            # replace data
            tmp_data[4:7] = s_file[k][4:7]
            f.write('|'.join(tmp_data))
            f.write("\n")
        except:
            # write to file
            f.write('|'.join(v))
            f.write("\n")
    f.close()