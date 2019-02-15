using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
    public class Teacher
    {
        [Key]
        public long TeacherID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Post { get; set; }
        public string Email { get; set; }

        public virtual ICollection<Attendance> Attendances { get; set; }
        public virtual ICollection<TeacherSubject> TeacherSubjects { get; set; }

        [Timestamp]
        public Byte[] TimeStamp { get; set; }

    }
}