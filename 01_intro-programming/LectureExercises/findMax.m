function [m] = findMax(v)
% Sample program: find maximum in array of integers
% Inputs:
%   v: Array of numbers
% Outputs:
%   m: maximum in array v

m = 0;

for i = 1:length(v)
    if (v(i) > m)
        m = v(i);
    end
end

end