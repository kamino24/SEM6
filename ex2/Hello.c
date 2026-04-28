#include<stdio.h>
#include<string.h>
#include<mpi.h>

int main(){
        char msg[100];
        int comm_sz;
        int my_rank;
        MPI_Init(NULL,NULL);
        MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);
        MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

        if(my_rank!=0){
                sprintf(msg,"Hello from process%d\n",my_rank);
                MPI_Send(msg,strlen(msg)+1,MPI_CHAR,0,0,MPI_COMM_WORLD);
        }
        else{
                printf("\nHello from process%d\n",my_rank);
                int i;
                for(i=1;i<comm_sz;i++){
                        MPI_Recv(msg,100,MPI_CHAR,i,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
                        printf("%s", msg);
                }
                printf("\n");
        }
        MPI_Finalize();
}
