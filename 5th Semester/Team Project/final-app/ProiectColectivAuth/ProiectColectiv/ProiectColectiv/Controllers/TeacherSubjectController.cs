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
    [RoutePrefix("api/teachersubject")]
    public class TeacherSubjectController : ApiController
    {
        [HttpGet, Route("")]
        [ResponseType(typeof(IList<TeacherSubjectDTO>))]
		public IHttpActionResult Get()
        {
            using (var ctx = new SchoolContext())
            {
                return Ok(Mapper.Map<List<TeacherSubject>, List<TeacherSubjectDTO>>(ctx.TeacherSubjects.ToList()));
            }
        }

        /// <summary>
        /// Gets a Address with the given id
        /// </summary>
        /// <param name="id">The id of the address</param>
        /// <returns>Status code: 200 (Ok) and an Address - if the action executed successfully
        ///          Status code : 404 (Not Found) - if the address was NOT found</returns>
        [HttpGet, Route("{teacherId}/{subjectId}/{group}/{subgroup}")]
        [ResponseType(typeof(TeacherSubjectDTO))]
		public IHttpActionResult Get(int teacherId, int subjectId, int group, int subgroup)
        {

            using (var ctx = new SchoolContext())
            {
                TeacherSubject teacherSubject = ctx.TeacherSubjects.Where(st => st.TeacherID == teacherId && st.SubjectID == subjectId && st.GroupID == group && st.SubGroup == subgroup).FirstOrDefault();
                if (teacherSubject == null)
                    return NotFound();
                return Ok(Mapper.Map<TeacherSubject, TeacherSubjectDTO>(teacherSubject));
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
		public IHttpActionResult Post(TeacherSubjectDTO teachersubject)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            using (var ctx = new SchoolContext())
            {
                try
                {
                    ctx.TeacherSubjects.Add(Mapper.Map<TeacherSubjectDTO, TeacherSubject>(teachersubject));
                    ctx.SaveChanges();
                }
                catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok(teachersubject);
            }


        }


        [HttpGet, Route("{teacherId}/subject/{subjectId}/students")]
        [ResponseType(typeof(StudentDTO))]
		public IHttpActionResult GetStudents(int teacherId, int subjectId)
        {

            using (var ctx = new SchoolContext())
            {
                List<TeacherSubject> teacherSubjects = ctx.TeacherSubjects.Where(st => st.TeacherID == teacherId && st.SubjectID == subjectId).ToList();
                List<StudentDTO> students = new List<StudentDTO>();
                teacherSubjects.ForEach(ts =>
                {
                    List<Student> st;
                    if (ts.SubGroup == 0)
                        st = ctx.Students.Where(s => s.GroupID == ts.GroupID).ToList();
                    else
                        st = ctx.Students.Where(s => s.GroupID == ts.GroupID && s.SubGroup == ts.SubGroup).ToList();
                    List<StudentDTO> stDTO=Mapper.Map<List<Student>,List<StudentDTO>>(st);
                    stDTO.ForEach(s => students.Add(s));
                });
                return Ok(students);
            }
        }


        [HttpPost, Route("{teacherId}/subject/{subjectId}/year/{year}")]
        [ResponseType(typeof(StudentDTO))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult AssignYear(int teacherId, int subjectId,int year)
        {

            using (var ctx = new SchoolContext())
            {
                var groups = ctx.Students.Where(s => s.Year == year).Select(s => s.GroupID).Distinct().ToList();
                groups.ForEach(gr =>
                {
                    
                    try
                    {
                        
                        TeacherSubject teacherSubject = ctx.TeacherSubjects.Where(st => st.TeacherID == teacherId && st.SubjectID == subjectId && st.GroupID == gr).FirstOrDefault();
                        if (teacherSubject == null)
                        {
                            TeacherSubject ts = new TeacherSubject()
                            {
                                TeacherID = teacherId,
                                SubjectID = subjectId,
                                GroupID = gr,
                                SubGroup = 0

                            };
                            ctx.TeacherSubjects.Add(ts);
                            ctx.SaveChanges();
                        }
                        else
                            if (teacherSubject.SubGroup !=0)
                            {
                            teacherSubject.SubGroup = 0;
                            ctx.SaveChanges();
                            }
                    }
                    catch (Exception ex) { }
                });
                return Ok();
            }
        }

        [HttpPost, Route("{teacherId}/subject/{subjectId}/group/{group}/subgroup/{subgroup}")]
        [ResponseType(typeof(StudentDTO))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult AssignGroup(int teacherId, int subjectId, int group,int subgroup)
        {

            using (var ctx = new SchoolContext())
             {
                try
                {

                        TeacherSubject teacherSubject = ctx.TeacherSubjects.Where(st => st.TeacherID == teacherId && st.SubjectID == subjectId && st.GroupID == group).FirstOrDefault();
                        if (teacherSubject == null)
                        {
                            TeacherSubject ts = new TeacherSubject()
                            {
                                TeacherID = teacherId,
                                SubjectID = subjectId,
                                GroupID = group,
                                SubGroup = subgroup

                            };
                            ctx.TeacherSubjects.Add(ts);
                            ctx.SaveChanges();
                        }
                        else
                            if (teacherSubject.SubGroup != subgroup)
                        {
                            teacherSubject.SubGroup = subgroup;
                            ctx.SaveChanges();
                        }
                    }
                    catch (Exception ex) { }
            };
            return Ok();
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

        [HttpDelete, Route("{teacherId}/{subjectId}/{group}/{subgroup}")]
        [ResponseType(typeof(void))]
		[Authorize(Roles = "Teacher")]
		public IHttpActionResult Delete(int teacherId, int subjectId, int group, int subgroup)
        {
            using (var ctx = new SchoolContext())
            {
                TeacherSubject teacherSubject = ctx.TeacherSubjects.Where(st => st.TeacherID == teacherId && st.SubjectID == subjectId && st.GroupID == group && st.SubGroup == subgroup).FirstOrDefault();
                if (teacherSubject != null)
                    try
                    {
                        ctx.TeacherSubjects.Remove(teacherSubject);
                        ctx.SaveChanges();
                    }
                    catch (Exception exn) { return BadRequest(exn.ToString()); }
                return Ok();
            }
        }

    }
}
