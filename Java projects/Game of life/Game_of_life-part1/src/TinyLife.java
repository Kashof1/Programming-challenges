public class TinyLife {
    public static void main (String[] args) throws Exception{
        getCell(0x20A0600000000000L)
    }

    public static boolean getCell(long world, int col, int row) {
        boolean truthstate = ((7>=col) & (0<=col) & (7>=row) & (0<=row));
        return truthstate;
    }

    public static void print(long world){
        System.out.println("-");
        for (int row=0; row<8; row++){
            for (int col=0; col<8; col++){
                System.out.print(getCell(world,col,row)?"#":"_");
            }
            System.out.println();
        }
    }

}
