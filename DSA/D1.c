//STARTING WITH DSA BASICS :-
// PATTERNS :-

/* Patter 1:-
1234
1234
1234 */
#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            printf("%d",j);
        }
        printf("\n");
    }
    return 0;
} 


/* Patter 1:-
****
****
****
****  

#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}    */


/* Patter 3:-
ABCD
ABCD
ABCD
ABCD

#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        char c = 'A';
        for(int j=0;j<n;j++){
            printf("%c",c);
            c=c+1;
        }
        printf("\n");
    }
    return 0;
}    */



/* Patter 4:-
123
456
789

#include <stdio.h>
int main() {
    int n;
    int num=1;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d",num);
            num++;
        }
        printf("\n");
    }
    return 0;
}    */


/* Patter 4:-
*
**
***
****

#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<i+1;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}    */


/* Patter 4:-
1
22
333
4444

#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<i+1;j++){
            printf("%d",i+1);
        }
        printf("\n");
    }
    return 0;
}    */


/* Patter 4:-
1
12
123
1234

#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            printf("%d",j);
        }
        printf("\n");
    }
    return 0;
}    */


/* Patter 4:-
1
21
321
4321

#include <stdio.h>
int main() {
    int n;
    printf("Enter the range: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=i+1;j>0;j--){
            printf("%d",j);
        }
        printf("\n");
    }
    return 0;
}    */



