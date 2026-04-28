#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int A[100][100], B[100][100], sum[100][100], prod[100][100];
int r1, c1, r2, c2;

void *mat_add(void *arg){
        int i, j;
        for(i=0; i<r1; i++)
                for(j=0; j<c1; j++)
                        sum[i][j] = A[i][j] + B[i][j];
        /*printf("\nResult of matrix addition:\n");
        for(i=0; i<r1; i++){
                for(j=0; j<c1; j++)
                        printf("%d ", sum[i][j]);
                printf("\n");
        }*/
        pthread_exit(NULL);
}

void *mat_mul(void *arg){
        int i, j, k;
        for(i=0; i<r1; i++){
                for(j=0; j<c2; j++){
                        prod[i][j] = 0;
                        for(k=0; k<c1; k++){
                                prod[i][j] += A[i][k] * B[k][j];
                        }
                }
        }
        /*printf("\nResult of matrix multiplication:\n");
        for(i=0; i<r1; i++){
                for(j=0; j<c2; j++)
                        printf("%d ", prod[i][j]);
                printf("\n");
        }*/
        pthread_exit(NULL);
}

int main(){
        pthread_t t1, t2;
        printf("\nEnter r1, c1 - Matrix A : ");
        scanf("%d %d", &r1, &c1);
        printf("Enter r2, c2 - Matrix B : ");
        scanf("%d %d", &r2, &c2);

        /*A = malloc(r1*sizeof(int*));
        for(i=0; i<r1; i++)
                A[i] = malloc(c1*sizeof(int));

        B = malloc(r2*sizeof(int*));
        for(i=0; i<r2; i++)
                B[i] = malloc(c2*sizeof(int));

        sum = malloc(r1*sizeof(int*));
        for(i=0; i<r1; i++)
                sum[i] = malloc(c1*sizeof(int));

        prod = malloc(r1*sizeof(int*));
        for(i=0; i<r1; i++)
                prod[i] = malloc(c2*sizeof(int));*/

        if(r1!=r2 || c1!=c2 || c1!=r2)
                return 0;
        printf("\nEnter elements of Matrix A:\n");
        int i, j;
        for(i=0; i<r1; i++)
                for(j=0; j<c1; j++)
                        scanf("%d", &A[i][j]);
        printf("\nEnter elements of Matrix B:\n");
        for(i=0; i<r2; i++)
                for(j=0; j<c2; j++)
                        scanf("%d", &B[i][j]);
        pthread_create(&t1, NULL, mat_add, NULL);
        pthread_create(&t2, NULL, mat_mul, NULL);
        pthread_join(t1, NULL);
        pthread_join(t2, NULL);
        printf("\nResult of matrix addition:\n");
        for(i=0; i<r1; i++){
                for(j=0; j<c1; j++)
                        printf("%d ", sum[i][j]);
                printf("\n");
        }
        printf("\nResult of matrix multiplication:\n");
        for(i=0; i<r1; i++){
                for(j=0; j<c2; j++)
                        printf("%d ", prod[i][j]);
                printf("\n");
        }
        printf("\n");
}

