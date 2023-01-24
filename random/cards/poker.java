

public class poker {
    private static List<String> arr = new ArrayList<>();
    private static List <String> order = new ArrayList<>(Arrays.asList("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"));

    private static void FillDeck(){
        String [] types = {"H", "S", "D", "C"};
        String [] values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
        for(String type: types){
            for(String value: values){
                arr.add(value+type);
            }
        }
    }

    private static void Dealer(ArrayList<String>hand1, ArrayList<String> hand2){
        // give out five cards?
        // flip over 5 cards

    }

    // Straight Flush - same suit in sequence - highest: A, K, Q, J, and 10
    // Four of a Kind
    // Full HOuse - 3 of a kind with 2 of a kind
    // Flush - all same suit but no sequence
    // Straight - 
    private static int Compare(){

    }

    private static int Player(){

    }
    public static void main(String[]args){

    }
}
