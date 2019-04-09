/* 
* File:     main.c
* Author: Me, sort of
*
* Created on Feb12, 2019, 9:36 PM
*/

//#include <types.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define children 8

int main(int argc, char** argv) {
	int pid; /* process ID */
	int num =0; /*This first part checks to see if your using hard-coded value or command-line value*/
	if(argc>1){
		//printf("arg: %s\n",*(argv+1));
		num=atoi(*(argv+1));
	}
	else{
		//printf("arg: %d\n",children);
		num=children;
	}
	
	//printf("parent pid: %d\n",getpid());
	for(int i=0; i<num; i++){
		pid = fork(); 
		//creates new child process
		if(pid==0){
			//child process
			printf("Hello, pid=%d\n", getpid());
			exit(0);
		}
		else if(pid < 0){
			//error thrown
			printf("error");
			//perror("error");
			exit(1);
		}
		else{
			//parent process
			wait(0);
			//printf("I am the parent process: pid=%d, child pid=%d\n", getpid(), pid);
		}
	}exit(0);
	//return 0;
}
