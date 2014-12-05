[x y] = meshgrid(-2:0.1:2, -2:0.1:2);
z = x .* y .* exp(-x.^2 - y.^2)

figure;
surf(x,y,z);
title 'Surface plot'
xlabel('x'); ylabel('y'); zlabel('z');

figure;
v=-0.5:0.05:0.5;
contour(x,y,z,v,'ShowText', 'on');
title 'Contour plot'
xlabel('x'); ylabel('y'); zlabel('z');

figure;
waterfall(x,y,z);
title 'Waterfall'
xlabel('x'); ylabel('y'); zlabel('z');


figure;
ribbon(z);
title 'Ribbon'
xlabel('x'); ylabel('y'); zlabel('z');

[x y] = meshgrid(-2:0.2:2, -2:0.2:2);
z = x .* y .* exp(-x.^2 - y.^2)
[dx dy] = gradient(z,8,8)
figure;
contourf(x,y,z,30,'LineColor','none');
colormap(hot)
axis tight
colorbar
hold on;
quiver(x,y,dx,dy,'k');
title 'Vector plot'
xlabel('x'); ylabel('y'); zlabel('z');
