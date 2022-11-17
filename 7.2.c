#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    char znak;
    printf("Podaj znak:");
    scanf("%c",&znak);
    printf("\n");
    printf("Lie razy go wyswietlic:");
    scanf("%d",&n);
    printf("\n");
    for(n;n>0;n--)
    {
    printf("%c",znak);
    }
    return 0;
}
