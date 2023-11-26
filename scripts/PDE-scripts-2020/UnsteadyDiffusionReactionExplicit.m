Nx = 100;
Nt = 40000;
Dax = 1e-8;
cL = 1;
cR = 0;
tend = 5000;
length = 5e-3;

dt = tend/Nt;
dx = length/Nx;

Fo = Dax*dt/(dx*dx);

x = linspace(0, length, Nx+1);

c = zeros(Nt+1,Nx+1);
c(:,1) = cL;
%c(:,Nx+1) = cR;
for n=1:Nt
    for i=2:Nx
        r = ReactionRate(c(n,i));
        c(n+1,i) = Fo*c(n,i-1) + (1 - 2*Fo)*c(n,i) + Fo*c(n,i+1) + r*dt;
    end
    c(n+1,Nx+1) = c(n+1,Nx);
end

out = [12.6 62.5 125 625 5000];
outdt = fix(out/dt);
plot(x,c(outdt,:))