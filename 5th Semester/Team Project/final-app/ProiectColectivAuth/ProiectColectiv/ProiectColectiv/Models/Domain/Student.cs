using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
    public class Student
    {
        [Key]
        public long StudentID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public long GroupID { get; set; }
        public int SubGroup { get; set; }
        public int Year { get; set; }
        public string Email { get; set; }

        [Timestamp]
        public Byte[] TimeStamp { get; set; }

        public virtual ICollection<Attendance> Attendances { get; set; }

    }
}