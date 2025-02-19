#include <stdio.h>
#include <math.h>

// Function to compute factorial
double factorial(int n){
    double result = 1.0;
    for(int i = 1; i <= n; i++) 
        result *= i;

    return result;
}

// Function to compute e^x using Maclaurin series
double maclaurin_exp(double x, int terms){
    double result = 0.0;
    for (int n = 0; n < terms; n++)
        result += pow(x, n) / factorial(n);

    return result;
}

int main(){
    double x = 2.0;
    int terms = 10;

    double approx = maclaurin_exp(x, terms);
    double exact = exp(x);

    printf("Maclaurin approximation of e^%.2f: %.6f\n", x, approx);
    printf("Exact value of e^%.2f: %.6f\n", x, exact);

    return 0;
}