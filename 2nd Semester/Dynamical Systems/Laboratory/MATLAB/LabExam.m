clear;
fprintf('\n');
%Problem 14

fprintf('Problem14\n')
alpha = input('significance level (0; 1) = ');
X1 = [4.6 0.7 4.2 1.9 4.8 6.1 4.7 5.5 5.4];  %Steel
X2 = [2.5 1.3 2.0 1.8 2.7 3.2 3.0 3.5 3.4];  %Glass

% a)
% H0 : sigma1 = sigma2 <=> (sigma1^2)/(sigma2^2) = 1
% H1 : sigma1 != sigma2 <=> (sigma1^2)/(sigma2^2) != 1
fprintf('\na)');
[h, p, ci, stats] = vartest2(X1, X2, 'alpha', alpha, 'tail', 'both');


if h == 0
    fprintf('H0 is NOT rejected, i.e. the population variances are equal\n');
    vartype = 'equal';
else
    fprintf('H0 is rejected, i.e. the population variances are NOT equal\n');
    vartype = 'unequal';
end

fprintf('P-value is %3.4f\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', stats.fstat);


% b)
% H0 : miu1 = miu2 <=> miu1 - miu2 = 0
% H1 : miu1 > miu2 <=> miu1 - miu2 > 0
fprintf('\nb)');

[h, p, ci, stats] = ttest2(X1, X2, 'alpha', alpha, 'tail', 'right', 'vartype', vartype);

if h == 0
    fprintf('H0 is NOT rejected, i.e. the steel does NOT seem to be higher for glass\n');
else
    fprintf('H0 is rejected, i.e. the steel seems to be higher for glass\n');
end
fprintf('P-value is %e\n', p);
fprintf('Observed value of the test statistics is %3.4f\n', stats.tstat);
fprintf('\n');
