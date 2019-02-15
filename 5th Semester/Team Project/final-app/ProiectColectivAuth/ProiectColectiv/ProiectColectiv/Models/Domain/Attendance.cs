using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
    public class Attendance
    {
		[Key]
		public long id { get; set; }

        [ForeignKey("StudentID")]
        public Student Student { get; set; }
        public long StudentID { get; set; }

        [ForeignKey("TeacherID")]
        public Teacher Teacher { get; set; }
        public long TeacherID { get; set; }

        [ForeignKey("SubjectID")]
        public Subject Subject { get; set; }
        public long SubjectID { get; set; }


        public int WeekNumber { get; set; }

        public string TypeOf { get; set; }


        public int? grade { get; set; }

        [Timestamp]
        public Byte[] TimeStamp { get; set; }
    }
}