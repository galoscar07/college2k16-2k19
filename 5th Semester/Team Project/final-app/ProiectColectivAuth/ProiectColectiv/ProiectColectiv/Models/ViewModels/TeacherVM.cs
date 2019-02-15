using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.ViewModels
{
    public class TeacherVM
    {
		public int id;
        public long TeacherId { get; set; }
        public int WeekNumber { get; set; }
        public long SubjectId { get; set; }
		public string Type { get; set; }
        public List<StudentDTO> Students { get; set; }
        public List<AttendanceDTO> Attendances { get; set; }
    }
}