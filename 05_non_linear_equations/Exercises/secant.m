function [p] = secant(f, x1, x2, tol_step, tol_func)
  f1 = f(x1);
  f2 = f(x2);
  fp = f2;
  if (f1*f2>0)
    error('Root must be bracketed!');
  else
    it = 1;
    while ((abs(fp)>tol_func) && (abs(x2 - x1)>tol_step))
      it = it + 1;
      p = (x1*f2 - x2*f1)/(f2 - f1);
      fp = f(p);
      x1 = x2;
      f1 = f2;
      x2 = p;
      f2 = fp;
    end
    disp(sprintf('Root found in %d iterations at x = %e\n (function value = %e)', [it,p,fp])); 
  end
end