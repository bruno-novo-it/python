import json
import subprocess

f = open("new_magnet_list.json", "r")
data = f.read()
jsondata = json.loads(data)
#f.close()

# fw = open("new_magnet_list.json", "w")
# json.dump(jsondata,fw,indent=2)
# fw.close()

def execute_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    comm = proc.communicate()

    return comm[0]

for i in jsondata["link"]:
    download_dragon_ball_episode = "transmission-remote -n 'transmission:transmission' --add \"{0}\""
    execute_cmd(download_dragon_ball_episode.format(i))