using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.ViewModels
{
	public class AttendancesVM
	{
		public List<AttendanceDTO> Attendances { get; set; }

		public Dictionary<long, String> TeacherInfo { get; set; }

		public Dictionary<long,String> SubjectName { get; set; }
	}
}