# coding: utf-8
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <tokenid2name_file>".format(sys.argv[0]))
        sys.exit(1)

    name2ids = {}
    for line in open(sys.argv[1]):
        items = line.strip().split(",")
        token_id = int(items[0])
        token_name = items[1]
        if token_name not in name2ids:
            name2ids[token_name] = []
        name2ids[token_name].append(token_id)
    
    idrange2name = {}
    for tname in name2ids:
        ids = name2ids[tname]
        ids.sort(key=lambda i: i)
        r_start = ids[0]
        for i in range(1,len(ids)):
            if (ids[i] - ids[i-1]) != 1:
                r_end = ids[i-1]
                idrange2name[(r_start, r_end)] = tname
                r_start = ids[i]
        idrange2name[(r_start, ids[-1])] = tname
    
    idrange_name_list = []
    for (id_range, tname) in idrange2name.items():
        idrange_name_list.append([id_range, tname])
    #print(idrange_name_list[:10])
    idrange_name_list.sort(key=lambda i: i[0][0])
    with open("data/_dump_idrange2name.txt", "w") as dump_file:
        for (idrange, tname) in idrange_name_list:
            dump_file.write("({},{}): \"{}\",\n".format(
                idrange[0], idrange[1], tname
            ))