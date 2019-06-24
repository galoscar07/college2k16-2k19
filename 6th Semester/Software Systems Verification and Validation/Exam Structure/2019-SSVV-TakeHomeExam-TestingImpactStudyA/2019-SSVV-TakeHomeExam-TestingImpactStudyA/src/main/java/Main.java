import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args){
        System.out.println("Hello World");
        Emotion emo1 = new Emotion("descr1", EmotionType.Fear);
        Emotion emo2 = new Emotion("descr2", EmotionType.Fear);
        List<Emotion> listEmotions = new ArrayList<Emotion>();
        listEmotions.add(emo1);
        listEmotions.add(emo2);
        ListEmotions listEmo = new ListEmotions(listEmotions);
        if (listEmo.howGivenManyEmotionTypeInListEmotions(EmotionType.Fear) == 2) {
            System.out.println("KK");
        } else {
            System.out.println("Not KK");
        }

        if (listEmo.howGivenManyEmotionTypeInListEmotions(EmotionType.Joy) == 0) {
            System.out.println("KK");
        } else {
            System.out.println("Not KK");
        }

    }
}
