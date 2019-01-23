using System;
using System.Web.Mvc;
using lab9.Database;
using lab9.Models;

namespace lab9.Controllers
{
    public class AddController : Controller
    {
        public ActionResult Index()
        {
            return View ();
        }

        [HttpPost]
        public ActionResult Index(string city, string country, string description, string tourist, string cost)
        {
            if (string.IsNullOrWhiteSpace(city) || string.IsNullOrWhiteSpace(country) || string.IsNullOrWhiteSpace(description)
                || string.IsNullOrWhiteSpace(tourist) || string.IsNullOrWhiteSpace(cost))
            {
                Session["Error"] = "Add destination failed. All required fields must be filled correctly.";
                return RedirectToAction("Index");
            }
            try
            {
                DatabaseService.AddDestination(new Destination(city, country, description, int.Parse(tourist), int.Parse(cost)));
            }
            catch (Exception)
            {
				Session["Error"] = "Add destination failed. All required fields must be filled correctly.";
				return RedirectToAction("Index");
            }
            return Redirect("~/Main");
        }
    }
}
