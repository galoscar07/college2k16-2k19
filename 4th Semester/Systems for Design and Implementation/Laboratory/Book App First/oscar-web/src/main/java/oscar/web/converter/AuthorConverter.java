package oscar.web.converter;

import org.springframework.stereotype.Component;
import oscar.core.model.Author;
import oscar.core.model.BaseEntity;
import oscar.web.dto.AuthorDto;

import java.util.stream.Collectors;

@Component
public class AuthorConverter extends AbstractConverterBaseEntityConverter<Author, AuthorDto> {
    @Override
    public Author convertDtoToModel(AuthorDto authorDto) {
        Author a = new Author();
        a.setName(authorDto.getName());
        a.setId(authorDto.getId());
        return a;
    }

    @Override
    public AuthorDto convertModelToDto(Author author) {
        AuthorDto authorDto = AuthorDto.builder()
                .name(author.getName())
                .books(author.getBooks().stream().map(BaseEntity::getId).collect(Collectors.toSet()))
                .build();
        authorDto.setId(author.getId());
        return authorDto;
    }
}
