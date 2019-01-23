package oscar.web.dto;

import lombok.*;

import java.util.Set;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class AuthorDto extends BaseDto {
    private String name;
    private Set<Long> books;

    @Override
    public String toString() {
        return "Author: Name -> " + this.name + " ; " + super.toString();
    }
}
