import sys, os
import subprocess as sp
from pathlib import Path 
import re

# AUX endings
aux = (".toc", ".snm", ".out", ".nav", ".aux", ".log", ".vrb", ".dvi", ".fls", ".gz")
outfile = Path("./Slides.pdf")


def main(argv):
    # Collecting the filenames 
    filenames = [Path(f).stem for f in argv]
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
    # Run latex compiler until output does not change
    while not bool(re.search(fr"File `{outfile.stem}.out' has not changed","|".join(logfile))):
        sp.run(["pdflatex", "-jobname=%s"%outfile.stem,"main.tex"]) 
        with open(f"{outfile.stem}.log","r") as f:
            logfile = f.readlines()

    # Deleting the aux files 
    in_dir =tuple(map(Path,os.listdir()))
    in_sections = tuple(f for f in Path("./sections").iterdir() if f.is_file())
    for f in in_dir+in_sections:
        if f.suffix in aux:
            f.unlink()
    
    # Determine the operating system (Windows or Linux) and opening the resulting file
    if os.name == "posix":
        # Linux or macOS
        command = ["xdg-open", outfile.name]
    else:
        # Windows
        command = ["start", outfile.name]
    
    #sp.run(command, shell=True)


if __name__ == "__main__":
    argv = [a for a in sys.argv if a!="python" and a[0]!="-"]
    main(argv[1:])
