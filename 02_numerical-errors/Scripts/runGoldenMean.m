N = 50;

y1 = goldenMeanRecurrent(N)
y2 = goldenMeanPowerlaw(N)

figure;
subplot(1,2,1);
plot(y1,y2);
title('Parity plot on lin-scale');
xlabel('y1'); ylabel('y2');

subplot(1,2,2);
loglog(y1,y2,'+-r',[1e-12 1],[1e-12 1], '-k');
title('Parity plot on log-scale')
xlabel('y1'); ylabel('y2');