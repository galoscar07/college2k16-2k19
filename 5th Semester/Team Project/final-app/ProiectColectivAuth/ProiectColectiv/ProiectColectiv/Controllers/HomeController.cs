using ProiectColectiv.Models;
using ProiectColectiv.Models.Domain;
using ProiectColectiv.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Web;
using System.Web.Mvc;

namespace ProiectColectiv.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewBag.Title = "Home Page";

            return View();
        }

		public ActionResult Login()
		{

			return View();
		}

        public ActionResult AddSubject()
        {

            return View();
        }

        public ActionResult Register()
        {

            return View();
        }

        public ActionResult Student(long? id)
		{
			long studentId = id.Value;
			AttendancesVM vm = new AttendancesVM();
			
			using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/student/" + studentId +"/attendance");
				var responseTask = client.GetAsync(client.BaseAddress);
				responseTask.Wait();

				var result = responseTask.Result;
				if (result.IsSuccessStatusCode)
				{
					var readTask = result.Content.ReadAsAsync<List<AttendanceDTO>>();
					readTask.Wait();
					vm.Attendances = readTask.Result;
				}
				else //web api sent error response 
				{
					ModelState.AddModelError(string.Empty, "Server error. Please contact administrator.");
				}
			}
			using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/teacher");
				var responseTask = client.GetAsync(client.BaseAddress);
				responseTask.Wait();
				var result = responseTask.Result;
				if (result.IsSuccessStatusCode)
				{
					var readTask = result.Content.ReadAsAsync<List<TeacherDTO>>();
					readTask.Wait();
					var dict = new Dictionary<long, string>();
					readTask.Result.ForEach(t => { if (!dict.ContainsKey(t.TeacherID)) dict.Add(t.TeacherID, "" + t.Post + " " + t.FirstName + " " + t.LastName); });
					vm.TeacherInfo = dict;
				}
				else //web api sent error response 
				{
					ModelState.AddModelError(string.Empty, "Server error. Please contact administrator.");
				}
			}
			using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/subject");
				var responseTask = client.GetAsync(client.BaseAddress);
				responseTask.Wait();
	
				var result = responseTask.Result;
				if (result.IsSuccessStatusCode)
				{
					var readTask = result.Content.ReadAsAsync<List<SubjectDTO>>();
					readTask.Wait();
					var dict = new Dictionary<long, string>();
					readTask.Result.ForEach(s => { if (!dict.ContainsKey(s.SubjectID)) dict.Add(s.SubjectID, s.Title); });
					vm.SubjectName = dict;
				}
				else //web api sent error response 
				{
					ModelState.AddModelError(string.Empty, "Server error. Please contact administrator.");
				}
			}
			return View(vm);
		}

		public ActionResult Teacher(long? id,long? subjectId, string type="string",int weekNumber=1)
        {
            TeacherVM vm = new TeacherVM();
            vm.TeacherId = id.Value;
            vm.SubjectId = subjectId.Value;
            vm.WeekNumber = weekNumber;
			vm.Type = type;
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/teachersubject/" + vm.TeacherId +"/subject/" + vm.SubjectId + "/students");

                //Called Member default GET All records  
                //GetAsync to send a GET request   
                // PutAsync to send a PUT request  
                var responseTask = client.GetAsync(client.BaseAddress);
                responseTask.Wait();
                //To store result of web api response.   
                var result = responseTask.Result;
                //If success received   
                if (result.IsSuccessStatusCode)
                {
                    var readTask = result.Content.ReadAsAsync<List<StudentDTO>>();
                    readTask.Wait();
                    vm.Students = readTask.Result;
                }
                else
                {
                    ModelState.AddModelError(string.Empty, "Server error try after some time.");
                }
            }
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/attendance");
                //Called Member default GET All records  
                //GetAsync to send a GET request   
                // PutAsync to send a PUT request  
                var responseTask = client.GetAsync(client.BaseAddress);
                responseTask.Wait();
                //To store result of web api response.   
                var result = responseTask.Result;
                //If success received   
                if (result.IsSuccessStatusCode)
                {
                    var readTask = result.Content.ReadAsAsync<List<AttendanceDTO>>();
                    readTask.Wait();
                    vm.Attendances = readTask.Result.Where(s=>s.SubjectID == vm.SubjectId && s.TypeOf.Equals(vm.Type) && s.WeekNumber==vm.WeekNumber && vm.Students.Exists(s1 => s1.StudentID == s.StudentID)).ToList();
                }
                else
                {
                    ModelState.AddModelError(string.Empty, "Server error try after some time.");
                }
            }
            return View("Teacher1",vm);
        }

		public ActionResult Subjects(long? id)
		{
			TeachersSubjectsVM vm = new TeachersSubjectsVM();
			vm.TeacherId = id.Value;
			var dict = new Dictionary<long, string>();
            var dictAll = new Dictionary<long, string>();
            using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/teachersubject");
				//Called Member default GET All records  
				//GetAsync to send a GET request   
				// PutAsync to send a PUT request  
				var responseTask = client.GetAsync(client.BaseAddress);
				responseTask.Wait();
				//To store result of web api response.   
				var result = responseTask.Result;
				//If success received   
				if (result.IsSuccessStatusCode)
				{
					var readTask = result.Content.ReadAsAsync<List<TeacherSubjectDTO>>();
					readTask.Wait();
					readTask.Result.ForEach(s => { if (!dict.ContainsKey(s.SubjectID)) dict.Add(s.SubjectID, ""); });
					vm.SubjectName = dict;
				}
				else
				{
					ModelState.AddModelError(string.Empty, "Server error try after some time.");
				}
			}
			using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/subject");

				//Called Member default GET All records  
				//GetAsync to send a GET request   
				// PutAsync to send a PUT request  
				var responseTask = client.GetAsync(client.BaseAddress);
				responseTask.Wait();
				//To store result of web api response.   
				var result = responseTask.Result;
				//If success received   
				if (result.IsSuccessStatusCode)
				{
					var readTask = result.Content.ReadAsAsync<List<SubjectDTO>>();
					readTask.Wait();
					readTask.Result.ForEach(s =>
                    {
                        if (dict.ContainsKey(s.SubjectID)) dict[s.SubjectID] = s.Title;
                        if (!dictAll.ContainsKey(s.SubjectID)) dictAll.Add(s.SubjectID, s.Title);
                    });
					vm.SubjectName = dict;
                    vm.AllSubjectName = dictAll;
				}
				else
				{
					ModelState.AddModelError(string.Empty, "Server error try after some time.");
				}
			}
			return View("Subjects", vm);
		}


        public ActionResult SubjectsAssign(long? id)
        {
            TeachersSubjectsVM vm = new TeachersSubjectsVM();
            vm.TeacherId = id.Value;
            var dict = new Dictionary<long, string>();
            var dictAll = new Dictionary<long, string>();
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/teachersubject");
                //Called Member default GET All records  
                //GetAsync to send a GET request   
                // PutAsync to send a PUT request  
                var responseTask = client.GetAsync(client.BaseAddress);
                responseTask.Wait();
                //To store result of web api response.   
                var result = responseTask.Result;
                //If success received   
                if (result.IsSuccessStatusCode)
                {
                    var readTask = result.Content.ReadAsAsync<List<TeacherSubjectDTO>>();
                    readTask.Wait();
                    readTask.Result.ForEach(s => { if (!dict.ContainsKey(s.SubjectID)) dict.Add(s.SubjectID, ""); });
                    vm.SubjectName = dict;
                }
                else
                {
                    ModelState.AddModelError(string.Empty, "Server error try after some time.");
                }
            }
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://ubbacademicinfo.azurewebsites.net/api/subject");

                //Called Member default GET All records  
                //GetAsync to send a GET request   
                // PutAsync to send a PUT request  
                var responseTask = client.GetAsync(client.BaseAddress);
                responseTask.Wait();
                //To store result of web api response.   
                var result = responseTask.Result;
                //If success received   
                if (result.IsSuccessStatusCode)
                {
                    var readTask = result.Content.ReadAsAsync<List<SubjectDTO>>();
                    readTask.Wait();
                    readTask.Result.ForEach(s =>
                    {
                        if (dict.ContainsKey(s.SubjectID)) dict[s.SubjectID] = s.Title;
                        if (!dictAll.ContainsKey(s.SubjectID)) dictAll.Add(s.SubjectID, s.Title);
                    });
                    vm.SubjectName = dict;
                    vm.AllSubjectName = dictAll;
                }
                else
                {
                    ModelState.AddModelError(string.Empty, "Server error try after some time.");
                }
            }
            return View("AssignSubject", vm);
        }


    }
}
