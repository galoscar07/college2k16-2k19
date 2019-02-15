using AutoMapper;
using ProiectColectiv.Models;
using ProiectColectiv.Models.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http;
using System.Web.Mvc;
using System.Web.Optimization;
using System.Web.Routing;

namespace ProiectColectiv
{
    public class WebApiApplication : System.Web.HttpApplication
    {
        protected void Application_Start()
        {
            AreaRegistration.RegisterAllAreas();
            GlobalConfiguration.Configure(WebApiConfig.Register);
            FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
            RouteConfig.RegisterRoutes(RouteTable.Routes);
            BundleConfig.RegisterBundles(BundleTable.Bundles);
            Mapper.Initialize(cfg =>
            {
                cfg.CreateMap<Student, StudentDTO>().ReverseMap();
                cfg.CreateMap<Teacher, TeacherDTO>().ReverseMap();
                cfg.CreateMap<TeacherSubject, TeacherSubjectDTO>().ReverseMap();
                cfg.CreateMap<Attendance, AttendanceDTO>().ReverseMap();
                cfg.CreateMap<Subject, SubjectDTO>().ReverseMap();
            });
        }
    }
}
