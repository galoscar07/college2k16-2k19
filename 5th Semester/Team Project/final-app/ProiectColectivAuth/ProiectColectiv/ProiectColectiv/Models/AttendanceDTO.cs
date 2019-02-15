using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models
{
    public class AttendanceDTO
    {
		public long id { get; set; }

		public long StudentID { get; set; }

   
        public long TeacherID { get; set; }

        public long SubjectID { get; set; }

        public int WeekNumber { get; set; }

        public string TypeOf { get; set; }

        public int? grade { get; set; }
    }
}