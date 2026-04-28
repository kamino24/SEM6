#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<mpi.h>

int main(){
        char str[100];
        char temp[100];
        int comm_sz;
        int my_rank;
        MPI_Status status;
        MPI_Init(NULL,NULL);
        MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);
        MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

        if(my_rank==1){
                sprintf(str,"Hello");
                MPI_Send(str,strlen(str)+1,MPI_CHAR,0,1,MPI_COMM_WORLD);
        }
        else if(my_rank==2){
                sprintf(str,"madam");
                MPI_Send(str,strlen(str)+1,MPI_CHAR,0,2,MPI_COMM_WORLD);
        }
        else if(my_rank==3){
                sprintf(str,"high");
                MPI_Send(str,strlen(str)+1,MPI_CHAR,0,1,MPI_COMM_WORLD);
        }
        else if(my_rank==4){
                sprintf(str,"system");
                MPI_Send(str,strlen(str)+1,MPI_CHAR,0,2,MPI_COMM_WORLD);
        }
        else{
                printf("\nMaster Process%d", my_rank);
                int i,j;
                for(i=1;i<comm_sz;i++){
                        MPI_Recv(str,100,MPI_CHAR,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
                        if(status.MPI_TAG==1){
                                for(j=0;str[j]!='\0';j++){
                                        str[j]=toupper(str[j]);
                                }
                                printf("\nResult : %s from process%d", str, status.MPI_SOURCE);
                        }
                        else if(status.MPI_TAG==2){
                                for(j=0;str[j]!='\0';j++){
                                        temp[j]=str[j];
                                }
                                if(strcmp(str,temp)==0){
                                        printf("\nResult :(%s) Palindrome from process%d",str, status.MPI_SOURCE);
                                }
                                else{
                                        printf("\nResult :(%s) Not Palindrome from process%d",str, status.MPI_SOURCE);
                                }
                        }
                }
                printf("\n\n");
        }
        MPI_Finalize();
}

