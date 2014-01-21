import java.util.*;
import java.lang.Math.*;
public class Euler3{
    //600 851 475 143
    public static long Sieve(long max){
        long lrgst=1;
        for(int i = 2; i*i <= max;i++){
            while(max%i == 0){
                max = max/i;
                lrgst = i;
            }
        }
        if(max > lrgst)
            return max;
        return lrgst;
    }

    public static void main(String [] args){

        long lrgstPrm = Sieve(600851475143L);
        System.out.println(lrgstPrm);
    }


}
