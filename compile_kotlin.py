import subprocess 


def compile_kotlin(): 
    subprocess.run("./kotlin_compiler.sh", shell=True)
    create_response()

def create_response():
    with open('response') as r:
        response = r.read()
        return response

