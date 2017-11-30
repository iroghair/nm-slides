function demo_lsqnonlin

data = load('tudataset1.mat')
U = data.U;
T = data.T;

k0 = [1 0.5];
lb = [-Inf -Inf];
ub = [Inf Inf];

k = lsqnonlin(@fitcrit,k0,lb,ub,[],T,U);

[ts,us] = ode45(@simpleode,T,0,[],k);

plot(T,U,'.')
hold on;
plot(ts,us,'-')

    function [dudt] = simpleode(t,u,k)
        dudt = -k(1)*u + k(2);
    end

    function [err] = fitcrit(k, T_exp, U_exp)
        k
        [tsim,usim] = ode45(@simpleode,T_exp,0,[],k);
        
        err = (U_exp - usim);
    end
end

