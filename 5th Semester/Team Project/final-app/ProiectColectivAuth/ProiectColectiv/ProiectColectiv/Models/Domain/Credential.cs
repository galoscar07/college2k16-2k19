using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace ProiectColectiv.Models.Domain
{
	public class Credential
	{
		[Key]
		public string Email { get; set; }
		public string Password { get; set; }
		public string Role { get; set; }
		
	}
}