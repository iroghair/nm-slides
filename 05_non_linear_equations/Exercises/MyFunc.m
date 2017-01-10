function [f] = MyFunc(x)
  f(1) = x(1)^2 + x(2)^2 - 4;
  f(2) = x(1)^2 - x(2) + 1;
  f = f';
end