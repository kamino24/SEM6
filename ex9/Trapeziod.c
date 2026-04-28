#include <stdio.h>
#include <omp.h>

double f(double x) {
    return x * x;
}

int main() {
    int n, i;
    double a, b, h;
    double integral_pf = 0.0, integral_red = 0.0, integral_crit = 0.0;

    printf("\nEnter lower limit (a): ");
    scanf("%lf", &a);

    printf("Enter upper limit (b): ");
    scanf("%lf", &b);

    printf("Enter number of trapezoids (n): ");
    scanf("%d", &n);

    h = (b - a) / n;

    integral_pf = (f(a) + f(b)) / 2.0;

    #pragma omp parallel for
    for (i = 1; i < n; i++) {
        double x = a + i * h;

        #pragma omp critical
        integral_pf += f(x);
    }

    integral_pf *= h;

    double sum = 0.0;

    #pragma omp parallel for reduction(+:sum)
    for (i = 1; i < n; i++) {
        double x = a + i * h;
        sum += f(x);
    }

    integral_red = (f(a) + f(b)) / 2.0 + sum;
    integral_red *= h;

    double sum2 = 0.0;

    #pragma omp parallel for
    for (i = 1; i < n; i++) {
        double x = a + i * h;
        double temp = f(x);

        #pragma omp critical
        sum2 += temp;
    }

    integral_crit = (f(a) + f(b)) / 2.0 + sum2;
    integral_crit *= h;

    printf("\nResult using Parallel For + Critical: %lf\n", integral_pf);
    printf("Result using Reduction: %lf\n", integral_red);
    printf("Result using Critical: %lf\n\n", integral_crit);

    return 0;
}
