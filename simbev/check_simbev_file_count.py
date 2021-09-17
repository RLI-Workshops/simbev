import os

from pathlib import Path


simbev_dir = Path(r"/storage/open_bea_calculations_v2/simbev_data/default_multi_2021-09-17_simbev_run")

file_count = 0

for sub_dir in os.listdir(simbev_dir):
    file_count += len(os.listdir(os.path.join(simbev_dir, sub_dir)))

print(file_count)