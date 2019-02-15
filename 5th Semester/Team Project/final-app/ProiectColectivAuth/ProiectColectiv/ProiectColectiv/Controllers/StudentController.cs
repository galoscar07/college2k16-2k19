using AutoMapper;
using ProiectColectiv.Models;
using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Description;

namespace ProiectColectiv.Controllers
{
    [RoutePrefix("api/student")]
    public class StudentController : ApiController
    {

        [HttpGet, Route("")]
		[ResponseType(typeof(IList<StudentDTO>))]
        public IHttpActionResult Get()
        {
            using (var ctx = new SchoolContext())
            {
                return Ok(Mapper.Map<List<Student>,List<StudentDTO>>(ctx.Students.ToList()));
            }
        }



        /// <summary>
        /// Gets a Address with the given id
        /// </summary>
        /// <param name="id">The id of the address</param>
        /// <returns>Status code: 200 (Ok) and an Address - if the action executed successfully
        ///          Status code : 404 (Not Found) - if the address was NOT found</returns>
        [HttpGet, Route("{id}")]
        [ResponseType(typeof(StudentDTO))]
		public IHttpActionResult Get(long id)
        {

            using (var ctx = new SchoolContext())
            {
                Student student = ctx.Students.Where(st => st.StudentID == id).FirstOrDefault();
                if (student == null)
                    return NotFound();
                return Ok(Mapper.Map<Student,StudentDTO>(student));
            }
        }

        [HttpGet, Route("{id}/attendance")]
        [ResponseType(typeof(AttendanceDTO))]
		public IHttpActionResult GetAttendance(long id)
        {

            using (var ctx = new SchoolContext())
            {
                Student student = ctx.Students.Include("Attendances").Where(st => st.StudentID == id).FirstOrDefault();
                if (student == null)
                    return NotFound();
                var att = student.Attendances.ToList();
                return Ok(Mapper.Map<List<Attendance>, List<AttendanceDTO>>(student.Attendances.ToList()));
            }
        }

        [HttpGet, Route("{id}/subject/{sid}/attendance")]
        [ResponseType(typeof(AttendanceDTO))]
		public IHttpActionResult GetAttendance(long id,long sid)
        {

            using (var ctx = new SchoolContext())
            {
                Student student = ctx.Students.Include("Attendances").Where(st => st.StudentID == id).FirstOrDefault();
                if (student == null)
                    return NotFound();
                List<Attendance> attendances = student.Attendances.Where(a => a.SubjectID == sid).ToList();
                return Ok(Mapper.Map<List<Attendance>, List<AttendanceDTO>>(attendances));
            }
        }

		[Authorize]
		public List<AttendanceDTO> GetAttendanceDTO(long id)
		{
			using (var ctx = new SchoolContext())
			{
				Student student = ctx.Students.Include("Attendances").Where(st => st.StudentID == id).FirstOrDefault();
				if (student == null)
					return null;
				var att = student.Attendances.ToList();
				return Mapper.Map<List<Attendance>, List<AttendanceDTO>>(student.Attendances.ToList());
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
        public IHttpActionResult Post(StudentDTO student)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    ctx.Students.Add(Mapper.Map<StudentDTO,Student>(student));
                    ctx.SaveChanges();
                }
                catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok(student);
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
        [HttpPut, Route("")]
        [ResponseType(typeof(void))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult Put(StudentDTO student)
        {

            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    var existingStudent= ctx.Students.Where(st => st.StudentID == student.StudentID).FirstOrDefault();
                    if (existingStudent==null)
                        return NotFound();
                    existingStudent.LastName = student.LastName;
                    existingStudent.FirstName = student.FirstName;
                    existingStudent.GroupID = student.GroupID;
                    existingStudent.SubGroup = student.SubGroup;
                    existingStudent.Email = student.Email;
                    existingStudent.Year = student.Year;
                    ctx.SaveChanges();
                }
                catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok();
            }

        }

        [HttpDelete, Route("{id}")]
        [ResponseType(typeof(void))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult Delete(int id)
        {
            using (var ctx = new SchoolContext())
            {
                Student student = ctx.Students.Where(st => st.StudentID == id).FirstOrDefault();
                if (student != null)
                    try
                    { 
                    ctx.Students.Remove(student);
                        ctx.SaveChanges();
                    }
                    catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok();
            }
        }
    }
}
