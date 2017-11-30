function [xc,yc,Tc,A,b] = solveLaplaceEq(Nx,Ny)
%% Solves the Laplace equation for steady-state heat conduction
% Usage: [xc,yc,Tc,A,b] = solveLaplaceEq(Nx,Ny)
%
% Inputs: 
%       Nx, Ny: field dimensions
% Outputs: 
%       xc, yc: field coordinates
%       Tc: temperature field
%       A,b: matrix and RHS

%% Default case
if (nargin < 2)
    Nx = 15;
    Ny = 15;
end

%% Set up parameters and boundary conditions
d = 1/Nx;                           % Grid spacing
alpha = 1;                          % Heat conduction
Tb = [10 20 30 40];                 % Fixed boundary temperatures

%% Fill sparse matrix with [1 1 -4 1 1]
e = ones(Nx*Ny,1);
A = spdiags([e,e,-4*e,e,e],[-Nx,-1,0,1,Nx],Nx*Ny,Nx*Ny);
A = A*alpha/d^2;                    % This doesnt matter, steady state...
b = zeros(Nx*Ny,1);                 % Right hand side vector

%% Apply boundary conditions
[A,b] = setBoundaryConditions(A,b,Tb,Nx,Ny);

tic
% T = A\b;                                    % Solve matrix
[T,it] = solveJacobi(A,b,1e-1);
toc

%% Post-processing
Tc = reshape(T,[Nx,Ny]);                     % Reshape x-vec to mat Nx,Ny
[xc yc] = meshgrid(1:Nx,1:Ny);               % Get position arrays
surf(xc,yc,Tc)                               % Surface plot

