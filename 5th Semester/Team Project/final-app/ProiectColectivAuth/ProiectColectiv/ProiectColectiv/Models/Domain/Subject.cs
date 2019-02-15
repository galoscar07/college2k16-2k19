using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
    public class Subject
    {
        [Key]
        public long SubjectID { get; set; }

        public string Title { get; set; }

        [Timestamp]
        public Byte[] TimeStamp { get; set; }

        public virtual ICollection<Attendance> Attendances { get; set; }
        public virtual ICollection<TeacherSubject> TeacherSubjects { get; set; }


    }
}