package oscar.web.dto;

import lombok.*;

import java.util.Set;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class BookDto extends BaseDto {
    private String title;
    private String author;
    private Integer year;

    @Override
    public String toString() {
        return "Book: Title -> " + this.title + " ; Author -> " + this.author + " ; Year -> " + this.year + " ; " + super.toString();
    }
}