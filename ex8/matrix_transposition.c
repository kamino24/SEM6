#include <stdio.h>
#include <omp.h>

int main(int argc, char* argv[]){
   int n;
   int thread_count = strtol(argv[1], NULL, 10);
   printf("\nEnter matrix size : ");
   scanf("%d", &n);
   int mat[n][n], res[n][n];
   int i,j;
   srand(time(NULL));
   printf("\nMatrixA:\n");
   for(i=0; i<n; i++){
      for(j=0; j<n; j++){
         mat[i][j] = rand()%10;
         printf("%d ", mat[i][j]);
      }
      printf("\n");
   }

#pragma omp parallel for num_threads(thread_count)
   for(i=0; i<n; i++)
      for(j=0; j<n; j++)
         res[j][i] = mat[j][n-1-i];
   printf("\nHorizontal mirror matrix:\n");
   for(i=0; i<n; i++){
      for(j=0; j<n; j++)
         printf("%d ", res[i][j]);
      printf("\n");
   }
   printf("\n");
}