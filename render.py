import sys, os
import subprocess as sp
from pathlib import Path 
import re

# AUX endings
aux = (".toc", ".snm", ".out", ".nav", ".aux", ".log", ".vrb", ".dvi", ".fls", ".gz")
latex_exec = "pdflatex"
infile = "main.tex"

def render(argv):
    # Collecting the filenames 
    filenames, outfile = get_input_output_filenames(argv)

    f_sep_commas = ",".join([f for f in filenames])
    f_with_path = ",".join(["sections/%s"%f for f in filenames])

    # Writing includes to include.tex
    if filenames:
        includes = "\\includeonlylecture{%s}\n\\includeonly{%s}"
        includes = includes%(f_sep_commas, f_with_path)
    else:
        includes = ""

    with open("./preamble/include.tex","w") as f:
        f.write(includes)

    # Rendering them using latex
    # Check if the logfile exists
    logfile = ''
    sp.run([latex_exec, "-interaction=nonstopmode","-jobname=%s"%outfile.stem,infile])
    
    run = 0
    # Run latex compiler until output does not change
    while not re.search(fr"File `{outfile.stem}.out' has not changed","|".join(logfile)) and (run := run+1) < 4:
        sp.run([latex_exec, "-interaction=nonstopmode","-jobname=%s"%outfile.stem,infile]) 
        with open(f"{outfile.stem}.log","r") as f:
            logfile = f.readlines()

def get_input_output_filenames(argv):
    filenames = [Path(f).stem for f in argv]
    print(filenames)
    outnames = '_'.join(filenames)
    with open(infile,'r') as file:
         data = file.readlines()
         for line in data:
             if line.startswith('\documentclass'):
                 if bool(re.findall('handout',line)):
                     outfile = Path(outnames.title() + ".pdf")
                 else:
                     outfile = Path("Lecture" + outnames.title() + ".pdf")

    return filenames, outfile
   
def clean(argv):
    # Delete the auxiliary files 
    in_dir = tuple(map(Path,os.listdir()))
    in_sections = tuple(f for f in Path("./sections").iterdir() if f.is_file())
    for f in in_dir+in_sections:
        if f.suffix in aux:
            f.unlink()

def view(argv):
    _, outfile = get_input_output_filenames(argv)
    # Determine the operating system (Windows or Linux) and opening the resulting file
    if os.name == "posix":
        # Linux or macOS
        command = ["xdg-open", outfile.name]
    else:
        # Windows
        command = ["start", outfile.name]

    sp.run(command)
    

if __name__ == "__main__":
    argv = [a for a in sys.argv if a!="python" and a[0]!="-"]
    if 'clean' in argv:
        clean(argv[1:])
    # elif 'view' in argv:
    #     view(argv[1:])
    else:
        render(argv[1:])
