#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define DIFFERENCE
#define SUMSQR
#define SQRSUM

/**
PURPOSE
    Find the sum of every number [1, 100] squared.
    Then find the sum over ever number [1, 100] and squared it.
    Then subtract the smaller from the larger and return.
*/



/**
PURPOSE
    Uses the closed form expression for the sum of i^2.
PRECONDITIONS
    i is greater than 0 and n is greater than i.
*/
int sum_i_squared ( int n ){
   return ( n * (n+1) * ((2*n)+1)) /( 6);  
}

int squared_sum_to_i ( int n ) {
    int sum = ((n)*(n+1))/2;
    return sum*sum;

}

int main ( int argc, const char *argv[] ){

    int i_squared = sum_i_squared( 100 );

    printf("Sum of squared: %d", i_squared);
    
    int sum_squared= squared_sum_to_i( 100 );

    printf("\nSum of squared: %d", sum_squared);

    int answer = sum_squared - i_squared;

    printf("\nAnswer: %d", answer);

//end main()
}
