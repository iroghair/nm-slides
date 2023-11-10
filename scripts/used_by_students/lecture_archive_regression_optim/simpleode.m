function [dudt] = simpleode(t,u,k)
dudt = -k(1)*u + k(2);
end
