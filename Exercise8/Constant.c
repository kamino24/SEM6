#include <stdio.h>
#include <omp.h>

int main(int argc, char* argv[]){
   int n;
   int thread_count = strtol(argv[1], NULL, 10);
   printf("\nEnter array size : ");
   scanf("%d", &n);
   int A[n];
   int i, con;
   printf("Enter constant value : ");
   scanf("%d", &con);
   srand(time(NULL));
   for(i=0; i<n; i++){
      A[i] = rand()%10;
   }
   printf("\nArray A: ");
   for(i=0; i<n; i++)
      printf("%d ", A[i]);

#pragma omp parallel for num_threads(thread_count)
   for(i=0; i<n; i++)
      A[i] = A[i] + con;

   printf("\nElement after addition of constant:\n");
   for(i=0; i<n; i++)
      printf("%d ", A[i]);
   printf("\n\n");
}
