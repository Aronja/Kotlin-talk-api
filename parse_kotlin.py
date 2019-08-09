import json
import os 


def parse_kotlin(request):
    kotlin_file = open('kotlin.kt', 'w')
    kotlin_file.write(reformatter(request.json))
    return kotlin_file

def reformatter(json):
    return json.get("name", "weird error caused by mysterious reasons")
