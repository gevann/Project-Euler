#include <stdio.h>
#include <stdlib.h>


void sieve ( int nums [10000] ){

    int count = 1;
    int curr_val=2;
    int i;
    while ( count < 10001 ){
        i = 0;
        curr_val++;
        while( curr_val % nums[i] != 0 ){
            if( nums[ i+1 ] == 0 ){
                nums[ i+1 ] = curr_val;
                count++;
            }
            i++;
        }
    }
	
	
	//end sieve()
}


int main ( int argc, const char * argv [] ){
	
	int primes_list [10001] = {2};
    sieve( primes_list );
    int k;
    printf("The 10001st prime is:  %d", primes_list[10000]);

	
	



	//end main()
}
