using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models
{
    public class TeacherSubjectDTO
    {
       public long id { get; set; }

        public long TeacherID { get; set; }

        public long SubjectID { get; set; }

        public int GroupID { get; set; }

        public int SubGroup { get; set; }
    }
}