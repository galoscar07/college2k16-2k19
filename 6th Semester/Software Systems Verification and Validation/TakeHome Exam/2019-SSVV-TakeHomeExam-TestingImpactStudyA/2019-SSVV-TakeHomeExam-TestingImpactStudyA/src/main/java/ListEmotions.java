import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class ListEmotions {

    private List<Emotion> lstEmotions;

    public ListEmotions(List<Emotion> newLstEmotions){
        this.lstEmotions = newLstEmotions;
    }

    public int getNumberOfEmotions(){
        return lstEmotions.size();
    }

    // Task A_1
    // return the number of emotion of the given EmotionType et
    // Remark: No test cases are going to be created.
    public int howGivenManyEmotionTypeInListEmotions(EmotionType et){
        int nJE=0;

        for (Emotion emotion: this.lstEmotions) {
            if (emotion.getEmotionType() == et) {
                nJE++;
            }
        }

        return nJE;
    }

    // Task A_2
    // return the list of predominant emotions
    // Remark: Create a set of test cases to assess the correctness of your code.
    //         Create a class to test this method, several test cases are needed.
    //         One sample test case is provided in cladd Test_ListEmotions.
    public List<Emotion> predominantEmotion(){
        List<Emotion> lstEPredominant = new ArrayList<Emotion>();

        int maxNo = 0;
        List<EmotionType> maxNoEmotions = new ArrayList<EmotionType>();

        for (EmotionType emo : EmotionType.values()) {
            int howManyEmotionType = this.howGivenManyEmotionTypeInListEmotions(emo);
            if (howManyEmotionType > maxNo) {
                maxNoEmotions = new ArrayList<EmotionType>();
                maxNoEmotions.add(emo);
                maxNo = howManyEmotionType;
            } else {
                if (howManyEmotionType == maxNo) {
                    maxNoEmotions.add(emo);
                }
            }
        }

        for (EmotionType emo: maxNoEmotions) {
            for (Emotion emotion: this.lstEmotions) {
                if (emotion.getEmotionType() == emo) {
                    lstEPredominant.add(emotion);
                }
            }
        }

        return  lstEPredominant;
    }

    // Task A_3
    // Eliminate the emotions that are of given type EmotionType et
    // Remark: A set of test cases to assess the correctness of your code is provided.
    //         A class to test this method was created, several test cases were added.
    //         Use the test cases to check for your code.
    public void eliminateAllProvidedEmotion(EmotionType et){
        for(Iterator<Emotion> iterator = this.lstEmotions.iterator(); iterator.hasNext(); ) {
            if(iterator.next().getEmotionType() == et)
                iterator.remove();
        }
    }
}
