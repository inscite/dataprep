import calendar
from itertools import product
from os import makedirs, sep
from sys import argv

import numpy as np


def cal_builder(year, month):

    datetime_serial_fmt = str('{0:04d}{1:02d}{2:02d}')
    ym = calendar.monthcalendar(year, month)

    ym_np_arr = np.array(ym).ravel()
    ym_np_where = np.where(ym_np_arr > 0)

    days = ym_np_arr[ym_np_where]
    days_list = list()

    for day in days:

        dt_fmtd = datetime_serial_fmt.format(year, month, day)
        days_list.append(dt_fmtd)

    return days_list


def main():

    mode = argv[1]
    path_out = argv[2]
    path_out_root = str(path_out).split(sep=sep)[:-1]
    path_out_root_str = str('')
    if len(path_out_root) > 0:

        for i in range(len(path_out_root) - 1):
            path_out_root_str += str('{:s}{:s}').format(path_out_root[i], sep)
        path_out_root_str += path_out_root[-1]

        makedirs(path_out_root_str, exist_ok=True)
    else:
        pass

    f = open(file=path_out, mode='w')

    years, months = None, None
    if mode == 'year' and len(argv) -1 == 3:
        years = [int(year) for year in filter(None, str(argv[3]).split(sep=','))]
        months = list(range(1, 1+12))
    elif mode == 'yearmonth' and len(argv) -1 == 4:
        months = [int(month) for month in filter(None, str(argv[4]).split(sep=','))]
    else:
        pass

    for year, month in product(years, months):
        list_ymd = cal_builder(year, month)

        for ymd in list_ymd:
            f.write(str('{:s}\n').format(ymd))
        f.flush()

    # close file handler
    f.close()

    # fin
    return


if __name__ == '__main__':
    main()
