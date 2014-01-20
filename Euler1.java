public class Euler1{

	//Sums all of the multiples of a and b between 0 and max, inclusive.
	public static int sumMultiples( int a, int b){
		int sum = 0;
			for(int i = 0; i <1000; i++){
				if(i%a == 0)
					sum += i;
				if(i%b == 0)
					sum += i;
				if(i %(a*b) == 0){
					sum -= i;
				}
			}
		return sum;
	}
	
	public static void main(String [] args){
		
			int x = sumMultiples(3, 5);
			System.out.println(x);
	}

}
