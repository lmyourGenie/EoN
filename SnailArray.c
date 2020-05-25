#include <stdio.h>
int array[10][10]={0,};
int num=0,x=-1,y=0;

void SnailArray(int n, int direct)
{
 
   int i;
      if(n==0) return;

      for(i=0; i<2*n-1; i++)
   {
     if(i < n) x += direct;
     else y += direct;
     array[y][x] = ++num;
   }
     SnailArray(n-1, direct * (-1));
}

int main(void)
{
 
      int i,j,n;
      printf("n : ");
      scanf("%d", &n);
 
      SnailArray(n, 1);

      for(i=0;i <n;i++)    {
           for(j=0;j <n;j++)         {
                printf("%4d",array[i][j]);
          }
          printf("\n");
      }

   return 0;
}