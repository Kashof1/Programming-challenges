public class FibonacciCache {
    public static int[] fib = new int[20];
    public static void main (String[] args){
        System.out.println(fib);
        int[] finalarray = store();
        System.out.println(finalarray);
    }

    public static int[] store(){
        if (fib.length>0){
            int current = 1;
            for (int i=0;i<(fib.length);i++){
                if (i>1) {
                    current = fib[i] + fib[(i-1)];
                }
                fib[i] = current;
            }
        }
        return fib;
    }


}
