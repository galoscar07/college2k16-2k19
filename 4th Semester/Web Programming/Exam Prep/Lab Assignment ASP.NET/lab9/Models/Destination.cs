using System;
namespace lab9.Models
{
    public class Destination
    {
		public string City { get; set; }
		public string Country { get; set; }
		public int Id { get; set; }
        public string Description { get; set; }
        public int Tourist { get; set; }
        public int Cost { get; set; }

        public Destination() {}

        public Destination(string city, string country, string description, int tourist, int cost)
        {
            City = city;
            Country = country;
            Description = description;
            Tourist = tourist;
            Cost = cost;
        }

        public override string ToString()
        {
            return string.Format("'{0}', '{1}', '{2}', '{3}', '{4}'", City, Country, Description, Tourist, Cost);
        }
    }
}
