#include<stdio.h>
#include<omp.h>
int main(){
   int n,i;
   printf("\nEnter the no.of elements : ");
   scanf("%d",&n);
   int ar[n];
   printf("Enter the elements : ");
   for(i=0;i<n;i++){
      scanf("%d",&ar[i]);
   }
   int thread_count;
   printf("Enter the thread count : ");
   scanf("%d",&thread_count);
   int max_value=ar[0];
#pragma omp parallel for num_threads(thread_count) reduction(max:max_value)
   for(i=0;i<n;i++){
      if(ar[i]>max_value){
         max_value=ar[i];
      }
   }
   printf("\nMaximum element in the array is %d\n\n",max_value);
   return 0;
}