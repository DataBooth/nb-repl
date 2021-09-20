import jupyter
import os

def run_notebook(dotipynb_filename=''):
  print("Starting Jupyter notebook...")
  print("")
  print(f"jupyter notebook {dotipynb_filename} --ip 0.0.0.0 --port 3000")
  print("")
  os.system(f"jupyter notebook {dotipynb_filename} --ip 0.0.0.0 --port 3000")
