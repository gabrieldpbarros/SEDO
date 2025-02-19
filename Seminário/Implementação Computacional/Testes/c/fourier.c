#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Function to compute Fourier series approximation of a square wave
double fourier_square_wave(double x, int terms){
    double result = 0.0;
    for (int n = 1; n <= terms; n += 2) // Only odd harmonics
        result += (4.0 / (M_PI * n)) * sin(n * x);

    return result;
}

int main(){
    int terms = 10; // Number of harmonics
    double start = -2 * M_PI;
    double end = 2 * M_PI;
    int num_points = 1000; // Number of points to evaluate
    FILE *arquivo = fopen("fourier_data.txt", "w");

    for(int i = 0; i < num_points; i++){
        double x = start + (end - start) * i / (num_points - 1);
        double y = fourier_square_wave(x, terms);
        fprintf(arquivo, "%.4f\t%.4f\n", x, y);
    }

    fclose(arquivo);

    return 0;
}