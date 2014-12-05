function [dxdt] = myODEFunction(t,x,N)
c_tot = 13.9602;
D12 = 1.6e-3;
dxdt(1) = -(1+x)/(c_tot*D12) * N;
return