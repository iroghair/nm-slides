# Slides for Numerical Methods
These are the LaTeX source files for my course Numerical Methods (6E5X0), at Eindhoven University of Technology. The course deals with various numerical techniques, highlighting examples and exercises in Matlab. Topics are numerical errors, integration, interpolation, (systems of) (non-)linear equations, ODEs and PDEs, and optimization.

Some initial commits were artificially set to an earlier (reasonable) commit date to allow for some chronological ordering/evolution of these files over the years. 

## Compilation
I generally use the Makefile in the repository to compile slides for a particular lecture. For instance, to compile the slides for the lecture on solving linear systems:

```
make linear
```

This creates the lectures on linear systems. This lecture consists of 3 parts, compiled in a single pdf. If you just want a single part of the lecture, use for instance `make linear1`. See the Makefile for more details on what works.

The part compilation is based on LaTeX beamer, the Makefile creates a one-liner includes.tex file in which the parts that need to be compiled are given. This file hence refreshes each you switch topic.

The slides use a covering mechanism to mimic hide/appear animations which is useful for telling the story, but for handouts (and print especially) this is not very handy. You can switch to handout mode by adding the `handout` option in the documentclass option list. Some slides are entirely hidden in one or the other document type.
