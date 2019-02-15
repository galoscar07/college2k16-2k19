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
    [RoutePrefix("api/subject")]
    public class SubjectController : ApiController
    {
        [HttpGet, Route("")]
        [ResponseType(typeof(IList<SubjectDTO>))]
        public IHttpActionResult Get()
        {
            using (var ctx = new SchoolContext())
            {
                return Ok(Mapper.Map<List<Subject>, List<SubjectDTO>>(ctx.Subjects.ToList()));
            }
        }

        /// <summary>
        /// Gets a Address with the given id
        /// </summary>
        /// <param name="id">The id of the address</param>
        /// <returns>Status code: 200 (Ok) and an Address - if the action executed successfully
        ///          Status code : 404 (Not Found) - if the address was NOT found</returns>
        [HttpGet, Route("{id}")]
        [ResponseType(typeof(SubjectDTO))]
		public IHttpActionResult Get(int id)
        {

            using (var ctx = new SchoolContext())
            {
                Subject subject = ctx.Subjects.Where(st => st.SubjectID == id).FirstOrDefault();
                if (subject == null)
                    return NotFound();
                return Ok(Mapper.Map<Subject, SubjectDTO>(subject));
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
		public IHttpActionResult Post(SubjectDTO subject)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    ctx.Subjects.Add(Mapper.Map<SubjectDTO, Subject>(subject));
                    ctx.SaveChanges();
                }
                catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok(subject);
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
		public IHttpActionResult Put(SubjectDTO subject)
        {

            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    var existingSubject = ctx.Subjects.Where(st => st.SubjectID == subject.SubjectID).FirstOrDefault();
                    if (existingSubject == null)
                        return NotFound();
                    existingSubject.Title = subject.Title;
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
                Subject subject = ctx.Subjects.Where(st => st.SubjectID == id).FirstOrDefault();
                if (subject != null)
                    try
                    {
                        ctx.Subjects.Remove(subject);
                        ctx.SaveChanges();
                    }
                    catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok();
            }
        }
    }
}
