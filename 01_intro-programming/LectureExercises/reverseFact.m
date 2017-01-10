function [rv] = reverseFact(in1)

c = 0;
while (round(in1) > 1)
    c=c+1;
    in1 = in1 / c;
end

if (in1 == fix(in1))
    rv = c;
else
    rv = 0;
end

end