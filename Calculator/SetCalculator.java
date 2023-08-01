package Calculator;
import java.util.ArrayList;

import Calculator.Attributes.Color;
import Calculator.Attributes.Num;
import Calculator.Attributes.Shading;
import Calculator.Attributes.Shape;

public class SetCalculator {
    private Card[] cards;
    private ArrayList<Card[]> sets;
    public SetCalculator(Card ... cards){
        this.cards = cards;
        if(cards.length < 3 || cards.length % 3 != 0){
            throw new IllegalArgumentException("Invalid Card Amount");
        }
        sets = new ArrayList<>();
        findAllSets();
    }

    public int getSize(){
        return cards.length;
    }
    
    private static boolean checkNum(Card a, Card b, Card c){
        if(a.getNumber().ordinal() != b.getNumber().ordinal() &&
           b.getNumber().ordinal() != c.getNumber().ordinal() &&
           c.getNumber().ordinal() != a.getNumber().ordinal() ){
            return true;
        }
        if(a.getNumber().ordinal() == b.getNumber().ordinal() && b.getNumber().ordinal() == c.getNumber().ordinal()){
            return true;
        }
        return false;
    }

    private static boolean checkColor(Card a, Card b, Card c){
        if(a.getColor().ordinal() != b.getColor().ordinal() &&
           b.getColor().ordinal() != c.getColor().ordinal() &&
           c.getColor().ordinal() != a.getColor().ordinal() ){
            return true;
        }
        if(a.getColor().ordinal() == b.getColor().ordinal() && b.getColor().ordinal() == c.getColor().ordinal()){
            return true;
        }
        return false;
        
    }
     
    private static boolean checkShape(Card a, Card b, Card c){
        if(a.getShape().ordinal() != b.getShape().ordinal() &&
           b.getShape().ordinal() != c.getShape().ordinal() &&
           c.getShape().ordinal() != a.getShape().ordinal() ){
            return true;
        }
        if(a.getShape().ordinal() == b.getShape().ordinal() && b.getShape().ordinal() == c.getShape().ordinal()){
            return true;
        }
        return false;
    }
    
    private static boolean checkShading(Card a, Card b, Card c){
        if(a.getShading().ordinal() != b.getShading().ordinal() &&
           b.getShading().ordinal() != c.getShading().ordinal() &&
           c.getShading().ordinal() != a.getShading().ordinal() ){
            return true;
        }
        if(a.getShading().ordinal() == b.getShading().ordinal() && b.getShading().ordinal() == c.getShading().ordinal()){
            return true;
        }
        return false;
    }

    private static boolean isSet(Card a, Card b, Card c){
        return checkColor(a, b, c) && checkNum(a, b, c) && checkShading(a, b, c) && checkShape(a, b, c);
    }
    
    

    public void findAllSets(){
        
        for(int i = 0; i < cards.length - 2; i++){
            Card firstCard = cards[i];
            
            for(int j = i + 1; j < cards.length - 1; j++){
                Card secondCard = cards[j];
                
                for(int k = j + 1; k < cards.length; k++){
                    Card thirdCard = cards[k];
                    if(isSet(firstCard, secondCard, thirdCard)){
                        sets.add(new Card[] { firstCard, secondCard, thirdCard});
                    }
                }
            }
        }
    }

    public String toString(){
        StringBuilder result = new StringBuilder("Sets:\n");

        for (Card[] set : sets) {
            result.append("[ ");
            for (Card card : set) {
                result.append(card).append(", ");
            }
            result.delete(result.length() - 2, result.length()); // Remove the trailing ", "
            result.append(" ]\n");
        }

        return result.toString();
    }
    
    public static void main(String[] args){
        Card[] cards = new Card[] {
            new Card(Num.TWO, Color.PURPLE, Shading.SOLID, Shape.OVAL),
            new Card(Num.ONE, Color.RED, Shading.STRIPE, Shape.OVAL),
            new Card(Num.THREE,Color.RED, Shading.STRIPE, Shape.SQUIGGLE),
            
            new Card(Num.ONE, Color.PURPLE, Shading.SOLID, Shape.DIAMOND),
            new Card(Num.THREE, Color.PURPLE, Shading.EMPTY, Shape.DIAMOND),
            new Card(Num.TWO, Color.GREEN, Shading.STRIPE, Shape.DIAMOND),
            
            new Card(Num.ONE, Color.GREEN, Shading.STRIPE, Shape.DIAMOND),
            new Card(Num.ONE, Color.GREEN, Shading.SOLID, Shape.DIAMOND),
            new Card(Num.TWO, Color.GREEN, Shading.SOLID, Shape.DIAMOND),

            new Card(Num.THREE, Color.RED, Shading.SOLID, Shape.DIAMOND),
            new Card(Num.ONE, Color.GREEN, Shading.STRIPE, Shape.OVAL),
            new Card(Num.ONE, Color.GREEN, Shading.EMPTY, Shape.OVAL),

        };

        SetCalculator calculator = new SetCalculator(cards);
        System.out.println(calculator);

    }


}
