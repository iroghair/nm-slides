# Slides for Numerical Methods
These are the LaTeX source files for my course Numerical Methods (6E5X0), at Eindhoven University of Technology. The course deals with various numerical techniques, highlighting examples and exercises in Matlab. Topics are numerical errors, integration, interpolation, (systems of) (non-)linear equations, ODEs and PDEs, and optimization.

Some initial commits were artificially set to an earlier (reasonable) commit date to allow for some chronological ordering/evolution of these files over the years. 

## Compilation
To compile simply use:

`python render.py <filename>`

Where the filename does not have to contain the extension.

Example:

`python -m render introduction`

## Completed sections (testing the code and aligning the slides):
 - [x] integration
 - [x] interpolation
 - [x] introduction
 - [x] linear1
 - [x] linear2
 - [x] linear3
 - [x] nonlin
 - [x] numericalerrors
 - [x] ode1
 - [x] ode2
 - [x] optimization
 - [x] pde
 - [x] programming1
 - [x] programming2

All slides in the right order:
```
python render.py introduction programming1 programming2 numericalerrors linear1 linear2 linear3 nonlin1 nonlin2 interpolation integration ode1 ode2 pde optimization
```

## Todo (by priority after testing the code)
1. Make sure the story flows correctly (specially due to modules)
✅ Fix the issue with the table of contents not showing
3. Correct debugger information in programming2? (Ask ivo about which IDE)
4. Replace all the matlab generated images (programming2 has wrong 3d image as well)
5. Add animations to appropriate slides
6. Place important scripts in a specific folder instead of in text
7. Make rendering work with old make-file
8. Fix the progress bar gradient, it looks iffy
9. What's the notepad-displayed equation in python-versatility.pdf?
10. Transitions between slides using `(*@  @*)` seem to have stopped working (e.g. `(*@ \pause @*)`)
11. Convert references with `.format` to f-strings