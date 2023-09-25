# Slides for Numerical Methods
These are the LaTeX source files for my course Numerical Methods (6E5X0), at Eindhoven University of Technology. The course deals with various numerical techniques, highlighting examples and exercises in Matlab. Topics are numerical errors, integration, interpolation, (systems of) (non-)linear equations, ODEs and PDEs, and optimization.

Some initial commits were artificially set to an earlier (reasonable) commit date to allow for some chronological ordering/evolution of these files over the years. 

## Compilation
To compile simply use:

`python render.py <filename>`

Where the filename does not have to contain the extension. This will automatically open the resulting slide as well.

Example:

`python -m render introduction`

## Completed sections (testing the code and aligning the slides):
 - [ ] integration
 - [ ] interpolation
 - [x] introduction
 - [ ] linear1
 - [ ] linear2
 - [ ] linear3
 - [ ] nonlin
 - [ ] numericalerrors
 - [ ] ode1
 - [ ] ode2
 - [ ] optimization
 - [ ] pde
 - [x] programming1
 - [x] programming2
 - [ ] programming2_old

## Todo (by priority after testing the code)
1. Make sure the story flows correctly (specially due to modules)
2. Fix the issue with the table of contents not showing
3. Correct debugger information in programming2? (Ask ivo about which IDE)
4. Replace all the matlab generated images (programming2 has wrong 3d image as well)
5. Add animations to appropriate slides
6. Place important scripts in a specific folder instead of in text
7. Make rendering work with old make-file