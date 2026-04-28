#include <stdio.h>
#include <omp.h>

int main(int argc, char* argv[]){
   int n;
   int thread_count = strtol(argv[1], NULL, 10);
   printf("\nEnter array size : ");
   scanf("%d", &n);
   int A[n], B[n], C[n];
   int i;
   srand(time(NULL));
   for(i=0; i<n; i++){
      A[i] = rand()%10;
      B[i] = rand()%5;
   }
   printf("\nArray A: ");
   for(i=0; i<n; i++)
      printf("%d ", A[i]);
   printf("\nArray B: ");
   for(i=0; i<n; i++)
      printf("%d ", B[i]);

#pragma omp parallel for num_threads(thread_count)
   for(i=0; i<n; i++)
      C[i] = A[i] + B[i];

   printf("\nSum Elements after addition:\n");
   for(i=0; i<n; i++)
      printf("%d ", C[i]);
   printf("\n\n");
}
