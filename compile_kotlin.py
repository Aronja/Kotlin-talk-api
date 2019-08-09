import subprocess

def compile_kotlin(): 
    subprocess.run("./kotlin_compiler.sh", shell=True)
