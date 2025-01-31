#!/bin/bash

# Generate chapters for the slides
chapters=("introduction" "programming1" "programming2" "numericalerrors" "linear1" "linear2" "linear3" "nonlin1" "nonlin2" "interpolation" "integration" "ode1" "ode2" "pde" "optimization")

for chapter in "${chapters[@]}"; do
    echo "Processing chapter: $chapter"
    python render.py "$chapter"
    python render.py "$chapter"
done