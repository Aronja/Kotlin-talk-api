from compile_kotlin import compile_kotlin, create_response
from parse_kotlin import parse_kotlin


def process_kotlin(request):
        parse_kotlin(request)
        compile_kotlin()   
        return create_response()