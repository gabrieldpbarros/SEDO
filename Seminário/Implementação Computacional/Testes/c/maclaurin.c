#include <stdio.h>
#include <math.h>
#include <time.h>

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
    for(int n = 0; n < terms; n++)
        result += powl(x, n) / factorial(n);

    return result;
}

int main(){
    double x = 200.0;
    int terms = 2000;

    clock_t start = clock();
    double approx = maclaurin_exp(x, terms);
    clock_t end = clock();

    double exact = exp(x);

    double time = (double) (end - start) / CLOCKS_PER_SEC;

    printf("Maclaurin approximation of e^%.0f: %.6f\n", x, approx);
    printf("Exact value of e^%.0f: %.6f\n", x, exact);
    printf("Execution time: %.15Lf seconds\n", time);

    return 0;
}