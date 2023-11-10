Nx = 100;
Nt = 4000;
Dax = 1e-8;
cL = 1;
cR = 0;
tend = 5000;
length = 5e-3;

dt = tend/Nt;
dx = length/Nx;

Fo = Dax*dt/(dx*dx);

x = linspace(0, length, Nx+1);

A = sparse(Nx+1,Nx+1);
A(1,1) = 1;
for i=2:Nx
    A(i,i-1) = -Fo;
    A(i,i)   = 1 + 2*Fo;
    A(i,i+1) = -Fo;
end;
A(Nx+1,Nx+1) = 1;
A(Nx+1,Nx) = -1;

c = zeros(Nt+1,Nx+1);
c(:,1) = cL;
for n=1:Nt
    b = c(n,:)';
    b(Nx+1) = 0;
    c(n+1,:) = A\b;
end

out = [12.6 62.5 125 625 5000];
outdt = fix(out/dt);
plot(x,c(outdt,:))