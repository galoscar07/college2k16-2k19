using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using lab9.Database;
using lab9.Models;

namespace lab9.Controllers
{
    public class MainController : Controller
    {
		public ActionResult Index()
		{
			return View();
		}

        [HttpGet]
        public string GetDestination(string query = "")
        {
            return DatabaseService.GetDestination(query);
        }

		[HttpPost]
		[ValidateAntiForgeryToken]
		public ActionResult Index(string email, string password, string submit)
		{
			if (ModelState.IsValid)
			{
                var user = DatabaseService.GetUser(email, password);
				if (user != null && submit == "Login")
				{
                    Session["UserID"] = user.Id.ToString();
                    Session["UserName"] = user.Name;
					return RedirectToAction("Index");
				}
                else
                {
                    if (submit == "Register")
                    {
                        User newUser;
                        string name = email.Substring(0, email.IndexOf('@'));
                        newUser = new User(email, name);
                        int id = DatabaseService.AddUser(newUser, password);
                        if (id > 0)
                        {
                            newUser.Id = id;
                            Session["UserID"] = newUser.Id.ToString();
                            Session["UserName"] = newUser.Name;
                            return RedirectToAction("Index");
                        }
                        else
                        {
                            Session["Error"] = "User creation failed! A user with this email already exists!";
                        }
                    }
                }
			 }
			return View(new User());
		}

        [HttpGet]
        public ActionResult Index(string logout)
        {
            if (Session["UserID"] != null && logout == "out")
            {
                Session["UserID"] = null;
                Session["UserName"] = null;
            }
            return View();
        }

		[HttpGet]
		public ActionResult Delete(int id)
        {
            if (Session["UserID"] != null)
            {
                DatabaseService.DeleteDestination(id);
            }
            return Redirect("~/");
        }
	}
}
