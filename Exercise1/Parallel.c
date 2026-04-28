#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
   int *data, sid, sid2;
   double *max;
   int m, n, p;
   int size;
   printf("\nEnter value of m, n, p : ");
   scanf("%d %d %d", &m,&n,&p);
   size=(m*n)+(n*p)+(m*p);
   sid=shmget(3063,size*sizeof(int),IPC_CREAT|0777);
   sid2=shmget(3064,m*sizeof(double),IPC_CREAT|0777);
   data=(int*)shmat(sid,0,0);
   max=(double*)shmat(sid2,0,0);
   int i;
   for(i=0;i<m*n;i++)
      data[i]=rand()%5;
   for(i=0;i<n*p;i++)
      data[m*n+i]=rand()%5;
   int r,c,k;
   for(r=0;r<m;r++){
      int pid=fork();
      if(pid==0){
         clock_t start=clock();
         for(c=0;c<p;c++){
            int sum=0;
            for(k=0;k<n;k++){
               sum+=data[r*n+k]*data[m*n+k*p+c];
            }
            data[m*n+n*p+r*p+c]=sum;
         }
         clock_t end=clock();
         double time = ((double)(end-start)*1000.0/CLOCKS_PER_SEC);
         max[r]=time;
         exit(0);
      }
   }
   for(i=0;i<m;i++)
      wait(NULL);
   double max_t=max[0];
   for(i=1;i<m;i++){
      if(max_t<max[i])
         max_t=max[i];
   }
   printf("\nTime taken : %f milliseconds\n\n", max_t);
   shmdt(data);
   shmdt(max);
   shmctl(sid,IPC_RMID,0);
   shmctl(sid2,IPC_RMID,0);
}

