function x = contfrac(n)
    if n == 1
        x = 1.5;
    else
        x = 1 + 1/contfrac(n-1);
    end