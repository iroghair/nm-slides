format long e

N = 4;

opt = optimset('Display','iter');
flux = fzero(@RunBVP,N,opt)

[z,x] = ode45(@BVPODE,[0 1e-3],[0.2], [], flux);
figure; plot(z,x)
