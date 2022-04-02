# coding: utf-8

def init_LT():
    id_end = 8680
    per_fig_cnt = 299
    figs_cnt = 19

    dict_str = ""
    for i in range(figs_cnt):
        dict_str += "({},{}): '<PlaceHolder_{}>',\n".format(
            id_end - per_fig_cnt + 1,
            id_end,
            i + 1
        )
        id_end -= per_fig_cnt
   

    dump_file = open("_init_idrange2name_lt.txt", "w")
    dump_file.write(dict_str)
    dump_file.close()

if __name__ == "__main__":
    init_LT()