# coding: utf-8

def init_ATSJ():
    id_end = 38800
    xr_cnt = 300
    ur_figs = 5
    ur_per_fig_cnt = 300
    ssr_figs = 10
    ssr_per_fig_cnt = 300
    sr_figs = 20
    sr_per_fig_cnt = 450
    r_figs = 30
    r_per_fig_cnt = 500

    dict_str = ""
    # xr
    dict_str += "({},{}): '<PlaceHolder_XR>',\n".format(id_end - xr_cnt + 1, id_end)
    id_end = id_end - xr_cnt
    # ur
    for i in range(ur_figs):
        dict_str += "({},{}): '<PlaceHolder_UR_{}>',\n".format(
            id_end - ur_per_fig_cnt + 1,
            id_end,
            i + 1
        )
        id_end -= ur_per_fig_cnt
    # ssr
    for i in range(ssr_figs):
        dict_str += "({},{}): '<PlaceHolder_SSR_{}>',\n".format(
            id_end - ssr_per_fig_cnt + 1,
            id_end,
            i + 1
        )
        id_end -= ssr_per_fig_cnt
    # sr
    for i in range(sr_figs):
        dict_str += "({},{}): '<PlaceHolder_SR_{}>',\n".format(
            id_end - sr_per_fig_cnt + 1,
            id_end,
            i + 1
        )
        id_end -= sr_per_fig_cnt  
    # r
    for i in range(r_figs):
        dict_str += "({},{}): '<PlaceHolder_R_{}>',\n".format(
            id_end - r_per_fig_cnt + 1,
            id_end,
            i + 1
        )
        id_end -= r_per_fig_cnt

    dump_file = open("_init_idrange2name.txt", "w")
    dump_file.write(dict_str)
    dump_file.close()

if __name__ == "__main__":
    init_ATSJ()