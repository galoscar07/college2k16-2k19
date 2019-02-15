using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using Microsoft.AspNet.Identity;
using Microsoft.AspNet.Identity.EntityFramework;
using Microsoft.AspNet.Identity.Owin;
using Microsoft.Owin.Security;
using Microsoft.Owin.Security.Cookies;
using Microsoft.Owin.Security.OAuth;
using ProiectColectiv.Models;

namespace ProiectColectiv.Providers
{
	using System.Security.Claims;
	using System.Threading.Tasks;
	using Microsoft.Owin.Security.OAuth;
	using ProiectColectiv.Models.Domain;

	namespace WebApiAngularTokenAuthExample
	{
		public class ApplicationOAuthProvider : OAuthAuthorizationServerProvider
		{
			public override async Task ValidateClientAuthentication(OAuthValidateClientAuthenticationContext context)
			{
				context.Validated();
			}

			public override async Task GrantResourceOwnerCredentials(OAuthGrantResourceOwnerCredentialsContext context)
			 {
				context.OwinContext.Response.Headers.Add("Access-Control-Allow-Origin", new[] { "*" });

				using (var ctx = new SchoolContext())
				{
					var usr = ctx.Credentials.Where(c => c.Email.Equals(context.UserName)).FirstOrDefault();
					if ((usr==null )|| context.Password != usr?.Password)
					{
						context.SetError("invalid_grant", "The user name or password is incorrect.");
						return;
					}

					var identity = new ClaimsIdentity(context.Options.AuthenticationType);
					identity.AddClaim(new Claim("username", context.UserName));
					identity.AddClaim(new Claim("role", usr.Role));
					long? id;
					if (usr.Role.Equals("Teacher"))
						id = ctx.Teachers.Where(t => t.Email.Equals(usr.Email)).FirstOrDefault()?.TeacherID;
					else
						id = ctx.Students.Where(t => t.Email.Equals(usr.Email)).FirstOrDefault()?.StudentID;
					if (id.HasValue)
						identity.AddClaim(new Claim("id",id.Value.ToString()));
					identity.AddClaim(new Claim(ClaimTypes.Role, usr.Role));

					context.Validated(identity);
				}

			}
		}
	}
}