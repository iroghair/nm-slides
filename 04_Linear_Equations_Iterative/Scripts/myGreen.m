function [g] = myGreen(x,D,t)

g = 1/(sqrt(4*pi*D*t)) * exp(-(x.^2./(4*D*t)));