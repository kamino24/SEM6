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
   int count,target,thread_count;
   printf("Enter the target : ");
   scanf("%d",&target);
   count=0;
   printf("Enter the thread count : ");
   scanf("%d",&thread_count);
#pragma omp parallel for num_threads(thread_count) reduction(+:count)
   for(i=0;i<n;i++){
      if(ar[i]<target){
         count++;
      }
   }
   printf("\nNo of elements less than the target %d : %d\n\n",target,count);
   return 0;
}