using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
    public class TeacherSubject
    {


        [Key]
		public long id { get; set; }


        [ForeignKey("SubjectID")]
        public Subject Subject { get; set; }
        public long SubjectID { get; set; }


        [ForeignKey("TeacherID")]
        public Teacher Teacher { get; set; }
        public long TeacherID { get; set; }


        public long GroupID { get; set; }


        public int SubGroup { get; set; }

        [Timestamp]
        public Byte[] TimeStamp { get; set; }
    }
}