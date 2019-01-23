package ro.ubb.PracticalSample.web.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class PersonDto {
    private Long id;
    private String ssn;
    private String name;
}
