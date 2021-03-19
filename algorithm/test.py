import os
print(os.path.abspath(os.path.dirname(os.getcwd())))
alg_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'algorithm')
print(alg_path)
print(os.getcwd())



