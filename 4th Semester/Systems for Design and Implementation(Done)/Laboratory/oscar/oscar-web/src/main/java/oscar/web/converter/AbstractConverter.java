package oscar.web.converter;

import java.util.Collection;
import java.util.Set;
import java.util.stream.Collectors;

public abstract class AbstractConverter<Model, Dto>
        implements Converter<Model, Dto> {

    public Set<Dto> convertModelsToDtos(Collection<Model> models) {
        return models.stream()
                .map(this::convertModelToDto)
                .collect(Collectors.toSet());
    }

    public Set<Model> convertDtosToModel(Collection<Dto> dtos) {
        return dtos.stream()
                .map(this::convertDtoToModel)
                .collect(Collectors.toSet());
    }
}
