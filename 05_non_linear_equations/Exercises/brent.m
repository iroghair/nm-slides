function [root] = brent(f, x1, x2, tol)
  ITMAX = 100;  
  EPS = 3e-8;
  a = x1; b = x2; c = x2;
  fa = f(a);
  fb = f(b);
  fc = fb;
  if (fa*fb>0)
    error('Root must be bracketed!');
  else
    for iter=1:ITMAX
      if (fb*fc>0)
        c = a;  fc = fa;      % Rename a, b, c and 
        d = b - a;  e = d;    % adjust bounding interval d
      end;
      if (abs(fc)<abs(fb)) 
        a = b;  fa = fb;
        b = c;  fb = fc;
        c = a;  fc = fa;
      end;
      tol1 = 2.0*EPS*abs(b) + 0.5*tol; % Convergence check.
      xm = 0.5*(c - b);
      if ((abs(xm)<=tol1) || (fb == 0)) 
        root = b;
        disp(sprintf('\nRoot found in %d iterations at x = %e (f(x) = %e)', [iter,b,fb])); 
        break;
      end;
      if ((abs(e)>=tol1) && (abs(fa)>abs(fb))) 
        % Attempt inverse quadratic interpolation.  
        s = fb/fa; 
        if (a==c) 
          p = 2.0*xm*s;
          q = 1.0 - s;
        else 
          q = fa/fc;
          r = fb/fc;
          p = s*(2.0*xm*q*(q - r) - (b - a)*(r - 1.0));
          q = (q - 1.0)*(r - 1.0)*(s - 1.0);
        end;
        if (p>0.0) 
          q = -q; % Check whether in bounds.
        end;
        p = abs(p);
        min1 = 3.0*xm*q - abs(tol1*q);
        min2 = abs(e*q);       
        if (2.0*p<min(min1,min2)) 
          e = d; % Accept interpolation.
          d = p/q;
        else 
          d = xm; % Interpolation failed, use bisection.
          e = d;
        end;
      else
         d = xm; % Bounds decreasing too slowly, use bisection.
         e = d;
      end;
      a = b; % Move last best guess to a.
      fa = fb;
      if (abs(d)>tol1) % Evaluate new trial root.
        b = b + d;
      else
        if (xm<0)
          b = b - tol1;
        else
          b = b + tol1;
        end;
      end;
      fb = f(b);     
      if (d == xm)
        disp(sprintf('Iteration: %d => x = %e, f(x) = %e (bisection)', [iter,b,fb])); 
      else
        disp(sprintf('Iteration: %d => x = %e, f(x) = %e (inverse quadratic interpolation)', [iter,b,fb]));           
      end;
    end;
    if (iter==ITMAX) 
      disp('Maximum number of iterations exceeded in brent!'); 
    end;
  end;
end

