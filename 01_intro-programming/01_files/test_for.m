p(1) = 1;
p(2) = 1;
for i = 2:10
    p(i+1) = p(i) + p(i-1);
end

p