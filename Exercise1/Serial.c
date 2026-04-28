#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
   int m, n, p;
   int i, j, k;
   printf("\nEnter value of m, n, p : ");
   scanf("%d %d %d", &m, &n, &p);

   int **A = (int **)malloc(m*sizeof(int*));
   int **B = (int **)malloc(n*sizeof(int*));
   int **C = (int **)malloc(m*sizeof(int*));

   for(i=0;i<m;i++)
      A[i] = (int *)malloc(n*sizeof(int));
   for(i=0;i<n;i++)
      B[i] = (int *)malloc(p*sizeof(int));
   for(i=0;i<m;i++)
      C[i] = (int *)malloc(p*sizeof(int));

   for(i=0;i<m;i++)
      for(j=0;j<n;j++)
         A[i][j]=rand()%5;
   for(i=0;i<n;i++)
      for(j=0;j<p;j++)
         B[i][j]=rand()%5;
   clock_t start=clock();
   for(i=0;i<m;i++){
      for(j=0;j<p;j++){
         C[i][j]=0;
         for(k=0;k<n;k++){
            C[i][j]+=A[i][k]+B[k][j];
         }
      }
   }
   clock_t end=clock();
   double time = ((double)(end-start)*1000.0)/CLOCKS_PER_SEC;
   printf("\nTime taken : %f milliseconds\n\n", time);
}
