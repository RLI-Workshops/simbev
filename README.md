# 2021-06-22 TUB Workshop

Welcome!

## Setup

### Linux

1. Check your Python Version by running `python3 --version`
    - It should be `>= 3.6`
    - If it's `< 3.6` please update your Python
2. Run `python3 -m venv path/to/venvs/d_py38_SimBEV` (Note: change `py38` with your `python3 --version`)
    - You may or may not have to install `python3-venv`
    - Run `apt-get update`
    - and `apt-get install python3-venv`
    - You may or may not need `sudo`
    - rerun `python3 -m venv path/to/venvs/d_py38_SimBEV` if `python3-venv` had to be installed first
3. Run `source d_py38_SimBEV/bin/activate` to activate your newly created `venv`
4. Change into your git directory `cd path/to/my/git/repos/`
5. `git clone` the `SimBEV` repository from [here]()


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

