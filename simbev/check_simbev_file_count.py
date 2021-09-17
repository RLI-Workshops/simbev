import os

from pathlib import Path


simbev_dir = Path(r"/storage/open_bea_calculations_v2/simbev_data/default_multi_2021-09-17_simbev_run")

file_count = 0

sub_dirs = sorted(os.listdir(simbev_dir))

print(len(sub_dirs))

for sub_dir in sub_dirs:
    single_dir_file_count = len(os.listdir(os.path.join(simbev_dir, sub_dir)))

    file_count += single_dir_file_count

    print(sub_dir, single_dir_file_count)

print(file_count)