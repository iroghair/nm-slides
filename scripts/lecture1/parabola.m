function x = parabola(a,b,c)

% Catch exception cases
if (a==0)
    if(b==0)
        if(c==0)
            disp('Solution indeterminate');
            return;
        end
        disp('There is no solution');
        return;
    end
    x = -c/b;
    return;
end

D = b^2 - 4*a*c;
if (D<0)
    disp('Complex roots');
    return;
else if (D==0)
        x = -b/(2*a);
        else if (D>0)
                x(1) = (-b + sqrt(D))/(2*a);
                x(2) = (-b - sqrt(D))/(2*a);
                x = sort(x);
            end
    end
end

