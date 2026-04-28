#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int request = 0;

pthread_mutex_t mutex;
pthread_cond_t cond;

int *seats;

void* user_thread(void* arg)
{
    while(1)
    {
        int tickets;

        pthread_mutex_lock(&mutex);

        if(*seats == 0)
        {
            pthread_mutex_unlock(&mutex);
            break;
        }

        pthread_mutex_unlock(&mutex);

        printf("Enter tickets to book: ");
        scanf("%d",&tickets);

        pthread_mutex_lock(&mutex);

        request = tickets;
        printf("User requested %d tickets\n",tickets);

        pthread_cond_signal(&cond);

        pthread_mutex_unlock(&mutex);

        sleep(1);
    }

    return NULL;
}

void* booking_thread(void* arg)
{
    while(1)
    {
        pthread_mutex_lock(&mutex);

        while(request == 0 && *seats > 0)
            pthread_cond_wait(&cond,&mutex);

        if(*seats == 0)
        {
            pthread_mutex_unlock(&mutex);
            break;
        }

        if(request <= *seats)
        {
            *seats -= request;
            printf("Booking confirmed for %d tickets\n\n",request);
        }
        else
        {
            printf("Booking failed. Only %d seats left\n\n",*seats);
        }

        request = 0;

        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}

void* display_thread(void* arg)
{
    while(1)
    {
        pthread_mutex_lock(&mutex);

        printf("Seats remaining: %d\n",*seats);

        if(*seats == 0)
        {
            pthread_mutex_unlock(&mutex);
            break;
        }

        pthread_mutex_unlock(&mutex);

        sleep(2);
    }

    return NULL;
}

int main()
{
    pthread_t user, booking, display;

    pthread_mutex_init(&mutex,NULL);
    pthread_cond_init(&cond,NULL);

    int shmid = shmget(IPC_PRIVATE, sizeof(int), 0666 | IPC_CREAT);

    seats = (int*) shmat(shmid, NULL, 0);

    *seats = 10;

    pthread_create(&display,NULL,display_thread,NULL);
    pthread_create(&booking,NULL,booking_thread,NULL);
    pthread_create(&user,NULL,user_thread,NULL);

    pthread_join(user,NULL);
    pthread_join(booking,NULL);
    pthread_join(display,NULL);

    printf("All seats booked. System closing.\n");

    shmdt(seats);
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}