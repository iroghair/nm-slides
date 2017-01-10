clear;
clc;
format long e;

A = [[1.2969 0.8648]; [0.2161 0.1441]]
x = [0.8642; 0.1440]
y = A \ x

A2 = single(A)
x2 = single(x)
y2 = A2\x2