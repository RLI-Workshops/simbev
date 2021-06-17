# 2021-06-22 TUB Workshop

Welcome!

## Setup

### Windows

1. Change into your `python/git` directory on your local device and create a new folder for this workshop `C:\Users\xxx\projects_python\simbev_workshop`
2. Use a git programme (e.g. Git Bash) to clone the repository https://github.com/RLI-Workshops/simbev into the new folder using `git clone https://github.com/RLI-Workshops/simbev`
3. In your git programme, change into the cloned repository using `cd simbev` you now should see the current branch in brackets, e.g. (dev)
4. Checkout the workshop branch with `git checkout feature/tub-workshop`
5. Start your Anaconda Prompt
6. Create a new virtual environment using `conda create -n d_py38_SimBEV python` (Note: change `py38` accordingly to your `python3 --version`)
7. Activate the new environment using `conda activate d_py38_SimBEV`
8. Change into the cloned repository on your local device using `cd path\to\simbev_workshop\simbev`
9. Install the required packages using `pip3 install -r requirements.txt`
10. You can check if the following packages were installed with `pip3 list`
    - configparser
    - numpy
    - pandas
    - matplotlib
    - seaborn
    - jupyterlab

### Linux

1. Check your Python Version by running `python3 --version` in your terminal
    - It should be `>= 3.6`
    - If it's `< 3.6` please update your Python
2. Change into your venv directory `cd ~/path/to/venvs/`
3. Run `python3 -m venv d_py38_SimBEV` (Note: change `py38` accordingly to your `python3 --version`)
    - You may or may not have to install `python3-venv`
    - Run `apt-get update`
    - and `apt-get install python3-venv`
    - You may or may not need `sudo`
    - rerun `python3 -m venv path/to/venvs/d_py38_SimBEV` if `python3-venv` had to be installed first
4. Run `source d_py38_SimBEV/bin/activate` to activate your newly created `venv`
5. Change into your git directory `cd ~/path/to/my/git/repos/`
6. `git clone` the `SimBEV` repository from [here](https://github.com/RLI-Workshops/simbev) (Note: I forked the project. So be sure to use this link.)
    - Either use `HTTPS` or `SSH` depending on your setup
7. `cd simbev/`
8. Checkout the workshop branch with `git checkout feature/tub-workshop`
9. `pip3 install -r requirements.txt`
10. You can check if the following packages were installed with `pip3 list`
    - configparser
    - numpy
    - pandas
    - matplotlib
    - seaborn
    - jupyterlab


# LEGACY - Ignore this part for now:
------------------------------------
# Download and run SimBEV

## Download/install

- clone repository to your local machine
- install requirements found in requirements.txt (virtualenv recommended)

## Run SimBEV

- you can define a custom scenario in the directory `scenarios`, see [scenario readme](./simbev/scenarios/README.md) for instructions
- run main_simbev.py with the desired scenario: `python main_simbev.py <SCENARIO_NAME>` (defaults to `python main_simbev.py default_single`)
- results are created in directory `res`

## Set paramters for your scenario

Select regio-type for the mobility characteristics:
- regiotypes:
Ländliche Regionen
LR_Klein - Kleinstädtischer, dörflicher Raum
LR_Mitte - Mittelstädte, städtischer Raum
LR_Zentr - Zentrale Stadt
Stadtregionen
SR_Klein - Kleinstädtischer, dörflicher Raum
SR_Mitte - Mittelstädte, städtischer Raum
SR_Gross - Regiopolen, Großstädte
SR_Metro - Metropole

Change vehicle configuration
- battery capacity
- charging power (slow and fast)
- consumption

Decide how many vehicles should be simulated
- note: more than 5000 vehicles of one type in one region is not necessary, if you want to analyze more, scale it accordingly

