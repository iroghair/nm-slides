function [A,b] = setBoundaryConditions(A,b,Tb,Nx,Ny)

% Set boundary conditions over x-direction
for i=1:Nx
    j = 1;
    ind = i + Nx * (j-1);
    A(ind,:) = 0; % Reset matrix for boudary cells
    A(ind,ind) = 1; % Add a 1 on the diagonal
    b(ind) = Tb(1);
    j = Ny;
    ind = i + Nx * (j-1);
    A(ind,:) = 0; % Reset matrix for boudary cells
    A(ind,ind) = 1; % Add a 1 on the diagonal
    b(ind) = Tb(2);
end

% Set boundary conditions over y-direction
for j=1:Ny
    i = 1;
    ind = i + Nx * (j-1);
    A(ind,:) = 0; % Reset matrix for boudary cells
    A(ind,ind) = 1; % Add a 1 on the diagonal
    b(ind) = Tb(3);
    i = Nx;
    ind = i + Nx * (j-1);
    A(ind,:) = 0; % Reset matrix for boudary cells
    A(ind,ind) = 1; % Add a 1 on the diagonal
    b(ind) = Tb(4);
end