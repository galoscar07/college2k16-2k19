using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using lab9.Database;
using lab9.Models;

namespace lab9.Controllers
{
    public class UpdateController : Controller
    {
        [HttpGet]
        public ActionResult Index(int id)
        {
            return View ("Index", DatabaseService.GetDestinationById(id));
        }

        [HttpPost]
		public ActionResult Index(string id, string city, string country, string description, string tourist, string cost)
		{
            if (string.IsNullOrWhiteSpace(city) || string.IsNullOrWhiteSpace(country) || string.IsNullOrWhiteSpace(description)
				|| string.IsNullOrWhiteSpace(tourist) || string.IsNullOrWhiteSpace(cost))
			{
				Session["Error"] = "Update destination failed. All required fields must be filled correctly.";
				return RedirectToAction("Index");
			}
			try
			{
                Destination dest = new Destination(city, country, description, int.Parse(tourist), int.Parse(cost));
                dest.Id = int.Parse(id);
                DatabaseService.UpdateDestination(dest);	
            }
			catch (Exception)
			{
				Session["Error"] = "Update destination failed. All required fields must be filled correctly.";
				return RedirectToAction("Index");
			}
			return Redirect("~/Main");
		}
    }
}
