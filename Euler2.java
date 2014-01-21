public class Euler2{
    
    public static long Fib(int max){
        long prev, curr, next, sum;
        sum = 2;
        prev = 1;
        curr = 2;
        while(curr <= 4000000){
            next = prev + curr;
            prev = curr;
            curr = next;
            if((curr%2) == 0){
                sum += curr;
            }
        }
        return sum;
    }




    public static void main(String [] args){
        long x = Fib(10);
        System.out.println(x);
    }




}
