p(1) = 1;
p(2) = 1;
diff = 1;
c = 3;
while (diff > 1e-2)
    p(c) = p(c-1)+p(c-2);
    diff = p(c)-p(c-1);
    c=c+1;
end

    