using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace ExamREST.Utilits
{
    public class JsonDateConverter : IsoDateTimeConverter
    {
        public JsonDateConverter()
        {
            base.DateTimeFormat = "yyyy-MM-dd";
        }
    }
}
