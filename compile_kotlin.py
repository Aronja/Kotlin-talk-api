import subprocess

def compile_kotlin(kotlin_file): 
    subprocess.call("./kotlin_compiler.sh", shell=True)
