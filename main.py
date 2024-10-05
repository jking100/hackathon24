# main script

import sys
import numpy as np # type: ignore # numpy==1.26.4
import matplotlib # type: ignore # matplotlib==3.9.2
import pandas as pd # pandas==2.2.3
import torch # torch==2.4.1
import tensorflow # tensorflow==2.17.0
from my_check_packages import check_package_versions

def main():
    '''
    main is here
    '''
    return None

if __name__ == "__main__":
    if (not check_package_versions()):
        exit("MAIN.PY: Error on pacakge versions. Terminating")
    print("main.py: Environment is good so hello World!")
    main()