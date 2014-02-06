#include<stdlib.h>
#include<stdio.h>
#include<math.h>

/**PURPOSE
*		Finds all primes between 2 and 20
*		Finds highest power of each prime that is less that twenty
*		Stores power of prime in a[i], with i as the prime
*		Non-primes are to power 0.
* PRECONDITIONS
*		a[] is a legal C integer array with space to hold all the primes
*		between 2 and 20.
*/
void sieve( int a[] ){
	
	int i, j, k, v;
	j = 2;
	
	for( i = 2; i < 21; i++ ){
		a[i] = 1;
	}
	
	while( j < 20 ){
		i = j;
		k = 2;
		v = j;
		if ( a[i] == 1 ){
			
			while( i*k < 20 ){

				while( v*j < 20 ){
					a[i] += 1;
					v*=j;
				}
				a[i*k] = 0;
				k++;
			}
		}
		j++;
	}

}





int main(){

	int prime[20];
	int i;
	sieve( prime );
	int answer = 1;
	printf("\nFactors are:\n");
	for( int i = 2; i < 20; i++ ){
		if( prime [i] != 0 ){
			printf("(%d^%d) ", i, prime[i]);
			answer = answer*( pow(i, prime[i] ) );
		}
	}
	printf("\n\nAnswer is:  %d", answer);
	return EXIT_SUCCESS;
}
