#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MAX 1000

int arr[MAX];
int n,i, thread_count;
long  global_sum = 0;
long thread;

void *partial_sum(void *rank)
{
    long my_rank = (long) rank;

    int local_n = n / thread_count;
    int first = my_rank * local_n;
    int last = first + local_n - 1;
    if(my_rank == thread_count-1)
       last = n-1;
    long local_sum = 0;
    printf("Thread %ld: Index= %d - %d ",my_rank,first,last);
    for(i = first; i <= last; i++)
    {
        local_sum += arr[i];
    }
    printf("Local sum : %d\n", local_sum);
    global_sum += local_sum;
    pthread_exit(NULL);
}

int main()
{
    pthread_t *thread_handles;
    printf("\nEnter number of elements: ");
    scanf("%d", &n);
    printf("Random generated elements:\n");
    srand(time(NULL));
    for(i = 0; i < n; i++){
        arr[i] = rand()%10;
        printf("%d ", arr[i]);
    }
    printf("\nEnter number of threads: ");
    scanf("%d", &thread_count);
    printf("\n");
    thread_handles = malloc(thread_count * sizeof(pthread_t));
    for(thread = 0; thread < thread_count; thread++)
    {
        pthread_create(&thread_handles[thread],NULL,partial_sum, (void*) thread);
    }

    for(thread = 0; thread < thread_count; thread++)
    {
        pthread_join(thread_handles[thread], NULL);
    }
    printf("\nTotal Sum = %ld\n\n", global_sum);
    free(thread_handles);

    return 0;
}
