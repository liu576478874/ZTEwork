import os
import subprocess
import re

def abstract_log():
    

    cmd_git_log=["git","log","-3"]
    proc=subprocess.Popen(cmd_git_log,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr=proc.communicate()
    log=stdout.split('commit')
    return log


def log_output(filename,log):
    fi=open(filename,'w')
    for item in log:
        fi.write(item)
    fi.close()

def run(project_dir,filename):
    os.chdir(project_dir)
    log=[]
    log=abstract_log()
    log_output(filename,log)

if __name__=='__main__':
    project_dir="d:/ccode"
    filename="log"
    run(project_dir,filename)
