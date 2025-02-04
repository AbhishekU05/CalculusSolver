#include <iostream>

double f(double x)
{
    return (x * x * x - 3 * x * x + 2 * x - 1);
}

int main()
{
    double a, b, l, in;

    std::cout << "Enter a and b:\n";
    std::cin >> a >> b;

    in = (b-a)*(f(a) + 4*f((a+b)/2) + f(b)) /6;
    std::cout << "Integral:" << in;
}