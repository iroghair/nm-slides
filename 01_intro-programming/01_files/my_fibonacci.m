p(1) = 1;
p(2) = 1;

for i = 3:10
    p(i) = p(i-1) + p(i-2);
end

p