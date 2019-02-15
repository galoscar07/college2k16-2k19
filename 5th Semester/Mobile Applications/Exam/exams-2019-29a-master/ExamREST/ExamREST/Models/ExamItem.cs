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

		public string Notes { get; set; }

		public bool Done { get; set; }

        [JsonConverter(typeof(JsonDateConverter))]
        public DateTime Date { get; set; }

    }
}
