clear;
Nx = 50;
Ny = 50;
d = 1/Nx;
alpha = 1;
Tb = [10 20 30 40];

% Column of ones, size N equations
e = ones(Nx*Ny,1);
% Fill sparse matrix
A = spdiags([e,e,-4*e,e,e],[-Nx,-1,0,1,Nx],Nx*Ny,Nx*Ny);
% A = A*alpha/d^2; % This doesnt matter, steady state...
% Right hand side vector
b = zeros(Nx*Ny,1);

i = 1:Nx;
% Lower boundary
j = 1;
low = i + Nx * (j-1);
% Upper boundary
j = Ny;
upp = i + Nx * (j-1);

j = 1:Ny;
% Left boundary
i = 1;
lef = i + Nx * (j-1);
% Right boundary
i = Nx;
rig = i + Nx * (j-1);

% Collect all boundary node indices
ind = [low upp lef rig];
% Reset these rows to zero
A(ind,:) = 0;
B = ones(Nx*Ny,1)
A = spdiags(B,0,A);

% Set rhs for boundaries
b(low) = Tb(1);
b(upp) = Tb(2);
b(lef) = Tb(3);
b(rig) = Tb(4);

tic
T = A\b;
toc


T = reshape(T,[Nx,Ny]);

[x y] = meshgrid(1:Nx,1:Ny);
surf(x,y,T)
