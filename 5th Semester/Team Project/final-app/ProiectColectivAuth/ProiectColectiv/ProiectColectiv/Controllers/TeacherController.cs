using AutoMapper;
using ProiectColectiv.Models;
using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Security.Claims;
using System.Text;
using System.Web;
using System.Web.Http;
using System.Web.Http.Description;

namespace ProiectColectiv.Controllers
{



    [RoutePrefix("api/teacher")]
    public class TeacherController : ApiController
    {
        [HttpGet, Route("")]
        [ResponseType(typeof(IList<TeacherDTO>))]
		public IHttpActionResult Get()
        {
            using (var ctx = new SchoolContext())
            {
                return Ok(Mapper.Map<List<Teacher>, List<TeacherDTO>>(ctx.Teachers.ToList()));
            }
        }


		/// <summary>
		/// Gets a Address with the given id
		/// </summary>
		/// <param name="id">The id of the address</param>
		/// <returns>Status code: 200 (Ok) and an Address - if the action executed successfully
		///          Status code : 404 (Not Found) - if the address was NOT found</returns>
		[HttpGet, Route("{id}")]
        [ResponseType(typeof(TeacherDTO))]
		public IHttpActionResult Get(int id)
        {

            using (var ctx = new SchoolContext())
            {
                Teacher teacher = ctx.Teachers.Where(st => st.TeacherID == id).FirstOrDefault();
                if (teacher == null)
                    return NotFound();
                return Ok(Mapper.Map<Teacher, TeacherDTO>(teacher));
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
		public IHttpActionResult Post(TeacherDTO teacher)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    ctx.Teachers.Add(Mapper.Map<TeacherDTO, Teacher>(teacher));
                    ctx.SaveChanges();
                }
                catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok(teacher);
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
		public IHttpActionResult Put(TeacherDTO teacher)
        {

            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    var existingTeacher = ctx.Teachers.Where(st => st.TeacherID == teacher.TeacherID).FirstOrDefault();
                    if (existingTeacher == null)
                        return NotFound();
                    existingTeacher.LastName = teacher.LastName;
                    existingTeacher.FirstName = teacher.FirstName;
                    existingTeacher.Post = teacher.Post;
                    existingTeacher.Email = teacher.Email;
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
                Teacher teacher = ctx.Teachers.Where(st => st.TeacherID == id).FirstOrDefault();
                if (teacher != null)
                    try
                    {
                        ctx.Teachers.Remove(teacher);
                        ctx.SaveChanges();
                    }
                    catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok();
            }
        }
    }
}
