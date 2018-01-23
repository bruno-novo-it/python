# To install the Python YAML Parser:
# 
# pip install pyyaml

import yaml
import sys

try:
    apk_path = sys.argv[1]
    features_path = sys.argv[2]
    no_run_tag = sys.argv[3]
    number_of_devices = int(sys.argv[4])
    profile = sys.argv[5]
    report_output_format = sys.argv[6]
    scenario_tag = sys.argv[7]
except IndexError:
    scenario_tag = ''


config_file = {'Parameters':{'apk_path':apk_path, 'features_path':features_path, 'no_run_tag':no_run_tag,'number_of_devices':number_of_devices, \
    'profile':profile, 'report_output_format':report_output_format, 'scenario_tag':scenario_tag}}

with open('config.yml', 'w') as yaml_file:
    yaml.dump(config_file, yaml_file, default_flow_style=False)

# python make_yml.py app-prd.apk features/android/features/ instrumentado 2 android html

# python make_yml.py app-prd.apk features/android/features/ '' 2 android html