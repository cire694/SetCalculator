import Attributes.*;
public class Card {

    private Num num; 
    private Color color;
    private Shading shading; 
    private Shape shape;

    public Card(Num num, Color color, Shading shading, Shape shape){
        if(num.ordinal() > 2 || num.ordinal() < 0){
            throw new IllegalStateException("Invalid Number");
        } 

        
        this.num = num;
        this.color = color;
        this.shading = shading;
        this.shape = shape;
    }
    
    public Num getNumber(){
        return num;
    }
    public Color getColor(){
        return color;
    }
    public Shading getShading(){
        return shading;
    }
    public Shape getShape(){
        return shape;
    }

    public String toString(){
        return num + " " + color + " " + shading + " "+  shape;
    }
}
