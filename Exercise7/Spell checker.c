#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 50
#define WORD_LEN 20

char *dictionary[] = {
    "apple","banana","cat","dog","computer",
    "science","book","program","server","thread"
};

int dict_size = 10;

char work_buffer[BUFFER_SIZE][WORD_LEN];
int work_count = 0;

char result_buffer[BUFFER_SIZE][50];
int result_count = 0;

pthread_mutex_t mutex;
pthread_cond_t cond;

int total_words;

int check_dictionary(char word[])
{
   int i;
    for(i=0;i<dict_size;i++)
    {
        if(strcmp(word,dictionary[i])==0)
            return 1;
    }
    return 0;
}

void* spell_check(void* arg)
{
    while(1)
    {
        pthread_mutex_lock(&mutex);

        while(work_count == 0)
            pthread_cond_wait(&cond,&mutex);

        char word[WORD_LEN];
        strcpy(word,work_buffer[--work_count]);

        printf("Thread %lu picked: %s\n",pthread_self(),word);

        pthread_mutex_unlock(&mutex);

        int correct = check_dictionary(word);

        pthread_mutex_lock(&mutex);

        if(correct)
            sprintf(result_buffer[result_count++],"%s : Correct",word);
        else
            sprintf(result_buffer[result_count++],"%s : Incorrect",word);

        pthread_mutex_unlock(&mutex);
    }
}

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Usage: %s <number_of_threads>\n",argv[0]);
        return 1;
    }

    int THREADS = atoi(argv[1]);
    int i;

    printf("Dictionary Words:\n");
    for(i=0;i<dict_size;i++)
        printf("%s ",dictionary[i]);
    printf("\n\n");

    printf("Enter number of words to check: ");
    scanf("%d",&total_words);

    char input_words[BUFFER_SIZE][WORD_LEN];

    for(i=0;i<total_words;i++)
    {
        printf("Enter word %d: ",i+1);
        scanf("%s",input_words[i]);
    }

    pthread_t threads[THREADS];

    pthread_mutex_init(&mutex,NULL);
    pthread_cond_init(&cond,NULL);

    for(i=0;i<THREADS;i++)
        pthread_create(&threads[i],NULL,spell_check,NULL);

    for(i=0;i<total_words;i++)
    {
        pthread_mutex_lock(&mutex);

        strcpy(work_buffer[work_count++],input_words[i]);
        printf("Server added: %s\n",input_words[i]);

        pthread_cond_signal(&cond);

        pthread_mutex_unlock(&mutex);

        sleep(1);
    }

    sleep(2);

    printf("\nSpell Check Results:\n");
    for(i=0;i<result_count;i++)
        printf("%s\n",result_buffer[i]);

    return 0;
}
