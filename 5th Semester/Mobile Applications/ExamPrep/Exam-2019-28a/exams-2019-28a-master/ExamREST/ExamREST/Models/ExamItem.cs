using System;
using ExamREST.Utilits;
using Newtonsoft.Json;
using SQLite;

namespace ExamREST
{
	public class ExamItem
	{
        [PrimaryKey]
        [JsonProperty(PropertyName = Constants.Json.IdName, NullValueHandling = NullValueHandling.Ignore)]
        public int Id { get; set; }

        [MaxLength(255)]
        public string Name { get; set; }

        [MaxLength(255)]
        public string Type { get; set; }

        [MaxLength(255)]
        public string Status { get; set; }

        public int Power { get; set; }

        [JsonConverter(typeof(JsonDateConverter))]
        public DateTime Date { get; set; }

    }
}
