Nx = 2000;
Nt = 200000;
Dax = 1e-8;
cL = 1;
cR = 0;
tend = 50;
length = 5e-3;

dt = tend/Nt;
dx = length/Nx;

Fo = Dax*dt/(dx*dx);

x = linspace(0, length, Nx+1);

e = ones(Nx-1,1);
ld = [Fo*e; 0; 0];
md = [1; (1-2*Fo)*e; 1];
ud = [0; 0; Fo*e];
A = spdiags([ld md ud], [-1 0 1], Nx+1, Nx+1);

c = zeros(Nt+1,Nx+1);
c(:,1) = cL;
c(:,Nx+1) = cR;
c = c';

tic
for n=1:Nt
   c(:,n+1) = A*c(:,n);
end
toc

c = c';
outdt = fix(linspace(1,Nt,min(Nt,10)));
% out = [12.6 62.5 125 625 5000];
% outdt = fix(out/dt);
plot(x,c(outdt,:))