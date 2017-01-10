function [gcd] = euclidean(a,b)

% Sanity check
if (~isinteger(a) | ~isinteger(b))
    error('Please provide two integers...');
end
    
k = 0;
