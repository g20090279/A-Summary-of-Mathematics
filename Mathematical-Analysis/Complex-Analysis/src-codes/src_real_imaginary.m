% real and imaginary properties

a = randi(100)-50 + 1i*(randi(100)-50);
b = randi(100)-50 + 1i*(randi(100)-50);

% addition
disp('Properties of Addition');
disp(['real of addition: ', num2str(real(a+b))]);
disp(['addition of real: ', num2str(real(a)+real(b))]);
disp(['imaginary of addition: ', num2str(imag(a+b))]);
disp(['addition of imaginary: ', num2str(imag(a)+imag(b))]);

% multiplication
disp('---')
disp('Properties of Multiplication')
disp(['real of multiplication: ', num2str(real(a*b))]);
disp(['multiplication of real plus imaginary: ', num2str(real(a)*real(b)-imag(a)*imag(b))]);
disp(['imaginary of multiplication: ', num2str(imag(a*b))]);
disp(['multiplication of real plus imaginary: ', num2str(imag(a)*real(b)+real(a)*imag(b))]);
