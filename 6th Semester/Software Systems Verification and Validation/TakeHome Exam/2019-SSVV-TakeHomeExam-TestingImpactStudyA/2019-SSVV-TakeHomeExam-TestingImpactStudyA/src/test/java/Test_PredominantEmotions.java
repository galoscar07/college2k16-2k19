import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Test_PredominantEmotions {

    @Test
    public void Test_OnePredominantEmotion_predominantEmotion() {
        System.out.println("Test .... Test_OnePredominantEmotion_predominantEmotion ... ");
        Emotion emo1 = new Emotion("descr1", EmotionType.Fear);
        Emotion emo2 = new Emotion("descr2", EmotionType.Fear);
        Emotion emo3 = new Emotion("descr3", EmotionType.Joy);
        List<Emotion> listEmotions = new ArrayList<Emotion>();
        listEmotions.add(emo1);
        listEmotions.add(emo2);
        listEmotions.add(emo3);
        ListEmotions listEmo = new ListEmotions(listEmotions);

        List<Emotion> lstPE = listEmo.predominantEmotion();
        System.out.println("Number of Predominant Emotions=" + lstPE.size());
        assertEquals(lstPE.size(), 2);
    }

    @Test
    public void Test_MultiplePredominantEmotions_predominantEmotion() {
        System.out.println("Test .... Test_MultiplePredominantEmotions_predominantEmotion ... ");
        Emotion emo1 = new Emotion("descr1", EmotionType.Fear);
        Emotion emo2 = new Emotion("descr2", EmotionType.Fear);
        Emotion emo3 = new Emotion("descr3", EmotionType.Joy);
        Emotion emo4 = new Emotion("descr4", EmotionType.Joy);
        Emotion emo5 = new Emotion("descr5", EmotionType.Anger);
        List<Emotion> listEmotions = new ArrayList<Emotion>();
        listEmotions.add(emo1);
        listEmotions.add(emo2);
        listEmotions.add(emo3);
        listEmotions.add(emo4);
        listEmotions.add(emo5);
        ListEmotions listEmo = new ListEmotions(listEmotions);

        List<Emotion> lstPE = listEmo.predominantEmotion();
        System.out.println("Number of Predominant Emotions=" + lstPE.size());
        assertEquals(lstPE.size(), 4);
    }

    @Test
    public void Test_NoEmotion_predominantEmotion() {
        System.out.println("Test .... Test_NoEmotion_predominantEmotion ... ");
        List<Emotion> listEmotions = new ArrayList<Emotion>();
        ListEmotions listEmo = new ListEmotions(listEmotions);
        List<Emotion> lstPE = listEmo.predominantEmotion();
        System.out.println("Number of Predominant Emotions=" + lstPE.size());
        assertEquals(lstPE.size(), 0);
    }
}

