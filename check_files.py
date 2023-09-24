import re
import shutil
import numpy as np
from pathlib import Path 
from itertools import chain 

EXTS = ".pdf .png .jpg .dat .txt .m .eps .fig .gif".split()

def read_file(fname):
    with open(fname, "r") as f:
        return f.read()
            
def find_files_in_tex(fname, pats):
    # Reading the text
    t = read_file(fname)

    # Extracting filenames for each pattern
    fnames = [re.findall(p, t) for p in pats]

    # Making all filenames in the same line
    files = chain(*fnames)
    return files

def find_all_files(parent_dir, endings):
    files = set()
    for f in Path(parent_dir).iterdir():
        if f.is_dir():
            files = files | find_all_files(f,endings)
        elif f.suffix in endings:
            files.add(f)
    return set(files) 

def find_all_files_in_tex(parent_dir, pats):
    tex_files = find_all_files(parent_dir, [".tex"])
    fname_groups = []
    for tf in tex_files:
        fname_groups.append(find_files_in_tex(tf, pats))
    return set(chain(*fname_groups)) 

def find_to_move(figures, intex):
    to_move = []
    intex_stems = tuple(Path(f).stem for f in intex)
    print(sorted(intex_stems))
    for f in map(Path, figures):
        if not f.stem in intex_stems:
            to_move.append(f)
    return to_move

def main():
    """ Moves unised files to the useless_files directory """
    pats = [r"\\includegraphics(?:<[^>]*>)?(?:\[[^\]]*\])?\{([^\}]*)\}",
            r"\\input\{([^\}]*)\}",
            r"\\addplot\[[^\]]*\]\s*table\s*(?:\[[^\]]*\])?\s*\{([^\}]*)\}",
            r"\\lstinputlisting(?:\[[^\]]*\])?\{([^\}]*)\}"]
    figures = find_all_files(".", EXTS)
    texfiles = find_all_files_in_tex(".", pats)
    to_move = find_to_move(figures, texfiles)
    print("len(figures) = %i"%len(figures))
    print("len(texfiles) = %i"%len(texfiles))
    print("len(to_move)=%i"%len(to_move))
    
    for f in to_move:
        #f.unlink()
        shutil.move(f, "./useless_files")


if __name__ == "__main__":
    main()