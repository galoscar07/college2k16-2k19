using AutoMapper;
using ProiectColectiv.Models;
using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Mail;
using System.Web.Http;
using System.Web.Http.Description;

namespace ProiectColectiv.Controllers
{
    [RoutePrefix("api/attendance")]
    public class AttendanceController : ApiController
    {
        private string Email= "ubbcluj.info@gmail.com";
        private string Pwd = "Password_2018";

        [HttpGet, Route("")]
		[ResponseType(typeof(IList<AttendanceDTO>))]
        public IHttpActionResult Get()
        {
            using (var ctx = new SchoolContext())
            {
                return Ok(Mapper.Map<List<Attendance>, List<AttendanceDTO>>(ctx.Attendances.ToList()));
            }
        }

        /// <summary>
        /// Gets a Address with the given id
        /// </summary>
        /// <param name="id">The id of the address</param>
        /// <returns>Status code: 200 (Ok) and an Address - if the action executed successfully
        ///          Status code : 404 (Not Found) - if the address was NOT found</returns>
        [HttpGet, Route("{studentId}/{subjectId}/{weekNumber}/{type}")]
        [ResponseType(typeof(AttendanceDTO))]
		public IHttpActionResult Get(int studentId, int subjectId, int weekNumber, string type)
        {

            using (var ctx = new SchoolContext())
            {
                Attendance attendance = ctx.Attendances.Where(st => st.StudentID == studentId && st.SubjectID == subjectId && st.WeekNumber == weekNumber && st.TypeOf.Equals(type)).FirstOrDefault();
                if (attendance == null)
                    return NotFound();
                return Ok(Mapper.Map<Attendance, AttendanceDTO>(attendance));
            }
        }

        /// <summary>
        /// Adds an address.
        /// </summary>
        /// <param name="addressDTO">The address you want to add</param>
        /// <returns>   Status code : 200 (Ok) - if the user was added successfully
        ///             Status code: 400  (Bad Request)- Malformed syntax </returns>
        [HttpPost, Route("")]
        [ResponseType(typeof(void))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult Post(AttendanceDTO attendance)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    ctx.Attendances.Add(Mapper.Map<AttendanceDTO, Attendance>(attendance));
                    ctx.SaveChanges();
                    var student = ctx.Students.Where(s => s.StudentID == attendance.StudentID).FirstOrDefault();
					var subj = ctx.Subjects.Where(s => s.SubjectID == attendance.SubjectID).FirstOrDefault();
                    if (student != null && subj != null)
                        this.SendEmail(student.Email, "You received the grade " + attendance.grade +" on week #" + attendance.WeekNumber + " at " + attendance.TypeOf + " at " + subj.Title );
                }
                catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok(attendance);
            }


        }

        /// <summary>
        /// Updates the address with the given id with the given values
        /// </summary>
        /// <param name="id"> The id of the Address you want to update</param>
        /// <param name="addressDTO">The updated Address</param>
        /// <returns>Status code : 200 (Ok) - if the user was updated successfully
        ///         Status code: 400 (Bad Request) - Malformed syntax 
        ///         Status code: 404 (Not Found) - No user found with the given Id
        ///</returns>

        [HttpDelete, Route("{studentId}/{subjectId}/{weekNumber}/{type}")]
        [ResponseType(typeof(void))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult Delete(int studentId, int subjectId, int weekNumber, string type)
        {
            using (var ctx = new SchoolContext())
            {
                Attendance attendance = ctx.Attendances.Where(st => st.StudentID == studentId && st.SubjectID == subjectId && st.WeekNumber == weekNumber && st.TypeOf.Equals(type)).FirstOrDefault();
                if (attendance != null)
                    try
                    {
                        ctx.Attendances.Remove(attendance);
                        ctx.SaveChanges();
                    }
                    catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok();
            }
        }

        public void SendEmail(String EmailTo,String message)
        {
            try
            {
                MailMessage msg = new MailMessage(this.Email, EmailTo, "You've been graded", message);
                msg.IsBodyHtml = true;
                SmtpClient sc = new SmtpClient("smtp.gmail.com", 587);
                sc.UseDefaultCredentials = false;
                NetworkCredential cre = new NetworkCredential(this.Email, this.Pwd);//your mail password
                sc.Credentials = cre;
                sc.EnableSsl = true;
                sc.Send(msg);
            }
            catch(Exception _)
            {
            }
        }
    }
}
