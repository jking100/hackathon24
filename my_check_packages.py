# Local Environment checker: helloworld but it verifies we have the same environment configuration
#   if this doesnt exit out successfully then your envionment is not proper
# Follow automatic install steps first to configure local envioment

#
# AUTOMATIC INSTALLATION VIA REQUIREMENTS.TXT
# 
# { INSTALL PYTHON 3.11 IF NOT FOUND. CHECK BY ls -l /usr/bin/ | grep "python" (if found you will see "python3.11")
# $ sudo zypper install python311 //installs as /usr/bin/python3.11
# $ cd /path/to/this/project/
# $ python3.11 -m venv hackathon24venv //create venv(hackathon24venv) in project folder
# $ source hackathon24venv/bin/activate //to enter venv
# $ python --version //should be 3.11.10 when ran within venv
# $ deactivate //to exit venv
# }
#
# $ source hackathon24venv/bin/activate //to enter venv
# $ cat ./requirements.txt | wc -l //67
# $ pip install -r ./requirements.txt
# $ pip freeze | wc -l //67
# $ pip check //"No broken requirements found."
#
# AUTO INSTALL SHOULD BE COMPLETE, MAKE SURE SCRIPT PASSES NOW: execute main.py
#
# --------------------------------------------------------------------------------
# 
# MANUAL INSTALL: FOLLOW FROM HERE
#
# { INSTALL PYTHON 3.11 IF NOT FOUND. CHECK BY ls -l /usr/bin/ | grep "python"
# $ sudo zypper install python311 //installs as /usr/bin/python3.11
# $ cd /path/to/this/project/
# $ python3.11 -m venv hackathon24venv //create venv(hackathon24venv) in project folder
# $ source hackathon24venv/bin/activate //to enter venv
# $ python --version //should be 3.11.10 when ran within venv
# $ deactivate //to exit venv
# }
#
# work in hackathon24venv from now on
# $ source hackathon24venv/bin/activate //to enter venv
# $ pip install --upgrade pip // 24.2
# https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies
# $ pip install --upgrade pandas // 2.2.3
# $ pip install --upgrade numpy // 2.1.1
# $ pip install --upgrade matplotlib // 3.9.2
# $ pip install --upgrade torch // 2.4.1
# $ pip install --upgrade tensorflow // 2.17.0
# $ pip freeze | wc -l //67
# $ pip check //"No broken requirements found."
#
# MANUAL INSTALL SHOULD BE COMPLETE, MAKE SURE SCRIPT PASSES NOW: execute main.py
#
# --------------------------------------------------------------------------------

import sys
import numpy as np # numpy==1.26.4
import matplotlib # matplotlib==3.9.2
import pandas as pd # pandas==2.2.3
import torch # torch==2.4.1
import tensorflow # tensorflow==2.17.0
import geopandas as gpd

def check_package_versions(verbose=True):
    #use by importing into main script, then call it and use its return status to determine if program should abort
    #returns True if no errors

    all_passed = True
    if verbose:
        print("-" * 80)
        print("\t\tChecking main package versions")

    curr_python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    required_versions = {
            "python": "3.11.10",
            "numpy": "1.26.4",
            "pandas": "2.2.3",
            "matplotlib": "3.9.2",
            "torch": "2.4.1+cu121",
            "tensorflow": "2.17.0",
            "geopandas": "1.0.1"
        }
    packages_to_check = {
            "numpy": np,
            "pandas": pd,
            "matplotlib": matplotlib,
            "torch": torch,
            "tensorflow": tensorflow,
            "geopandas": gpd
        }
    results = []
    
    #check python version
    if curr_python_version != required_versions["python"]:
        results.append(f"Error on Python. Version Required: {required_versions['python']}, Installed: {curr_python_version}")
        all_passed = False

    #check packages defined in above dictionairies "required_versions" + "packages_to_check"
    for package, module in packages_to_check.items():
        installed_version = module.__version__
        if verbose:
            print(f"{package} version: {installed_version}")

        if installed_version != required_versions[package]:
            results.append(f"Error on {package}. Version Required: {required_versions[package]}, Installed: {installed_version}")
            all_passed = False

    if verbose:
        if all_passed:
            print(f"{'-'*80}\nAll Version Checks Passed\n{'-'*80}")
        else:
            print(f"{'-'*80}\nVersion Check Failures:\n")
            for result in results:
                print(result)
            print(f"{'-'*80}")

    return all_passed

if __name__ == "__main__":
    check_package_versions()