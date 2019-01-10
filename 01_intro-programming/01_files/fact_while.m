function Z = fact_while(N)
%% This function computes a factorial of input value N
% Usage: fact_while(N)
% N      : value of which the factorial is computed
% returns: factorial of N


Z = 1;
i = 1;
while (i<=N)
    Z = Z*i;
    i = i+1;
end

end