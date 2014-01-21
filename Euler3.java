import java.util.*;
import java.lang.Math.*;
public class Euler3{
    public static long Sieve(long max){
/*Start at 2, iterate up to sqrt(max) checking if each 
number divides max. If it divides max then redefine max 
as the result of that division. Repeat until you can no 
longer divide max. Max will not be the largest prime factor*/
        for(int i = 2; i*i <= max;i++){
            while(max%i == 0){
                max = max/i;
            }
        }
        return max;
    }

    public static void main(String [] args){

        long lrgstPrm = Sieve(600851475143L);
        System.out.println(lrgstPrm);
    }


}
