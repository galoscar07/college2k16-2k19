using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace ProiectColectiv
{
    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional }
            );

			routes.MapRoute(
				name: "Details",
				url: "Home/Teacher/{id}/{subjectId}/{type}/{weekNumber}",
				defaults: new { controller = "Home", action = "Teacher", id = UrlParameter.Optional, type = UrlParameter.Optional, subjectId = UrlParameter.Optional, weekNumber = UrlParameter.Optional }
			);


		}
    }
}
