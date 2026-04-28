#include <stdio.h>
#include <omp.h>

int main(int argc, char* argv[]){
   int n, win;
   int thread_count = strtol(argv[1], NULL, 10);
   printf("\nEnter array size : ");
   scanf("%d", &n);
   int arr[n];
   printf("Enter window size : ");
   scanf("%d", &win);

   printf("\nArray: ");
   int i;
   srand(time(NULL));
   for(i=0; i<n; i++){
      arr[i] = rand() % 10;
      printf("%d ", arr[i]);
   }

   int total = (n-win)+1;
   int res[total];
   int j;

#pragma omp parallel for num_threads(thread_count)
   for(i=0; i<total; i++){
      int sum = 0;
      for(j=i; j<i+win; j++){
         sum += arr[j];
      }
      res[i] = sum;
   }
   printf("\nSum: ");
   for(i=0; i<total; i++)
      printf("%d ", res[i]);
   printf("\n\n");
}