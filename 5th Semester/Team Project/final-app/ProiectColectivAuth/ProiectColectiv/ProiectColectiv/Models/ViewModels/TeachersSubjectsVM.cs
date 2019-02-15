using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.ViewModels
{
	public class TeachersSubjectsVM
	{

		public long TeacherId { get; set; }
		public Dictionary<long, String> SubjectName { get; set; }
        public Dictionary<long, String> AllSubjectName { get; set; }
    }
}