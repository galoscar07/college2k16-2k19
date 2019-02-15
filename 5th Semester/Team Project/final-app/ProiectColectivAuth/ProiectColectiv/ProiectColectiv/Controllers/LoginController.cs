using ProiectColectiv.Models;
using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Security.Claims;
using System.Web;
using System.Web.Http;
using System.Web.Http.Description;

namespace ProiectColectiv.Controllers
{
	[RoutePrefix("login")]
	public class LoginController : ApiController
    {

		[HttpGet, Route("")]
		[Authorize]
		[ResponseType(typeof(CredentialsDTO))]
		public IHttpActionResult GetRole()
		{
			var identity = HttpContext.Current.User.Identity as ClaimsIdentity;
			if (identity != null)
			{
				CredentialsDTO c = new CredentialsDTO();
				c.Id = long.Parse(identity.FindFirst("id").Value);
				c.Role = identity.FindFirst("role").Value;
				c.username = identity.FindFirst("username").Value;
				return Ok(c);
			}
			return BadRequest();
		}

        [HttpPost, Route("")]
        [ResponseType(typeof(Credential))]
        public IHttpActionResult Post(Credential c)
        {
            using (var ctx = new SchoolContext())
            {
                if (c.Role.Equals("Teacher"))
                    if (!ctx.Teachers.Any(s => s.Email.Equals(c.Email)))
                        return BadRequest("Invalid email");
                if (c.Role.Equals("Student"))
                    if (!ctx.Students.Any(s => s.Email.Equals(c.Email)))
                        return BadRequest("Invalid email");
                ctx.Credentials.Add(c);
                ctx.SaveChanges();
                return Ok(c);

            }
            return BadRequest();
        }
    }
}
