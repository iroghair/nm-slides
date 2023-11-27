def brent_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have different signs.")
    # Initialize variables
    c = a
    fa = f(a)
    fb = f(b)
    fc = fa
    history = [a, b]
    d = e = b - a
    for _ in range(max_iter):
        if fa * fc > 0:
            c = a
            fc = fa
            d = e = b - a
        if abs(fc) < abs(fb):
            a, b, c = b, c, a
            fa, fb, fc = fb, fc, fa
        tol1 = 2 * 1.0e-16 * abs(b) + 0.5 * tol
        xm = 0.5 * (c - b)
        if abs(xm) <= tol1 or fb == 0:
            return b, history
        if abs(e) >= tol1 and abs(fa) > abs(fb):
            s = fb / fa
            if a == c:
                # Linear interpolation (Secant method)
                p = 2 * xm * s
                q = 1 - s
            else:
                # Inverse quadratic interpolation
                q = fa / fc
                r = fb / fc
                p = s * (2 * xm * q * (q - r) - (b - a) * (r - 1))
                q = (q - 1) * (r - 1) * (s - 1)
            if p > 0:
                q = -q
            p = abs(p)

            if 2 * p < min(3 * xm * q - abs(tol1 * q), abs(e * q)):
                e = d
                d = p / q
            else:
                d = xm
                e = d
        else:
            d = xm
            e = d
        a = b
        fa = fb
        if abs(d) > tol1:
            b += d
        else:
            b += tol1 if xm > 0 else -tol1

        fb = f(b)
        history.append(b)
    raise ValueError("Maximum number of iterations reached.")

# Usage
if __name__ == "__main__":
    f = lambda x: 3*x**2 - 6*x + 2
    a = 1
    b = 2
    root, history = brent_method(f, a, b)
    print(f"Root: {root}")
    print(f"Number of iterations: {len(history) - 1}")
