function [tf] = isMagic(A)

if (size(A,1) ~= size(A,2)
    tf = false;
    return
end

for i = 1:size(A,1)
    r(i) = sum(A(:,i));
    c(i) = sum(A(:,i));
end

for j = 1:size(r)
    if r(j) ~= c(j) || r(j) ~= 
if isequal(r,c)
    tf = true;
else
    tf = false;
end
    