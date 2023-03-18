import java.util.List;
import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class poker {
    private static List<String> arr = new ArrayList<>();
    private static List <String> types = new ArrayList<>(Arrays.asList("H", "S", "D", "C"));

    private static List <String> order = new ArrayList<>(Arrays.asList("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"));

    private static void FillDeck(){
        arr = new ArrayList<>();
        for(String type: types){
            for(String value: order){
                arr.add(value+type);
            }
        }
    }

    private static void Dealer(List<String>hand1, List<String> hand2){
        Random rand = new Random();
        // give out five cards?
        for(int i = 0; i<5; i++){
            int index1 = rand.nextInt(arr.size());
            hand1.add(arr.get(index1));
            arr.remove(index1);
            int index2 = rand.nextInt(arr.size());
            hand2.add(arr.get(index2));
            arr.remove(index2);
        }

    }

    // 22 Straight Flush - same suit in sequence - highest: A, K, Q, J, and 10
    // 20 Four of a Kind
    // 11 Full HOuse - 3 of a kind with 2 of a kind
    // 10 Flush - all same suit but no sequence
    // 01 Straight - 
    private static int Compare(List<String>hand1, List<String>hand2){

        int highest1 = 0;
        int highest2 = 0;

        boolean flush1 = false;
        boolean flush2 = false;

        boolean straight1 = false;
        boolean straight2 = false;

        int prev1 = 0;
        int prev2 = 0;
        int count1 = 0;
        int count2 = 0;

        // hands unsorted
        // put values into array? then sort then check?
        int [] pairing1 = new int [13];
        int[] colors1 = new int[4];
        int [] pairing2 = new int[13];
        int[] colors2 = new int[4];
        int number1 ;
        int number2 ;
        int color1 ;
        int color2 ;

        for(int i =0; i<5; i++){
            number1 = order.indexOf(hand1.get(i).substring(0, hand1.size()-2));
            number2 = order.indexOf(hand2.get(i).substring(0, hand2.size()-2));
            color1 = types.indexOf(hand1.get(i).substring(hand1.size()-2));
            color2 = types.indexOf(hand1.get(i).substring(hand2.size()-2));

            pairing1[number1] ++;
            pairing2[number2] ++;
            colors1[color1] ++;
            colors2[color2] ++;
                        
        }

        // Add up values
        // check pairs, highest, and straight
        for(int i = 0; i<13; i++){
            // check colors
            if(i <4){
                if(colors1[i] == 5){
                    flush1 = true;
                }
                if(colors2[i] == 5){
                    flush2 = true;
                }

            }
            // check for straight
            if(pairing1[i]>0 )
                // four pair
                if(pairing1[i] == 4){

                }
                // number of pairs found? then compare values?? 
                if(prev1 == (i-1)|| prev1 == 0)
                    count1++;
                    prev1 = i;
                highest1 = i;
            if(pairing2[i] >0)
                highest2 = i;
                if(prev2 == (i-1)|| prev1 == 0)
                    count2++;
                    prev2 = i;
        }
        if(count1 == 5){
            straight1=true;
        }
        if(count2 == 5){
            straight2=true;
        }
        // create scores
        String score1 ="";
        if(straight1 && flush1){
            score1+="11";
        }
        else if(flush1){
            score1+="10";
        }
        else if(straight1){
            score1+="01";
        }
        else{
            score1+="00";

        }

        // compare scores

        return 1;
    }

    private static int Play(){
        int count1 = 100;
        int count2 = 100;

        List<String>hand1 = new ArrayList<>();
        List<String>hand2 = new ArrayList<>();
        while(count1 >0 && count2 >0){
            FillDeck();
            hand1 = new ArrayList<>();
            hand2 = new ArrayList<>();
            Dealer(hand1,hand1);

            Compare(hand1, hand2);
        }
        if(count1>0){
            return 1;
        }
        else{
            return 2;
        }
    }
    public static void main(String[]args){
        System.out.println("Player: "+Play()+" WINS!!!");
    }
}
