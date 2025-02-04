#include <iostream>
#include <math.h>

double f(double x)
{
    return (exp(x));
}

int main()
{
    long double x, diff;

    std::cout << "Enter x: ";
    std::cin >> x;

    /*
    for (long double h = 1; h >= 1.e-30; h /= 10) {
        diff = (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h))/(12*h);
        std::cout << "h=" << h << "\n" << "f'(x)=" << diff << "\n";
        std::cout << "--------------\n";
    }
    */

    const long double epsilon = 2.2e-16;
    double g = (f(x+1) + f(x-1) - 2*f(x));
    const long double h = 2*sqrt(epsilon*f(x)/g);

    diff = (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h);
    std::cout << "h=" << h << "\n" << "f'(x)=" << diff << "\n";
    std::cout << "--------------\n";
}