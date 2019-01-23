package oscar.web.converter;


import oscar.core.model.BaseEntity;
import oscar.web.dto.BaseDto;

interface ConverterBaseEntity<Model extends BaseEntity<Long>, Dto extends BaseDto>
        extends Converter<Model, Dto> {

}

