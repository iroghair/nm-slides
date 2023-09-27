function [y] = curve_fit_model(a,xdata)

y = a(1)*xdata.^3+a(2)*xdata.^2 + a(3)*xdata + a(4);
end