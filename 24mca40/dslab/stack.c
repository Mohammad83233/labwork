#include<stdio.h>
#include<stdlib.h>
void push();
void pop();
void display();

typedef struct node
{
	int data;
 	struct node *next;
}node;

struct node *start;
int main(){
int ch;
do
{
	printf("\n_________");
	printf("\n\tMENU");
 	printf("\n\t____");
 	printf("\n\t1.PUSH");
 	printf("\n\t2.POP");
 	printf("\n\t3.DISPLAY");
 	printf("\n\t4.EXIT");
 	printf("\n enter your option\n: ");
 	scanf("%d",&ch);

	switch(ch)
	{
 		case 1:push();
 		       break;

		case 2:pop();
                       break;

	        case 3:display();
 			break;

		case 4: printf("EXIT___");
   			break;
	}
}while(ch!=4);
}



void push()
{
	int val;
   	struct node*ptr=(struct node*)malloc(sizeof(struct node));
	 if(ptr==NULL)
          { 
 	     printf("OVERFLOW___");
                                    }
         else
	{
	      printf("enter value to push : ");
	      scanf("%d",&val);
        if(start==NULL)
	   {
	     ptr->data=val;
	     ptr->next=start;
	     start=ptr;
                         }
        else
           {
             ptr->data=val;
             ptr->next=start;
             start=ptr;
                          }
             printf("in item pushed to stack");
                             }}
void pop()
{ 
      int item;
      struct node*ptr;
       if(start==NULL)
     {
       printf("underflow__-");
       }
     else
     {
	 item=start->data;
	 ptr=start;
	 start=start->next;
	 free(ptr);
	 printf("\n%d popped",item);
        }
}
void display()
{
  int i;
  struct node*ptr;
  ptr=start;
  if(ptr==NULL)
     {
       printf(" stack is empty");
        }
  else
    {
      printf("\tstack\n\t*****\n");
      while(ptr!=NULL) 
      { 
         printf("\t| %d |\n",ptr->data);
         ptr=ptr->next;
                      }
}
}
