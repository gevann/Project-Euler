# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>
# include <math.h>

int ReverseOrder( int n );
int isPalindrome( void );
int main( int argc, const char * argv[] ) {
    fprintf( stdout, "The biggest palindrome that is a product of two 3 digit numbers is %d\n", isPalindrome() );
    return EXIT_SUCCESS;
}

int isPalindrome( void ) {
    int i, j, candidate, biggest;
    biggest = 0;
    i = 999, j = 999;
    for( i = 999 ; i> 99 ; i -- ){
        for( j = 999 ; j > 99 ; j --){
            int candidate = i * j;
            if ( ( candidate == ReverseOrder( candidate ) ) && ( candidate > biggest  ))
                    biggest = candidate;
        }
    }    
    return biggest;
}

int ReverseOrder( int n ) {
    int reversed; 
    reversed = 0; 
    while ( n >= 10 ) {
        reversed = (reversed * 10) + (n%10);
        n = (n /10);
    }
    return ( reversed * 10 ) + n;   
}     
