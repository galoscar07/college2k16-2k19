using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models
{
    public class StudentDTO
    {
        public long StudentID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public long GroupID { get; set; }
        public int SubGroup { get; set; }
        public int Year { get; set; }
        public string Email { get; set; }
    }
}